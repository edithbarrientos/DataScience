# -*- coding: utf-8 -*-
"""
Module: src.api.contracts
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 3.0.0
Maintainer: Edith Barrientos
Status: Production Grade

Description:
    Capa de Presentación e Ingesta de Datos (Data Contract Layer). Implementa
    el Patrón Fábrica (Factory Pattern) acoplado a Pydantic V2 para generar
    esquemas de validación y documentación matricial (json_schema_extra) 
    de manera 100% paramétrica, dinámica e inyectable en tiempo de ejecución.
"""

import logging
from typing import List, Dict, Any, Type
from pydantic import BaseModel, Field, model_validator

# Inicialización del sistema de trazas para auditoría MLOps
logger = logging.getLogger("inference_engine.contracts")


class ModelMetaContract(BaseModel):
    """
    Contrato estricto para los metadatos de gobernanza del modelo.
    
    Garantiza el ruteo interno y el control de versiones (Model Lineage) 
    dentro del almacenamiento persistente del clúster de Kubernetes.
    """
    model_name: str = Field(
        ..., 
        description="Nombre único del modelo registrado en el Feature Store o Model Registry."
    )
    model_version: str = Field(
        ..., 
        description="Versión semántica del artefacto binario empaquetado (ej: v1.0.0, v3.0.0)."
    )


class BaseInferenceContract(BaseModel):
    """
    Contrato base abstracto para la consistencia y simetría de matrices matemáticas.
    
    Valida las reglas geométricas y estructurales del lote (Batch Payload) 
    en la frontera de red antes de que las colecciones sean enviadas a la CPU/GPU.
    """
    model_meta: ModelMetaContract = Field(
        ..., 
        description="Metadatos de control obligatorios para el ruteo dinámico."
    )
    data: List[Dict[str, float]] = Field(
        ..., 
        description="Lote de registros numéricos genéricos tabulares que representan la matriz X."
    )
    features_names: List[str] = Field(
        ..., 
        description="Lista ordenada que dicta el orden exacto de las variables de entrenamiento."
    )

    @model_validator(mode="after")
    def validate_matrix_consistency(self) -> "BaseInferenceContract":
        """
        Validador Dinámico de Consistencia Matricial.
        
        Inspecciona el lote de datos completo para verificar que sea perfectamente 
        simétrico y que cada fila contenga exactamente las variables declaradas 
        en 'features_names', previniendo fallos por asimetría en arreglos de NumPy.
        
        Raises:
            ValueError: Si el lote está vacío, carece de variables o existen 
                        discrepancias entre las claves y el contrato inyectado.
        """
        if not self.data:
            logger.error("Intento de inferencia abortado: El lote de datos ('data') está vacío.")
            raise ValueError("El lote de datos ('data') no puede estar completamente vacío.")
            
        if not self.features_names:
            logger.error("Intento de inferencia abortado: No se declararon variables guía.")
            raise ValueError("Debe especificar al menos una variable guía en 'features_names'.")

        required_features = set(self.features_names)
        
        # Validación vectorizada por registro para mitigar latencia en payloads masivos
        for index, record in enumerate(self.data):
            record_features = set(record.keys())
            
            # 1. Verificar variables faltantes (Under-injection)
            missing = required_features - record_features
            if missing:
                logger.warning(f"Fallo de contrato estructural en registro [{index}]. Faltan: {missing}")
                raise ValueError(
                    f"Violación de Contrato en registro [{index}]: Faltan variables requeridas: {missing}"
                )
                
            # 2. Verificar variables sobrantes o ruido (Over-injection)
            extra = record_features - required_features
            if extra:
                logger.warning(f"Fallo de contrato estructural en registro [{index}]. Sobran: {extra}")
                raise ValueError(
                    f"Violación de Contrato en registro [{index}]: Se enviaron variables no autorizadas: {extra}"
                )
                
        return self


def create_dynamic_contract(
    model_name: str, 
    model_version: str, 
    features: List[str], 
    example_data: List[Dict[str, float]]
) -> Type[BaseInferenceContract]:
    """
    Fábrica Dinámica de Contratos Parametrizables (Factory Design Pattern).
    
    Toma las variables de configuración del algoritmo actual (inyectadas al arrancar 
    el Pod desde un ConfigMap o API Gateway) y construye un nuevo modelo de Pydantic
    en tiempo de ejecución, sobrescribiendo de forma dinámica el 'json_schema_extra'
    para actualizar automáticamente la documentación interactiva de Swagger UI (/docs).

    Args:
        model_name (str): Nombre del algoritmo o modelo activo.
        model_version (str): Versión del modelo cargada en RAM.
        features (List[str]): Lista ordenada de las columnas del modelo.
        example_data (List[Dict[str, float]]): Datos de ejemplo realistas de producción.

    Returns:
        Type[BaseInferenceContract]: Una nueva clase de Pydantic V2 totalmente configurada
                                     e inyectada lista para usar como validador en las rutas.
    """
    logger.info(f"Instanciando contrato dinámico para {model_name} ({model_version})...")
    
    # Construcción dinámica del payload de ejemplo para inyección documental
    dynamic_example = {
        "model_meta": {
            "model_name": model_name,
            "model_version": model_version
        },
        "data": example_data,
        "features_names": features
    }

    # Declaración de la clase hija extendida inyectando la configuración paramétrica
    class ConfiguredContract(BaseInferenceContract):
        model_config = {
            "json_schema_extra": {
                "example": dynamic_example
            }
        }

    return ConfiguredContract
