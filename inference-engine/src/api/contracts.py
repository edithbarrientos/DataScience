# -*- coding: utf-8 -*-
"""
Module: src.api.contracts
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 3.5.0
Maintainer: Edith Barrientos
Status: Production Grade / Pydantic Namespace Patched

Description:
    Capa de Ingesta y Contratos de Datos (Data Contract Layer).
    Implementa el Patrón Fábrica acoplado a Pydantic V2 e inyecta la anulación
    de espacios de nombres protegidos para permitir el uso corporativo de 
    los metadatos de gobernanza MLOps (model_name, model_version).
"""

import logging
from typing import List, Dict, Type, Any
from pydantic import BaseModel, Field, model_validator

# Inicialización del sistema de trazas para auditoría MLOps
logger = logging.getLogger("inference_engine.contracts")


class ModelMetaContract(BaseModel):
    """Contrato estricto para los metadatos de gobernanza del modelo."""
    # 🪐 ESCUDO MLOPS: Desactiva la protección de palabras 'model_' exclusiva de Pydantic V2
    model_config = {"protected_namespaces": ()}
    
    model_name: str = Field(..., description="Nombre único del modelo registrado.")
    model_version: str = Field(..., description="Versión semántica del artefacto binario.")


class BaseInferenceContract(BaseModel):
    """Contrato base abstracto para la consistencia y simetría de matrices matemáticas."""
    model_config = {"protected_namespaces": ()}
    
    model_meta: ModelMetaContract = Field(..., description="Metadatos de control obligatorios.")
    data: List[Dict[str, float]] = Field(..., description="Lote de registros numéricos genéricos.")
    features_names: List[str] = Field(..., description="Lista ordenada que dicta el orden de variables.")

    @model_validator(mode="after")
    def validate_matrix_consistency(self) -> Any:
        """Valida dinámicamente que el lote de datos sea simétrico antes de ir a CPU."""
        if not self.data:
            raise ValueError("El lote de datos ('data') no puede estar completamente vacío.")
            
        if not self.features_names:
            raise ValueError("Debe especificar al menos una variable guía en 'features_names'.")

        required_features = set(self.features_names)
        
        for index, record in enumerate(self.data):
            record_features = set(record.keys())
            
            missing = required_features - record_features
            if missing:
                raise ValueError(f"Violación de Contrato en registro [{index}]: Faltan variables: {missing}")
                
            extra = record_features - required_features
            if extra:
                raise ValueError(f"Violación de Contrato en registro [{index}]: Se enviaron variables no autorizadas: {extra}")
                
        return self


def create_dynamic_contract(
    model_name: str, 
    model_version: str, 
    features: List[str], 
    example_data: List[Dict[str, float]]
) -> Type[BaseInferenceContract]:
    """Fábrica Dinámica de Contratos Parametrizables (Factory Design Pattern)."""
    
    dynamic_example = {
        "model_meta": {
            "model_name": model_name,
            "model_version": model_version
        },
        "data": example_data,
        "features_names": features
    }

    class ConfiguredContract(BaseInferenceContract):
        model_config = {
            "json_schema_extra": {
                "example": dynamic_example
            },
            "protected_namespaces": () # Parche también para la clase de la fábrica
        }

    return ConfiguredContract
