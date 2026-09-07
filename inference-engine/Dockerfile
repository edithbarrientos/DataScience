# =================================================================================
# Entorno de Producción de Ultra-Baja Latencia (Clean High-Performance Runtime)
# =================================================================================
FROM python:3.12-slim-bookworm

WORKDIR /app

# Bloqueamos variables de entorno para optimizar el comportamiento de Python en contenedores
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH=/root/.local/bin:$PATH

# Copiamos e instalamos los requerimientos utilizando los binarios precompilados de PIP
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copiamos el código fuente del microservicio respetando el andamiaje elástico
COPY src/ ./src/

# Declaración del punto de montaje elástico para el volumen persistente de grafos ONNX
RUN mkdir -p /mnt/models
ENV MODELS_DIR="/mnt/models"

# Puerto de red expuesto internamente en consonancia con tu Service de Kubernetes
EXPOSE 9000

# PUNTO DE ENTRADA MAESTRO CORREGIDO: Inyectamos el puerto 9000 explícito para Granian
ENTRYPOINT ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "9000", "src.main:app"]
