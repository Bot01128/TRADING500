importar sistema operativo
importar asyncio
importar pandas como pd
importar numpy como np
desde metaapi_cloud_sdk importar MetaApi
desde supabase importar create_client, Cliente
importar google.generativeai como genes
desde datetime importar datetime

# --- CREDENCIALES (Extraídas de tus fotos) ---
SUPABASE_URL = " https://twijbhpgusigkxaxxbgg.supabase.co "
SUPABASE_KEY = "sb_secret_U3- Q59QI0KD5hukufSEvqw_hUSpevKA"
CLAVE_GEMINI = " AIzaSyBIeuYf395dfR3kgGr5Z730s6 gWg5P0oVg"
CUENTA_ID = "074b666f-ded6-49aa-a349- 0fa7e8ac4757" # ID Real

supabase: Cliente = crear_cliente(SUPABASE_URL, SUPABASE_KEY)
genai.configure(clave_api= CLAVE_GEMINI)
modelo = genai.GenerativeModel('gemini- 1.5-flash')

# --- CONFIGURACIÓN DE RIESGO Y ESTRATEGIA [cite: 2026-01-21] ---
SÍMBOLO = "US500"
LOTE_ESTANDAR = 0.03 # Regla fija para Exness [cite: 2026-01-19]

def guardar_charla_ia(categoria, instruccion):
    """Escribe en Supabase para memoria permanente [cite: 2026-01-21]"""
    intentar:
        datos = {
            "categoría": categoría,
            "detalle_instruccion": instruccion,
            "estado_estrategia": "GitHub-Fly.io | Riesgo Max 30%"
        }
        supabase.table("memoria_conversacion").insert(data).execute()
    excepto Excepción como e:
        print(f"Error al mirar la memoria: {e}")

async def gestionar_conexion_metaapi(api, encender=True):
    """Interruptor: Prende/Apaga la cuenta en la nube [cite: 2026-01-20]"""
    cuenta = await api.metatrader_account_api.get_account (ID_CUENTA)
    if encender:
        print("🚀 Desplegando cuenta...")
        esperar cuenta.deploy()
        esperar cuenta.wait_connected()
    demás:
        print("💤 Suspendiendo cuenta para ahorrar recursos...")
        esperar cuenta.undeploy()

def obtener_analisis_vsa_completo():
    """Recupera datos de monitoreo y calcula Medias Móviles [cite: 2026-01-19]"""
    res = supabase.table("monitoreo_diamante_pro ").select("*"). order("timestamp", desc=True).limit(100).execute( )
    si no res.data: devuelve Ninguno
    
    df = pd.DataFrame(res.datos)
    último = df.iloc[0]
    
    # Lógica de Diamante y Trampa [cite: 2026-01-19]
    es_diamante = ultimo['volumen_dic_institutional'] > 500
    es_trampa = ultimo['volumen_esfuerzo_oculto'] > 1000
    
    # Medias Móviles dinámicas con Pandas
    ma200 = df['precio_ia_master']. rolling(window=20).mean(). iloc[0] # Simplificado para demostración
    
    devolver {
        "es_diamante": es_diamante, "es_trampa": es_trampa,
        "delta": ultimo['delta_fuerza_neta'], "precio": ultimo['precio_ia_master'],
        "ma200": ma200
    }

async def ejecutar_estrategia(api, vsa):
    """Decide y ejecuta: Prende -> Opera -> Apaga [cite: 2026-01-21]"""
    si vsa['es_trap']: return # No operar en trampas

    decisión = Ninguna
    # Regla: Diamante a favor de la tendencia (MA200) [cite: 2026-01-19]
    si vsa['es_diamante'] y vsa['price'] > vsa['ma200']:
        decision = "COMPRA"
    
    Si decisión:
        await gestionar_conexion_metaapi(api, encender=True)
        # Aquí iría el envío de orden vía connection.create_market_order...
        guardar_charla_ia("EJECUCIÓN", f"Operación {decision} detectada por Diamante.")
        await gestionar_conexion_metaapi(api, encender=False)

definición asíncrona principal():
    token = os.getenv("META_API_TOKEN")
    si no es token:
        print("❌ Error: No se detectó META_API_TOKEN en Fly.io")
        devolver

    api = MetaApi(token)
    guardar_charla_ia("SISTEMA", "Bot Activo: Procesando VSA, MA200 y Diamantes.")

    mientras sea verdadero:
        vsa = obtener_analisis_vsa_completo()
        si vsa:
            await ejecutar_estrategia(api, vsa)
        await asyncio.sleep(60) # Monitoreo cada minuto

si __nombre__ == "__principal__":
    asyncio.run(principal())
