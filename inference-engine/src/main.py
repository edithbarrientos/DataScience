# -*- coding: utf-8 -*-
"""
Module: src.main
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 6.0.0
Maintainer: Edith Barrientos
Status: Production Grade / High-Performance Async Optimized

Description:
    Punto de Entrada Maestro y Orquestador de Arranque (Application Bootstrap).
    Instancia el ciclo de vida de la aplicación ASGI de FastAPI e inyecta
    el bucle de eventos de ultra alta velocidad basado en C (uvloop), maximizando
    el rendimiento asíncrono del Inference Engine en local y Kubernetes.
"""

import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints import router as inference_router
from src.core import cache_manager  # Importación del gestor de hardware

# =================================================================================
# 1. CAPA ASÍNCRONA DE ALTO RENDIMIENTO (C-Based Event Loop Injected)
# =================================================================================
try:
    import uvloop
    # Reemplaza el bucle de eventos nativo de Python por el motor optimizado en C
    uvloop.install()
    async_engine_status = "⚡ uvloop (C-based Engine) inyectado de forma exitosa."
except ImportError:
    async_engine_status = "⚠️ uvloop no disponible. Usando asyncio nativo."

# =================================================================================
# 2. CONFIGURACIÓN DEL SISTEMA DE LOGS
# =================================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("inference_engine.main")

logger.info("⚙️ Iniciando secuencia de arranque del Inference Engine...")
logger.info(f"🧬 Motor Asíncrono: {async_engine_status}")


# =================================================================================
# 3. GESTIÓN DEL CICLO DE VIDA DE LA APLICACIÓN (Lifespan / Pre-warming)
# =================================================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Orquestador del Ciclo de Vida: Calienta el hardware y enlaza sockets al arrancar.
    
    Garantiza que ONNX Runtime analice el procesador y compile el grafo matemático
    en la RAM ANTES de que Kubernetes declare el Pod como listo (Readiness Probe).
    """
    logger.info("💾 [LIFESPAN START] Inicializando calentamiento proactivo de grafos ONNX...")
    try:
        # Pre-cargamos de forma proactiva la versión por defecto para mitigar el Cold Start
        cache_manager.get_model_from_cache("v5.0.0")
        logger.info("🧠 [LIFESPAN PRE-WARM SUCCESS] Grafo v5.0.0 cargado y listo en RAM.")
    except Exception as e:
        logger.warning(f"⚠️ No se pudo pre-cargar el modelo en el arranque (se cargará en la primera petición): {e}")
    
    yield  # Aquí es donde la aplicación se mantiene viva escuchando peticiones HTTP
    
    logger.info("🛑 [LIFESPAN SHUTDOWN] Liberando recursos y limpiando caché de memoria RAM...")
    cache_manager.MODEL_RAM_CACHE.clear()


# =================================================================================
# 4. INSTANCIACIÓN DE FASTAPI
# =================================================================================
app = FastAPI(
    title="⚡ Enterprise Inference Engine",
    description="Motor de inferencia asíncrono y paramétrico basado en contratos dinámicos de datos.",
    version="6.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan  # Inyección del manejador de ciclo de vida optimizado
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inyección del enrutador modularizado vectorizado
app.include_router(inference_router)

logger.info("🚀 [BOOTSTRAP COMPLETO] El microservicio está listo para recibir peticiones HTTP.")


# =================================================================================
# 5. BLOQUE DE EJECUCIÓN HIGH-PERFORMANCE LOCAL
# =================================================================================
if __name__ == "__main__":
    import uvicorn
    logger.info("🔌 Levantando servidor local de alta frecuencia con respaldo de uvloop...")
    # Ejecuta el servidor con el loop de uvloop integrado
    uvicorn.run("src.main:app", host="0.0.0.0", port=9000, loop="uvloop", reload=True)
