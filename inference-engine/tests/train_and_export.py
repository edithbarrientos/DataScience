# -*- coding: utf-8 -*-
"""
Script: train_and_export.py
Author: Edith Barrientos <edithbaga@github.com>
Copyright: (c) 2026 Edith Barrientos - DataScience Architecture Core
License: MIT License
Version: 1.0.0

Description:
    Script de automatización e ingeniería de características (ML Pipeline).
    Genera datos sintéticos, entrena una Regresión Lineal Múltiple con Scikit-Learn
    y exporta el modelo de manera directa al formato matemático seguro y optimizado
    ONNX (.onnx) dentro de las carpetas de gobernanza elásticas.
"""

import os
import numpy as np
from sklearn.linear_model import LinearRegression
from skl2onnx import to_onnx

print("🧪 [PIPELINE] Iniciando entrenamiento avanzado y conversión a ONNX...")

# 1. Generación de datos sintéticos (Metros cuadrados, Habitaciones, Antigüedad)
np.random.seed(42)
X_train = (np.random.rand(500, 3) * 100).astype(np.float32)  # ONNX exige flotantes de 32 bits estrictos

# Ecuación matemática oculta para el set de datos:
y_train = X_train[:, 0] * 300 + X_train[:, 1] * 5000 - X_train[:, 2] * 200

# 2. Ajuste del algoritmo clásico de Regresión Lineal Múltiple
model = LinearRegression()
model.fit(X_train, y_train)
print(f"✅ [MODELO ENTRENADO] Coeficientes calculados en C: {model.coef_}")

# 3. Creación automatizada y tolerante de las carpetas de gobernanza en el disco duro
TARGET_DIR = "./models/v5.0.0"
os.makedirs(TARGET_DIR, exist_ok=True)
FILE_PATH = os.path.join(TARGET_DIR, "model.onnx")

# 4. CONVERSIÓN SUPREMA: Transformamos el grafo de Scikit-Learn al formato Protobuf de ONNX
# Le indicamos un ejemplo inicial (X_train[:1]) para que infiera la forma geométrica de la matriz de entrada
model_onnx = to_onnx(model, X_train[:1])

# 5. Volcado físico del bitstream matemático optimizado en el almacenamiento local
with open(FILE_PATH, "wb") as f:
    f.write(model_onnx.SerializeToString())

print(f"🧠 [ARTEFACTO ONNX EXPORTADO] Grafo matemático guardado exitosamente en: {FILE_PATH}")