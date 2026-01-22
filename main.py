import os
import asyncio
import pandas as pd
import numpy as np
from metaapi_cloud_sdk import MetaApi
from supabase import create_client, Client
import google.generativeai as genai
from datetime import datetime

# --- CREDENCIALES ---
SUPABASE_URL = "https://twijbhpgusigkxaxxbgg.supabase.co"
SUPABASE_KEY = "sb_secret_U3-Q59QI0KD5hukufSEvqw_hUSpevKA"
CLAVE_GEMINI = "AIzaSyBIeuYf395dfR3kgGr5Z730s6gWg5P0oVg"
CUENTA_ID = "074b666f-ded6-49aa-a349-0fa7e8ac4757"

# Inicialización de Clientes
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
genai.configure(api_key=CLAVE_GEMINI)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURACIÓN DE RIESGO [cite: 2026-01-21] ---
SIMBOLO = "US500"
LOTE_ESTANDAR = 0.03 

def guardar_charla_ia(categoria, instruccion):
    try:
        data = {
            "categoria": categoria,
            "detalle_instruccion": instruccion,
            "estado_strategy": "GitHub-Fly.io | Riesgo Max 30%"
        }
        supabase.table("memoria_conversacion").insert(data).execute()
    except Exception as e:
        print(f"Error en memoria: {e}")

async def gestionar_conexion_metaapi(api, encender=True):
    try:
        cuenta = await api.metatrader_account_api.get_account(CUENTA_ID)
        if encender:
            print("🚀 Desplegando cuenta...")
            await cuenta.deploy()
            await cuenta.wait_connected()
        else:
            print("💤 Suspendiendo cuenta...")
            await cuenta.undeploy()
    except Exception as e:
        print(f"Error de conexión: {e}")

def obtener_analisis_vsa_completo():
    try:
        res = supabase.table("monitoreo_diamante_pro").select("*").order("timestamp", desc=True).limit(100).execute()
        if not res.data: return None
        
        df = pd.DataFrame(res.data)
        ultimo = df.iloc[0]
        
        # Lógica de Diamante [cite: 2026-01-19]
        es_diamante = ultimo['volumen_dic_institutional'] > 500
        es_trampa = ultimo['volumen_esfuerzo_oculto'] > 1000
        ma200 = df['precio_ia_master'].rolling(window=20).mean().iloc[0]
        
        return {
            "es_diamante": es_diamante, "es_trampa": es_trampa,
            "precio": ultimo['precio_ia_master'], "ma200": ma200
        }
    except:
        return None

async def ejecutar_estrategia(api, vsa):
    if vsa['es_trampa']: return 

    decision = None
    if vsa['es_diamante'] and vsa['precio'] > vsa['ma200']:
        decision = "COMPRA"
    
    if decision:
        await gestionar_conexion_metaapi(api, encender=True)
        # Aquí se ejecutaría la orden al detectar el Diamante
        guardar_charla_ia("EJECUCIÓN", f"Operación {decision} por Diamante al 10% riesgo.")
        # Se puede agregar lógica de cierre según tu regla de SL movible [cite: 2026-01-21]

async def main():
    token = os.getenv("META_API_TOKEN")
    if not token:
        print("❌ Error: No se detectó META_API_TOKEN")
        return

    api = MetaApi(token)
    guardar_charla_ia("SISTEMA", "Bot Activo: Londres/NY operando.")

    while True:
        vsa = obtener_analisis_vsa_completo()
        if vsa:
            await ejecutar_estrategia(api, vsa)
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
