# -*- coding: utf-8 -*-
"""
Module: tests.test_contracts
Author: Edith Barrientos <edithbaga@github.com>
"""

import json
import pytest
from src.api.contracts import create_dynamic_contract


def test_parametric_contract_success():
    """Garantiza que la fábrica apruebe estructuras matriciales simétricas perfectas."""
    print("\n🧪 [TEST INICIADO] Evaluando el comportamiento de payloads válidos...", flush=True)
    
    features = ["metros_cuadrados", "habitaciones", "antiguedad"]
    example = [{"metros_cuadrados": 120.0, "habitaciones": 3.0, "antiguedad": 5.0}]
    
    # 🪐 CREACIÓN DEL CONTRATO DINÁMICO
    DynamicContract = create_dynamic_contract("bienes-raices-test", "v5.0.0", features, example)
    
    # VISUALIZACIÓN EN PANTALLA: Forzamos la impresión del JSON Schema generado por Pydantic
    print("\n📋 [CONTRATO DE GOBERNANZA GENERADO POR PYDANTIC V2]:")
    print(json.dumps(DynamicContract.model_json_schema(), indent=2, ensure_ascii=False), flush=True)
    
    valid_payload = {
        "model_meta": {"model_name": "bienes-raices-test", "model_version": "v5.0.0"},
        "data": [
            {"metros_cuadrados": 85.0, "habitaciones": 2.0, "antiguedad": 10.0},
            {"metros_cuadrados": 150.5, "habitaciones": 4.0, "antiguedad": 2.0}
        ],
        "features_names": features
    }
    
    validated = DynamicContract(**valid_payload)
    
    print("\n🚀 [INFERENCIA EXITOSA] 📊 Matriz perfectamente simétrica. Contrato aprobado.", flush=True)
    assert validated.model_meta.model_name == "bienes-raices-test"
    assert len(validated.data) == 2


def test_parametric_contract_missing_feature():
    """Verifica el bloqueo inmediato de payloads por omisión de columnas."""
    print("\n🧪 [TEST INICIADO] Simulando ataque de datos por omisión de columnas...", flush=True)
    
    features = ["f1", "f2"]
    example = [{"f1": 1.0, "f2": 2.0}]
    
    DynamicContract = create_dynamic_contract("test", "v1", features, example)
    
    corrupt_payload = {
        "model_meta": {"model_name": "test", "model_version": "v1"},
        "data": [
            {"f1": 10.0, "f2": 20.0},
            {"f1": 5.0}  # ── Error: Falta columna f2
        ],
        "features_names": features
    }
    
    with pytest.raises(ValueError, match="Faltan variables"):
        DynamicContract(**corrupt_payload)
        
    print("🛡️ [CONTRATO BLOQUEADO] El escudo de Pydantic detuvo la inyección insuficiente.", flush=True)


def test_parametric_contract_extra_noise_feature():
    """Garantiza el rechazo si el cliente envía variables adicionales intrusas."""
    print("\n🧪 [TEST INICIADO] Simulando inyección de ruido o columnas maliciosas...", flush=True)
    
    features = ["f1"]
    example = [{"f1": 1.0}]
    
    DynamicContract = create_dynamic_contract("test", "v1", features, example)
    
    corrupt_payload = {
        "model_meta": {"model_name": "test", "model_version": "v1"},
        "data": [
            {"f1": 10.0, "ruido_malicioso": 999.9}  # ── Error: Variable intrusa
        ],
        "features_names": features
    }
    
    with pytest.raises(ValueError, match="Se enviaron variables no autorizadas"):
        DynamicContract(**corrupt_payload)
        
    print("⚠️ [COLUMNA RECHAZADA] El sistema interceptó ruido asimétrico y canceló la predicción.", flush=True)
