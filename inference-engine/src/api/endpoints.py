# -*- coding: utf-8 -*-
"""
Module: src.api.endpoints
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 8.0.0
Maintainer: Edith Barrientos
Status: Production Grade / Branchless Programming / Pylance Defeated

Description:
    Capa de Presentación - Controladores de Red Asíncronos de Alta Frecuencia (API Routing Layer).
    Este módulo expone la interfaz de comunicación HTTP del microservicio 'inference-engine'
    utilizando el framework de alto rendimiento FastAPI (ASGI). 
"""

import time
import logging
import numpy as np
from fastapi import APIRouter, HTTPException, status, Response
from typing import Dict, Any, List, Callable

# Importaciones externas oficiales de la librería Prometheus
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Importación estricta de módulos completos para neutralizar alertas estáticas de Pylance
from src.core import telemetry
from src.core import cache_manager

# Configuración del registrador de trazas de la aplicación
logger = logging.getLogger("inference_engine.endpoints")

# Instanciación del router modularizado con tags para la autodocumentación OpenAPI
router = APIRouter(tags=["Inference Engine Core Endpoints"])

# Global placeholder para la inyección paramétrica del contrato activo en el arranque
ACTIVE_CONTRACT_SCHEMA: Any = None

# =================================================================================
# ALGORITMO 1: PATRÓN STATE ALGEBRAICO (Branchless Circuit Breaker)
# =================================================================================
STATE_CLOSED = 0
STATE_OPEN = 1
STATE_HALF_OPEN = 2

current_state_index = STATE_CLOSED
failure_count = 0
failure_threshold = 3
last_state_change = time.time()
cooldown_period = 10.0


# =================================================================================
# 1. ENDPOINTS DE VERIFICACIÓN OPERACIONAL (Kubernetes Probes & Telemetry)
# =================================================================================

@router.get("/health", status_code=status.HTTP_200_OK, summary="Health Check Liveness Probe")
async def health_check() -> Dict[str, str]:
    """Sonda de diagnóstico operacional utilizada por los orquestadores de clúster (K8s)."""
    return {
        "status": "healthy",
        "circuit_state_index": str(current_state_index),
        "engine": "FastAPI Branchless ONNX Engine"
    }


@router.get("/metrics", summary="Prometheus Telemetry Scrape Endpoint")
async def metrics() -> Response:
    """Expone el registro y estado de las métricas internas analíticas del microservicio."""
    try:
        return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
    except Exception as telemetry_err:
        logger.error(f"Error al generar métricas analíticas: {str(telemetry_err)}")
        return Response(
            content="# Telemetry core initialization pending or unreachable in local machine", 
            media_type="text/plain"
        )
# =================================================================================
# ALGORITMO 2: TABLA DE DESPACHO POLIMÓRFICA (O(1) Dispatch Table)
# =================================================================================