importar sistema operativo
importar asyncio
importar pandas como pd
importar numpy como np
desde metaapi_cloud_sdk importar MetaApi
desde supabase importar create_client, Cliente
importar google.generativeai como genes
desde datetime importar datetime

# --- CREDENCIALES (Extraídas de tus fotos) ---
SUPABASE_URL = " https://twijbhpgusigkxaxxbgg.supabase.co "
SUPABASE_KEY = "sb_secret_U3- Q59QI0KD5hukufSEvqw_hUSpevKA"
CLAVE_GEMINI = " AIzaSyBIeuYf395dfR3kgGr5Z730s6 gWg5P0oVg"
CUENTA_ID = "074b666f-ded6-49aa-a349- 0fa7e8ac4757" # ID Real

supabase: Cliente = crear_cliente(SUPABASE_URL, SUPABASE_KEY)
genai.configure(clave_api= CLAVE_GEMINI)
modelo = genai.GenerativeModel('gemini- 1.5-flash')

# --- CONFIGURACIÓN DE RIESGO Y ESTRATEGIA [cite: 2026-01-21] ---
SÍMBOLO = "US500"
LOTE_ESTANDAR = 0.03 # Regla fija para Exness [cite: 2026-01-19]

def guardar_charla_ia(categoria, instruccion):
    """Escribe en Supabase para memoria permanente [cite: 2026-01-21]"""
    intentar:
        datos = {
            "categoría": categoría,
            "detalle_instruccion": instruccion,
            "estado_estrategia": "GitHub-Fly.io | Riesgo Max 30%"
        }
        supabase.table("memoria_conversacion").insert(data).execute()
    excepto Excepción como e:
        print(f"Error al mirar la memoria: {e}")

async def gestionar_conexion_metaapi(api, encender=True):
    """Interruptor: Prende/Apaga la cuenta en la nube [cite: 2026-01-20]"""
    cuenta = await api.metatrader_account_api.get_account (ID_CUENTA)
    if encender:
        print("🚀 Desplegando cuenta...")
        esperar cuenta.deploy()
        esperar cuenta.wait_connected()
    demás:
        print("💤 Suspendiendo cuenta para ahorrar recursos...")
        esperar cuenta.undeploy()

def obtener_analisis_vsa_completo():
    """Recupera datos de monitoreo y calcula Medias Móviles [cite: 2026-01-19]"""
    res = supabase.table("monitoreo_diamante_pro ").select("*"). order("timestamp", desc=True).limit(100).execute( )
    si no res.data: devuelve Ninguno
    
    df = pd.DataFrame(res.datos)
    último = df.iloc[0]
    
    # Lógica de Diamante y Trampa [cite: 2026-01-19]
    es_diamante = ultimo['volumen_dic_institutional'] > 500
    es_trampa = ultimo['volumen_esfuerzo_oculto'] > 1000
    
    # Medias Móviles dinámicas con Pandas
    ma200 = df['precio_ia_master']. rolling(window=20).mean(). iloc[0] # Simplificado para demostración
    
    devolver {
        "es_diamante": es_diamante, "es_trampa": es_trampa,
        "delta": ultimo['delta_fuerza_neta'], "precio": ultimo['precio_ia_master'],
        "ma200": ma200
    }

async def ejecutar_estrategia(api, vsa):
    """Decide y ejecuta: Prende -> Opera -> Apaga [cite: 2026-01-21]"""
    si vsa['es_trap']: return # No operar en trampas

    decisión = Ninguna
    # Regla: Diamante a favor de la tendencia (MA200) [cite: 2026-01-19]
    si vsa['es_diamante'] y vsa['price'] > vsa['ma200']:
        decision = "COMPRA"
    
    Si decisión:
        await gestionar_conexion_metaapi(api, encender=True)
        # Aquí iría el envío de orden vía connection.create_market_order...
        guardar_charla_ia("EJECUCIÓN", f"Operación {decision} detectada por Diamante.")
        await gestionar_conexion_metaapi(api, encender=False)

definición asíncrona principal():
    token = os.getenv("META_API_TOKEN")
    si no es token:
        print("❌ Error: No se detectó META_API_TOKEN en Fly.io")
        devolver

    api = MetaApi(token)
    guardar_charla_ia("SISTEMA", "Bot Activo: Procesando VSA, MA200 y Diamantes.")

    mientras sea verdadero:
        vsa = obtener_analisis_vsa_completo()
        si vsa:
            await ejecutar_estrategia(api, vsa)
        await asyncio.sleep(60) # Monitoreo cada minuto

si __nombre__ == "__principal__":
    asyncio.run(principal())
