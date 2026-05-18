# Control-de-Accesso-con-Reconocimiento-Facial-Basada-en-IA

# Sistema de Control de Acceso con Reconocimiento Facial Basado en IA

Proyecto desarrollado en Python utilizando OpenCV y técnicas clásicas de reconocimiento facial mediante EigenFaces para implementar un sistema básico de control de acceso basado en reconocimiento facial en tiempo real.

---

# Descripción General

Este proyecto implementa un flujo completo de reconocimiento facial compuesto por tres etapas:

1. Captura de imágenes faciales para construir el dataset.
2. Entrenamiento del modelo de reconocimiento facial.
3. Reconocimiento facial en tiempo real mediante webcam.

El sistema utiliza:

- OpenCV
- Haar Cascades
- EigenFaceRecognizer
- Python
- Computer Vision

---

# Tecnologías Utilizadas

- Python 3.10
- OpenCV
- NumPy
- Imutils
- Git
- Git LFS
- UV Package Manager
- WSL Ubuntu 22.04
- Visual Studio Code

---

# Estructura del Proyecto

```text
Control-Acceso-Facial-IA/
│
├── src/
│   ├── 01_face_capture.py
│   ├── 02_train_face_recognizer.py
│   └── 03_face_recognizer.py
│
├── models/
│   └── modeloEigenFace.xml
│
├── data/
│   └── .gitkeep
│
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .gitattributes
└── README.md
```

---

# Flujo de Funcionamiento

## 1. Captura de Rostros

El archivo:

```text
01_face_capture.py
```

permite capturar múltiples imágenes faciales desde la webcam para generar el dataset de entrenamiento.

### Funcionalidades

- Detecta rostros usando Haar Cascades.
- Extrae la región facial.
- Redimensiona cada rostro a 150x150 píxeles.
- Guarda automáticamente las imágenes capturadas.
- Construye un dataset organizado por persona.

### Configuración

Modificar:

```python
personName = 'NombrePersonaX'
```

por el nombre real de la persona.

---

## 2. Entrenamiento del Modelo

El archivo:

```text
02_train_face_recognizer.py
```

entrena el modelo EigenFaces utilizando las imágenes almacenadas en el dataset.

### Funcionalidades

- Lee todas las carpetas de personas.
- Convierte las imágenes a escala de grises.
- Genera etiquetas automáticamente.
- Entrena el modelo facial.
- Exporta el modelo entrenado a:

```text
modeloEigenFace.xml
```

---

## 3. Reconocimiento Facial en Tiempo Real

El archivo:

```text
03_face_recognizer.py
```

ejecuta el reconocimiento facial usando la webcam en tiempo real.

### Funcionalidades

- Detecta rostros en vivo.
- Predice identidad facial.
- Compara el rostro detectado contra el modelo entrenado.
- Muestra:
  - Nombre de la persona reconocida.
  - Etiqueta "Desconocido" si no coincide.

---

# Instalación del Proyecto

## Clonar el repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
```

---

# Configuración del Entorno

## Crear entorno virtual con UV

```bash
uv venv
```

Activar entorno:

```bash
source .venv/bin/activate
```

---

# Instalar Dependencias

```bash
uv sync
```

o manualmente:

```bash
uv add opencv-python
uv add opencv-contrib-python
uv add numpy
uv add imutils
```

---

# Dependencias del Sistema (Ubuntu / WSL)

```bash
sudo apt update

sudo apt install -y \
build-essential \
cmake \
python3-dev
```

---

# Ejecución del Proyecto

## 1. Capturar Dataset

```bash
python src/01_face_capture.py
```

---

## 2. Entrenar Modelo

```bash
python src/02_train_face_recognizer.py
```

---

## 3. Ejecutar Reconocimiento Facial

```bash
python src/03_face_recognizer.py
```

---

# Funcionamiento del Reconocimiento

El sistema utiliza:

## Haar Cascades

Para detección de rostros.

## EigenFaces

Para reconocimiento facial clásico basado en reducción de dimensionalidad y análisis de componentes principales (PCA).

---

# Dataset

Las imágenes capturadas se almacenan en:

```text
data/
```

Cada persona debe tener su propia carpeta:

```text
data/
├── Carlos/
├── Maria/
└── Pedro/
```

---

# Requisitos de Hardware

- Webcam
- Procesador básico moderno
- Sistema Linux / WSL recomendado

---

# Posibles Mejoras Futuras

- Integración con bases de datos.
- Sistema de autenticación.
- Interfaz gráfica.
- Soporte para cámaras IP.
- Deep Learning con FaceNet o Dlib.
- Registro de accesos.
- Integración con Raspberry Pi.
- Reconocimiento multiusuario.
- Soporte GPU/CUDA.

---

# Problemas Conocidos y Observaciones Técnicas

## 1. Rutas Absolutas

Actualmente el proyecto utiliza rutas absolutas como:

```python
dataPath = '/home/yorch/...'
```

Esto puede causar errores en otros sistemas.

### Recomendación

Usar rutas relativas:

```python
dataPath = './data'
```

---

## 2. Inconsistencia de Carpetas

El código usa:

```python
DATA/
```

pero la estructura recomendada es:

```python
data/
```

Linux distingue mayúsculas y minúsculas.

---

## 3. Posible Error con OpenCV

El reconocimiento facial requiere:

```python
opencv-contrib-python
```

NO solamente:

```python
opencv-python
```

Porque:

```python
cv2.face.EigenFaceRecognizer_create()
```

pertenece a OpenCV Contrib.

---

## 4. Posible Problema con Webcam en WSL

En algunos entornos WSL la webcam puede no detectarse correctamente.

Si ocurre:

```python
cap = cv2.VideoCapture(0)
```

probar:

```python
cap = cv2.VideoCapture(1)
```

---

## 5. Umbral de Reconocimiento

El parámetro:

```python
if result[1] < 5700:
```

puede necesitar ajustes dependiendo de:

- iluminación
- calidad de cámara
- cantidad de imágenes
- tamaño del dataset

---

## 6. Nombre del Archivo

Renombrar:

```text
train_face_recognizer
```

a:

```text
02_train_face_recognizer.py
```

para mantener consistencia.

---

# Seguridad y Privacidad

Este proyecto es únicamente educativo y experimental.

El reconocimiento facial puede implicar:

- riesgos de privacidad,
- sesgos algorítmicos,
- falsos positivos,
- problemas éticos.

No utilizar en entornos críticos sin validación adicional.

---

# Autor

Proyecto desarrollado con fines educativos y de investigación en Computer Vision y Ciberseguridad.

---

# Licencia

MIT License
