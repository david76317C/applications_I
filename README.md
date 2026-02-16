# OCR Pipeline

Pipeline sencillo y efectivo para **Reconocimiento Óptico de Caracteres (OCR)** que procesa imágenes y extrae texto utilizando **EasyOCR** (por defecto) y **Tesseract** (opcional).

Soporta imágenes **PNG, JPG y JPEG**.  
Ideal para facturas, carteles, recibos, libros escaneados, etc.

## Características principales

- Procesamiento por lotes de todas las imágenes en la carpeta `inputs/`
- Dos motores OCR disponibles:
  - **EasyOCR** (predeterminado) → mejor en imágenes con ruido, perspectivas variables, fuentes variadas y texto no alineado
  - **pytesseract** (predeterminado) → mejor en imágenes con ruido, perspectivas variables, fuentes variadas y texto no alineado
- Resultados guardados en carpeta `outputs/` con timestamp y nombre original
- Soporte nativo para **español + inglés** 
- Logging claro para seguimiento y depuración
- Compatible con **Windows** y **macOS** 

## Requisitos

- **Python 3.12** (no compatible con versiones ≥ 3.13 por dependencias de PyTorch)
- pip
- Git (opcional)

## Instalación

### 1. Instalar Python 3.12

**Windows**  
1. Descargar el instalador desde python.org/downloads (selecciona la versión 3.12.x).
2. Ejecutar el instalador y marca la opción "Add Python to PATH".
3. Sigue las instrucciones del instalador.
4. Verifica la instalación abriendo una terminal (cmd o PowerShell) y ejecutando:
```bash
python --version
```
Deberías ver Python 3.12.x.

**macOS**  
Opción recomendada (Homebrew):

```bash
1. Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Instalar Python 3.12
```bash
brew install python@3.12
```
3. Verificar
```bash
python3 --version
```

### 2. Clonar el repositorio (Opcional)
```bash
git clone https://github.com/david76317C/applications_I.git
```

### 3.Crear un entorno virtual 
Para evitar conflictos con otros proyectos.

**Windows** 
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar dependencias
Asegúrarse de tener el archivo requirements.txt en la raíz del proyecto (Se encuentra en la carpeta src). Luego ejecutar:

```bash
pip install --upgrade pip
pip install -r src/requirements.txt
```

## Estructura del proyecto

```text
ocr-pipeline/
│
├── src/                    # Código fuente
│   ├── ocr_pipeline.py     # Script principal
│   ├── inferencia.py       # Funciones de OCR y guardado
│   └── requirements.txt    # Dependencias de Python
│
├── inputs/                 # Carpeta para las imágenes de entrada
│   └── (colocar aquí las imágenes)
│
├── outputs/                # Carpeta donde se guardan los resultados (txt)
│   └── (carpeta de salida)
│
├── README.md               # Este archivo
└── .gitignore              # Archivos ignorados por Git
```

## Instrucciones de uso
### 1. Preparar las imágenes: 
Colocar las imágenes que se desea procesar en la carpeta inputs. Formatos soportados: .png, .jpg, .jpeg.
### 2. Script principal:
Ejecutar

**Windows**
```bash
python src/ocr_pipeline.py
```
**macOS** 
```bash
python3 src/ocr_pipeline.py
```

### 3. Resultados: 
Los archivos de texto generados se guardarán en la carpeta outputs con el nombre nombre_imagen_YYYYMMDD_HHMMSS.txt. Cada archivo contiene la fecha de generación y el texto extraído

## Limitaciones y posibles mejoras
### Limitaciones
- **Velocidad:** EasyOCR esta configurado por defecto para que use sólo CPU, lo hace más lento.
- **Idiomas:** Por defecto se usan español e inglés
### Posibles mejoras
- Añadir soporte para GPU (CUDA) en sistemas compatibles.
- Implementar un sistema de detección de idioma automático.
- Permitir procesamiento en paralelo para múltiples imágenes.
- Agregar una interfaz web simple.

## Autores
- Andrés Felipe Flórez Caro
- Sifred Humberto Mendoza Cáseres
- David Felipe Rodríguez Torres






