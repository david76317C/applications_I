OCR Pipeline
Este proyecto implementa un pipeline de reconocimiento óptico de caracteres (OCR) utilizando EasyOCR y Tesseract. Permite extraer texto de imágenes (PNG, JPG, JPEG) y guardar los resultados en archivos de texto. Está diseñado para ser fácil de usar tanto en Windows como en macOS.

Descripción general
El script principal (ocr_pipeline.py) procesa todas las imágenes contenidas en la carpeta inputs y genera archivos de texto con el texto extraído en la carpeta outputs. Soporta dos motores OCR:

EasyOCR (por defecto): soporta múltiples idiomas y es más robusto.

Tesseract: requiere instalación adicional del programa Tesseract OCR en el sistema.

El proyecto está estructurado en dos módulos:

ocr_pipeline.py: orquesta el flujo de trabajo.

inferencia.py: contiene las funciones de extracción de texto y guardado.

Requisitos del sistema
Python 3.12 (no compatible con versiones superiores debido a dependencias de PyTorch).

pip (gestor de paquetes de Python).

Git (opcional, para clonar el repositorio).

Tesseract OCR (solo si deseas usar el método pytesseract; EasyOCR no lo requiere).

Instalación de Python 3.12
En Windows
Descarga el instalador desde python.org/downloads (selecciona la versión 3.12.x).

Ejecuta el instalador y marca la opción "Add Python to PATH".

Sigue las instrucciones del instalador.

Verifica la instalación abriendo una terminal (cmd o PowerShell) y ejecutando:

bash
python --version
Deberías ver Python 3.12.x.

En macOS
Opción A: Usando el instalador oficial

Descarga el instalador desde python.org/downloads (versión 3.12.x).

Ejecuta el archivo .pkg y sigue las instrucciones.

Verifica la instalación en la Terminal:

bash
python3 --version
Opción B: Usando Homebrew (recomendado)

Instala Homebrew si no lo tienes: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Instala Python 3.12:

bash
brew install python@3.12
Verifica:

bash
python3.12 --version
Instrucciones de instalación
1. Clonar o descargar el repositorio
bash
git clone https://github.com/tu-usuario/ocr-pipeline.git
cd ocr-pipeline
O descarga el ZIP y extrae el contenido.

2. Crear un entorno virtual (recomendado)
Esto evita conflictos con otros proyectos.

En Windows
bash
python -m venv venv
venv\Scripts\activate
En macOS/Linux
bash
python3 -m venv venv
source venv/bin/activate
3. Instalar dependencias
Asegúrate de tener el archivo requirements.txt en la raíz del proyecto. Luego ejecuta:

bash
pip install --upgrade pip
pip install -r requirements.txt
Nota: Si encuentras errores relacionados con torch en macOS con chip Apple Silicon, instala PyTorch específico para CPU:

bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
4. (Opcional) Instalar Tesseract OCR
Solo si piensas usar el método pytesseract.

En Windows
Descarga el instalador desde GitHub UB-Mannheim/tesseract y agrega la carpeta de instalación a la variable de entorno PATH.

En macOS
bash
brew install tesseract
Estructura del repositorio
text
ocr-pipeline/
│
├── src/                       # Código fuente
│   ├── ocr_pipeline.py        # Script principal
│   └── inferencia.py          # Funciones de OCR y guardado
│
├── inputs/                     # Carpeta para las imágenes de entrada
│   └── (coloca aquí tus imágenes)
│
├── outputs/                    # Carpeta donde se guardan los resultados
│   └── (se genera automáticamente)
│
├── requirements.txt            # Dependencias de Python
├── README.md                   # Este archivo
└── .gitignore                  # Archivos ignorados por Git
Instrucciones de uso
Prepara tus imágenes: Coloca las imágenes que deseas procesar en la carpeta inputs. Formatos soportados: .png, .jpg, .jpeg.

Ejecuta el script principal:

bash
python src/ocr_pipeline.py
(En macOS, si python no funciona, usa python3 src/ocr_pipeline.py)

Resultados: Los archivos de texto generados se guardarán en la carpeta outputs con el nombre {nombre_imagen}_{timestamp}.txt. Cada archivo contiene la fecha de generación y el texto extraído.

Personalización del método OCR
Por defecto, el script usa EasyOCR. Si deseas usar Tesseract, edita la línea en ocr_pipeline.py que llama a extract_text y cambia method='easyocr' por method='pytesseract':

python
text = extract_text(img_path, method='pytesseract', languages=['es','en'])
Ejemplo de entrada y salida
Entrada (carpeta inputs)
factura.png

cartel.jpg

Salida (carpeta outputs)
factura_20250215_223045.txt

cartel_20250215_223045.txt

Contenido de ejemplo de un archivo de salida:

text
# Generado en 2025-02-15 22:30:45

Total a pagar: $150.00
Gracias por su compra
Limitaciones y posibles mejoras
Limitaciones
Velocidad: EasyOCR es más lento en CPU que en GPU.

Idiomas: Por defecto se usan español e inglés; puedes cambiar los idiomas en la llamada a extract_text.

Calidad del OCR: Depende de la calidad de la imagen (iluminación, resolución, etc.).

Tesseract: Requiere instalación externa y configuración adicional.

Posibles mejoras
Añadir soporte para GPU (CUDA) en sistemas compatibles.

Implementar un sistema de detección de idioma automático.

Permitir procesamiento en paralelo para múltiples imágenes.

Agregar una interfaz web simple.

Incluir más preprocesamiento de imágenes (mejora de contraste, binarización, etc.).

¡Listo! Con este README cualquier usuario debería poder instalar y ejecutar tu proyecto sin problemas. Si necesitas ajustar algún detalle (como la URL del repositorio o ejemplos más específicos), házmelo saber.
