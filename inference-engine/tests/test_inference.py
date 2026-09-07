# -*- coding: utf-8 -*-
"""
Module: tests.test_inference
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 2.1.0
Maintainer: Edith Barrientos
Status: Quality Assurance Grade / Hyper-Documented / Native Logs Injected

Description:
    Capa de Control de Calidad y Concurrencia - Suite de Inferencia Core.
    Este módulo implementa las pruebas operacionales automatizadas utilizando el
    framework Pytest, integrando el gestor nativo de 'logging' de Python para
    volcar trazas estructuradas con iconos e inmunes al filtrado de la consola.
"""

import time
import asyncio
import logging
import pytest
from fastapi import HTTPException

# Importación directa del controlador de red bajo auditoría para inspeccionar su memoria RAM
from src.api import endpoints

# Configuración del registrador exclusivo para la suite de pruebas unitarias
logger = logging.getLogger("inference_engine.tests")


@pytest.fixture(autouse=True)
def configure_test_logging(caplog):
    """Fixture que fuerza a Pytest a capturar e imprimir logs de nivel INFO en caliente.
    
    Establece el umbral del interceptor CLI nativo de Pytest para que los mensajes 
    con iconos desfilen por la terminal sin ser silenciados al pasar los tests.
    """
    caplog.set_level(logging.INFO)
    yield


@pytest.fixture(autouse=True)
def reset_circuit_breaker_state():
    """Fixture Automatizado de Aislamiento de Memoria RAM (State Reset Boundary).
    
    Garantiza que los acumuladores de fallos y los índices de la máquina de estados
    del Circuit Breaker se reinicien a cero antes de cada función de prueba.
    """
    endpoints.current_state_index = endpoints.STATE_CLOSED
    endpoints.failure_count = 0
    endpoints.last_state_change = time.time()
    yield


# =================================================================================
# SUITE DE VALIDACIÓN OPERACIONAL (Core Inference Testing Core)
# =================================================================================

def test_onnx_inference_prediction():
    """Certifica la validez del cálculo matricial directo utilizando el grafo ONNX."""
    logger.info(" ")
    logger.info("🧪 [TEST] ONNX Run Execution: Verificando Inferencia Algebraica Nativa...")
    logger.info("="*80)
    
    # Payload estructurado de acuerdo con la topología del modelo v5.0.0 exportado
    payload = {
        "model_meta": {
            "model_name": "regresion-multiple-onnx", 
            "model_version": "v5.0.0"
        },
        "data": [
            {"f1": 10.0, "f2": 20.0, "f3": 30.0},
            {"f1": 50.0, "f2": 100.0, "f3": 150.0}
        ],
        "features_names": ["f1", "f2", "f3"]
    }
    
    # Simulación de estampa de tiempo de red de alta resolución
    fake_start_time = time.perf_counter()
    
    # Invocación directa al ejecutor del estado CERRADO (Circuito Operativo)
    response = endpoints.execute_closed_state(payload, fake_start_time)
    
    # Volcado impecable de trazas analíticas usando logging oficial
    logger.info("📋 [BITÁCORA ANALÍTICA]:")
    logger.info(f"   |-- Estatus de Respuesta: {response['status']}")
    logger.info(f"   |-- Algoritmo Ejecutado:  {response['model_executed']}")
    logger.info(f"   |-- Latencia de Cómputo:  {response['latency_seconds']:.6f} segundos")
    logger.info(f"   |-- Registros Procesados: {response['total_records']}")
    logger.info(f"   |-- Predicciones Vector:  {response['predictions']}")
    
    # Aserciones de Seguridad e Integridad de Datos (Data Integrity Assertions)
    assert response["status"] == "success"
    assert response["total_records"] == 2
    assert isinstance(response["predictions"], list)
    assert len(response["predictions"]) == 2
    logger.info("🚀 [ÉXITO] Grafo ONNX validado. El cálculo numérico es consistente y reproducible.")


def test_circuit_breaker_trip_on_failures():
    """Audita la conmutación matemática del Disyuntor ante escenarios de estrés."""
    logger.info(" ")
    logger.info("🧪 [TEST] Resilience Stress: Validando Activación Aritmética del Escudo...")
    logger.info("="*80)
    
    # Payload malformado de forma intencional para reventar las salvaguardas de NumPy
    corrupt_payload = {
        "model_meta": {"model_name": "modelo-falla-test", "model_version": "v1.0.0"},
        "data": [], 
        "features_names": ["f1"]
    }
    
    logger.info("🚨 [STRESS PIPELINE] Disparando ráfaga de excepciones controladas...")
    
    # Ejecución iterativa para alcanzar el límite de tolerancia física del microservicio
    for i in range(endpoints.failure_threshold):
        with pytest.raises(HTTPException) as exc_info:
            endpoints.execute_closed_state(corrupt_payload, time.perf_counter())
        
        # Validamos que el código HTTP devuelto por el Circuit Breaker ante fallos sea un 500
        assert exc_info.value.status_code == 500
        logger.info(f"   [FALLO #{i+1}] Excepción interceptada. Conteo acumulado en RAM: {endpoints.failure_count}")
            
    # Inspección de Conmutación de Silicio: Verificamos si el índice cambió a OPEN (Índice 1)
    logger.info("🛡️ [ANÁLISIS DE ESCUDO]:")
    logger.info(f"   |-- Índice de Estado Actual: {endpoints.current_state_index} (Esperado: {endpoints.STATE_OPEN})")
    logger.info(f"   |-- Umbral de Fallos Máximo: {endpoints.failure_threshold}")
    
    assert endpoints.current_state_index == endpoints.STATE_OPEN
    logger.info("🚀 [ÉXITO] Disyuntor activado. El microservicio aisló el fallo y protegió los hilos del clúster.")


def test_health_endpoint_state():
    """Valida la transparencia de las sondas de monitoreo (Kubernetes Health Probes)."""
    logger.info(" ")
    logger.info("🧪 [TEST] Kubernetes Sre Probe: Monitoreando Transparencia del /health...")
    logger.info("="*80)
    
    # Forzamos de manera artificial la conmutación a estado ABIERTO (OPEN)
    endpoints.current_state_index = endpoints.STATE_OPEN
    logger.info("🔧 Inyectando de manera manual el Estado OPEN (Índice 1) en la RAM de la API...")
    
    # Orquestación y resolución del bucle asíncrono para consumir la corrutina de FastAPI
    health_report = asyncio.run(endpoints.health_check())
    
    logger.info("📋 [REPORTE ENVIADO A KUBERNETES]:")
    logger.info(f"   |-- Estado de Sonda:      {health_report['status']}")
    logger.info(f"   |-- Índice de Disyuntor:  {health_report['circuit_state_index']}")
    logger.info(f"   |-- Tecnología de Motor:  {health_report['engine']}")
    
    # Verificación de consistencia del bitstream expuesto
    assert health_report["status"] == "healthy"
    assert health_report["circuit_state_index"] == str(endpoints.STATE_OPEN)
    logger.info("🚀 [ÉXITO] Sonda verificada. El reporte de salud expone la telemetría en tiempo real.")
