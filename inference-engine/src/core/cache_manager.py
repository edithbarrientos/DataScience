# -*- coding: utf-8 -*-
"""
Module: src.core.cache_manager
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 2.0.0

Description:
    Administrador de Modelos en RAM (Model Cache Manager). Inicializa sesiones 
    nativas en C++ de ONNX Runtime aplicando optimizaciones de hardware estrictas
    (Thread Tuning) para pulverizar la latencia en entornos de contenedores.
"""

import os
import logging
import onnxruntime as ort
from typing import Dict, Any

logger = logging.getLogger("inference_engine.core.cache_manager")

# Diccionario global que actúa como caché caliente de persistencia en la memoria RAM
MODEL_RAM_CACHE: Dict[str, ort.InferenceSession] = {}
MODELS_BASE_DIR = os.getenv("MODELS_DIR", "./models")


def get_model_from_cache(model_version: str) -> ort.InferenceSession:
    """Carga y mantiene en memoria RAM una sesión de inferencia de ONNX Runtime
    optimizada a nivel de hilos de CPU.
    """
    if model_version in MODEL_RAM_CACHE:
        return MODEL_RAM_CACHE[model_version]
    
    model_path = os.path.join(MODELS_BASE_DIR, model_version, "model.onnx")
    
    logger.info(f"💾 [CACHE MISS] Sesión ONNX '{model_version}' no encontrada en RAM. Cargando grafo...")
    
    if not os.path.exists(model_path):
        error_msg = f"Artefacto ONNX no encontrado en la ruta de infraestructura: {model_path}"
        logger.error(f"🚨 [FILE NOT FOUND] {error_msg}")
        raise FileNotFoundError(error_msg)
        
    try:
        # =================================================================================
        # OPTIMIZACIONES EXTREMAS DE HARDWARE (C++ Native Tuning)
        # =================================================================================
        opts = ort.SessionOptions()
        opts.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
        
        # Forzamos la optimización total del grafo matemático antes de meterlo a la RAM
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        
        # EVITA CONTENCIÓN DE HILOS: Limitamos el paralelismo interno a 1 hilo para 
        # que coincida de forma exacta con los límites elásticos de Kubernetes (limits.cpu)
        opts.intra_op_num_threads = 1
        opts.inter_op_num_threads = 1
        
        # Inicialización de la sesión nativa de ejecución de hardware
        session = ort.InferenceSession(model_path, sess_options=opts, providers=["CPUExecutionProvider"])
        
        MODEL_RAM_CACHE[model_version] = session
        logger.info(f"🧠 [ONNX SESSION WARMED] Grafo '{model_version}' optimizado y cargado en memoria RAM.")
        
        return session
        
    except Exception as onnx_err:
        error_msg = f"Error crítico al levantar la sesión de ONNX Runtime: {str(onnx_err)}"
        logger.error(f"🚨 [ONNX RUNTIME ERROR] {error_msg}")
        raise RuntimeError(error_msg)
