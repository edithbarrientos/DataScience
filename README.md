# 🚀 Inference Engine: Enterprise MLOps Production Architecture

Inference Engine es una infraestructura de microservicios elástica, desacoplada y de alta disponibilidad diseñada para servir modelos de Ciencia de Datos y Machine Learning en producción a gran escala dentro de Kubernetes.

Este motor implementa un enfoque de **Contratos de Datos Dinámicos (Dynamic Data Contracts)**, permitiendo que la misma API atienda múltiples tipos y versiones de algoritmos de optimización o regresión lineal de manera intercambiable sin requerir despliegues adicionales.

---

## 🗺️ Arquitectura Global de Vanguardia

La infraestructura está diseñada bajo el estándar corporativo End-to-End MLOps, desacoplando completamente las capas de frontera de red, validación lógica, almacenamiento y reentrenamiento automatizado.

<div style="overflow-x: auto;">
<pre>
===================================================================================================================
 ARQUITECTURA MLOps DE VANGUARDIA: END-TO-END INFERENCE ENGINE & AUTOMATED RE-TRAINING LOOP
===================================================================================================================

  [ 1. INGRESO ]          [ CLIENTES / CURL ] ────► HTTP POST (Payload con Contrato de Datos)
                                   │
                                   ▼
  [ 2. GATEWAY ]     ┌────────────────────────────────────────────────────────────────────────┐
                     │ ⚡ APACHE APISIX API GATEWAY (Frontera de Control e Inferencia)        │
                     ├────────────────────────────────────────────────────────────────────────┤
                     │ • Rate Limiting & Auth  • Ruteo Dinámico según 'model_version'         │
                     └────────────────────────┬───────────────────────────────────────────────┘
                                              │
                                              ▼ (Distribución Elástica de Tráfico)
  [ 3. INFERENCIA ]  ┌────────────────────────────────────────┬───────────────────────────────────────┐
                     │ 📦 POD 01 (FastAPI Engine)             │ 📦 POD 02 (FastAPI Engine)            │
                     ├────────────────────────────────────────┼───────────────────────────────────────┤
                     │ • Validación Pydantic V2               │ • Validación Pydantic V2              │
                     │ • Extracción de Matrices NumPy         │ • Extracción de Matrices NumPy        │
                     └───────────────────┬────────────────────┘ Walidación de Datos)  └───┬───────────────────┘
                                         │                                            │
                                         ▼ (Lazy Loading en RAM)                      ▼
  [ 4. REPOSITORIO ] ┌────────────────────────────────────────────────────────────────────────┐
  [   DE MODELOS   ] │ 📁 K8S PERSISTENT VOLUME POOL (Model Registry / Shared Mesh)           │
                     │  • /models/regresion_lineal/v3.0.0/model.pkl                           │
                     └───────────────────────────────────▲────────────────────────────────────┘
                                                         │
                                                         │ (Inyección de nuevo .pkl optimizado)
                                                         │
  [ 5. GOBERNANZA ]  ┌───────────────────────────────────┴────────────────────────────────────┐
  [ Y AUTOMACIÓN ]   │ ⚙️ APACHE AIRFLOW / ARGO WORKFLOWS (Pipeline de Reentrenamiento)       │
                     ├────────────────────────────────────────────────────────────────────────┤
                     │ • Monitorea 'Data Drift'  • Dispara entrenamiento continuo si falla R² │
                     └───────────────────────────────────▲────────────────────────────────────┘
                                                         │
                                                         │ (Consume Datos Históricos Limpios)
                                                         │
  [ 6. DATOS CORE ]  ┌───────────────────────────────────┴────────────────────────────────────┐
                     │ 🌐 FEAST / APACHE HOP FEATURE STORE (Almacén de Características)       │
                     │  • Offline Layer: Parquet/S3 (Para entrenamiento masivo)               │
                     │  • Online Layer: Redis (Para consultas de la API en milisegundos)      │
                     └────────────────────────────────────────────────────────────────────────┘
</pre>
</div>

---

## 📁 Estructura del Proyecto (Clean Architecture & GitOps)

El repositorio sigue estrictamente los principios de diseño de software limpio y GitOps, separando las configuraciones de red, las tuberías de orquestación y el código fuente matemático del modelo:

<div style="overflow-x: auto;">
<pre>
inference-engine/
│
├── .github/                         # CAPA DE CI/CD AUTOMATIZADO
│   └── workflows/
│       ├── test-pipeline.yaml       # Validación de código y contratos (Pytest + Pydantic)
│       └── build-deploy.yaml        # Compilación de la API y subida automática a Docker Hub
│
├── config/                          # CONFIGURACIONES GLOBALES DE ENTORNO
│   ├── .env.production              # Variables de producción para contenedores
│   └── apisix_routes.json           # Configuración de contratos y ruteo dinámico en Apache APISIX
│
├── k8s_infra/                       # CAPA DE INFRAESTRUCTURA COMO CÓDIGO (GitOps)
│   ├── 01-storage-mesh.yaml         # PersistentVolume y PersistentVolumeClaim (Model Registry Mesh)
│   ├── 02-inference-deployment.yaml # Despliegue elástico de Pods de FastAPI con límites de CPU/RAM
│   ├── 03-inference-service.yaml    # Service NodePort/LoadBalancer que expone el puerto 9000
│   └── 04-hpa.yaml                  # Horizontal Pod Autoscaler (Autoescala si la CPU supera el 75%)
│
├── pipelines/                       # CAPA DE AUTOMATIZACIÓN DE DATOS (MLOps Pipeline)
│   ├── dags/
│   │   └── retrain_linear_model.py  # Orquestador Apache Airflow para reentrenamiento continuo
│   └── features/
│       └── feature_store_def.py     # Definición lógica de contratos de variables en Feast/Apache Hop
│
├── src/                             # CÓDIGO FUENTE DE INFERENCIA (Clean Architecture)
│   ├── __init__.py                  # Inicializador del módulo principal
│   ├── main.py                      # Punto de entrada asíncrono ASGI de FastAPI
│   │
│   ├── api/                         # Capa de Presentación (Controladores HTTP)
│   │   ├── __init__.py
│   │   ├── contracts.py             # Modelos estrictos de Pydantic V2 (Data Contracts)
│   │   └── endpoints.py             # Manejador de rutas (/predict, /health, /metrics)
│   │
│   ├── core/                        # Capa de Lógica de Negocio (Machine Learning Compute)
│   │   ├── __init__.py
│   │   ├── cache_manager.py         # Administrador de caché en RAM para modelos (Lazy Loading)
│   │   └── telemetry.py             # Inicialización y definición de métricas nativas de Prometheus
│   │
│   └── tests/                       # Capa de Control de Calidad e Integración
│       ├── __init__.py
│       ├── test_contracts.py        # Pruebas unitarias de esquemas JSON entrantes
│       └── test_inference.py        # Pruebas de velocidad de carga matemática del modelo
│
├── Dockerfile                       # Instrucciones de empaquetado optimizado (Multi-stage build)
├── requirements.txt                 # Dependencias rígidas de producción bloqueadas por versión
└── .gitignore                       # Filtro estricto para evitar subir basura o modelos locales (.pkl)
</pre>
</div>