def execute_closed_state(payload: Dict[str, Any], start_time: float) -> Dict[str, Any]:
    """Procesamiento estándar cuando el circuito está operativo (CLOSED)."""
    global current_state_index, failure_count, last_state_change
    
    model_meta = payload.get("model_meta", {})
    data = payload.get("data", [])
    features_names = payload.get("features_names", [])
    version = model_meta.get("model_version", "v1.0.0") if isinstance(model_meta, dict) else getattr(model_meta, "model_version", "v1.0.0")
    model_name = model_meta.get("model_name", "generic-model") if isinstance(model_meta, dict) else getattr(model_meta, "model_name", "generic-model")

    try:
        # 1. Transformación matricial vectorizada estricta float32 exigida por ONNX
        np_matrix = np.array([[row[feat] for feat in features_names] for row in data], dtype=np.float32)
        
        # ALGORITMO 3: ÁLGEBRA BOOLEANA VECTORIZADA (Branchless Guard Clause)
        is_matrix_valid = int(np_matrix.size > 0)
        _ = 1 / is_matrix_valid  # Provoca una excepción matemática controlada si está vacía sin usar if/else

        # 2. Invocación de la sesión de ONNX Runtime activa en memoria RAM a través del gestor de caché
        onnx_session = cache_manager.get_model_from_cache(version)
        
        # El grafo de ONNX espera un diccionario mapeado por el nombre de la variable de entrada
        input_name = onnx_session.get_inputs()[0].name
        
        # Inferencia matemática pura ejecutada en C++ nativo a nivel de hardware por ONNX Runtime
        raw_predictions = onnx_session.run(None, {input_name: np_matrix})
        
        # Colapsamos la matriz si la salida viene en dos dimensiones y la pasamos a lista nativa
        predictions_list = np.array(raw_predictions).flatten().tolist()
            
        latency = time.perf_counter() - start_time
        
        # Reinicio aritmético de fallos (Branchless reset)
        failure_count = 0 
        
        # Extracción y registro atributivo de telemetría directo (Inmune a fallos de Pylance)
        telemetry.INFERENCE_LATENCY.labels(model_version=version).observe(latency)
        telemetry.REQUEST_COUNTER.labels(endpoint="/predict", version=version, status="success").inc()
            
        logger.info(f"🚀 [INFERENCIA ONNX EXITOSA] 📊 {model_name} ({version}) ejecutado | Latencia: {latency:.6f}s")
        
        return {
            "status": "success",
            "model_executed": model_name,
            "version_executed": version,
            "latency_seconds": latency,
            "total_records": len(predictions_list),
            "predictions": predictions_list
        }
    except Exception as core_err:
        failure_count += 1
        
        # Matriz de Transición Algebraica (Calcula el cambio de estado sin condiciones ni saltos)
        should_open = int(failure_count >= failure_threshold)
        current_state_index = (current_state_index * (1 - should_open)) + (STATE_OPEN * should_open)
        last_state_change = (last_state_change * (1 - should_open)) + (time.time() * should_open)
        
        logger.error(f"🚨 [FALLO REGISTRADO] Estado indexado del disyuntor: {current_state_index} | Error: {str(core_err)}")
        raise HTTPException(status_code=500, detail="Fallo en Inference Engine ONNX Compute.")

def execute_open_state(payload: Dict[str, Any], start_time: float) -> Dict[str, Any]:
    """Modo degradado de contingencia ultra rápido (OPEN) sin evaluar condiciones de negocio."""
    global current_state_index, last_state_change
    
    # Evalúa aritméticamente el tiempo de enfriamiento (Cooldown Validation)
    time_passed = time.time() - last_state_change
    is_cooldown_complete = int(time_passed > cooldown_period)
    
    # Transición elástica de estados sin if/else: Si el tiempo pasó, salta a HALF-OPEN (Índice 2)
    current_state_index = (current_state_index * (1 - is_cooldown_complete)) + (STATE_HALF_OPEN * is_cooldown_complete)
    
    logger.warning("🛡️ [CIRCUITO ABIERTO] Sistema en autoprotección ONNX. Retornando Graceful Fallback.")
    return {
        "status": "degraded_fallback_mode",
        "message": "Circuito activo para autoprotección del clúster ante estrés computacional.",
        "predictions": [0.0] * len(payload.get("data", []))
    }

def execute_half_open_state(payload: Dict[str, Any], start_time: float) -> Dict[str, Any]:
    """Estado de prueba operativa (HALF-OPEN). Intenta canalizar el flujo al canal operativo."""
    logger.info("🔧 [DISYUNTOR] Intentando autorecuperación en canal controlado...")
    return execute_closed_state(payload, start_time)

# La Tabla de Despacho O(1) vincula los índices numéricos directamente con sus funciones en RAM
DISPATCH_TABLE: Dict[int, Callable[[Dict[str, Any], float], Dict[str, Any]]] = {
    STATE_CLOSED: execute_closed_state,
    STATE_OPEN: execute_open_state,
    STATE_HALF_OPEN: execute_half_open_state
}

# =================================================================================
# ENDPOINT CENTRAL DE ENTRADA HTTP POST
# =================================================================================

@router.post("/predict", status_code=status.HTTP_200_OK, summary="Execute Ultra-Fast Parametric Inference")
async def predict_inference(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Endpoint maestro que ejecuta el ruteo O(1) libre de saltos de CPU (Branchless)."""
    start_time = time.perf_counter()
    
    # EXECUCIÓN EN TIEMPO CONSTANTE O(1):
    # Se elimina por completo la secuencia de 'if/elif/else' tradicionales del hot path.
    state_executor = DISPATCH_TABLE[current_state_index]
    return state_executor(payload, start_time)
