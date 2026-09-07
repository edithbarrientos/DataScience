# -*- coding: utf-8 -*-
"""
Module: src.core.telemetry
Author: Edith Barrientos <edithbaga@github.com>
"""

import logging
from prometheus_client import Counter, Histogram

logger = logging.getLogger("inference_engine.core.telemetry")

# Inicialización explícita de métricas globales de Prometheus
REQUEST_COUNTER = Counter(
    "ml_api_requests_total", 
    "Total acumulado de peticiones recibidas por el motor de inferencia.", 
    ["endpoint", "version", "status"]
)

INFERENCE_LATENCY = Histogram(
    "ml_api_inference_duration_seconds", 
    "Tiempo de ejecución invertido por el core matemático.", 
    ["model_version"],
    buckets=(0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0)
)