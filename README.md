# OCR Pipeline

Pipeline sencillo y efectivo para **Reconocimiento Óptico de Caracteres (OCR)** que procesa imágenes y extrae texto utilizando **EasyOCR** (por defecto) y **Tesseract** (opcional).

Soporta imágenes **PNG, JPG y JPEG**.  
Ideal para facturas, carteles, recibos, libros escaneados, etc.

## Características principales

- Procesamiento por lotes de todas las imágenes en la carpeta `inputs/`
- Dos motores OCR disponibles:
  - **EasyOCR** (default)
  - **pytesseract** (Tesseract)
- Resultados guardados automáticamente en `outputs/` con timestamp
- Compatible con **Windows** y **macOS** (incluyendo Apple Silicon)
- Fácil de personalizar (idiomas, motor OCR, etc.)

## Requisitos

- **Python 3.12** (no compatible con versiones ≥ 3.13 por dependencias de PyTorch)
- pip
- Git (opcional)

## Instalación

### 1. Instalar Python 3.12

**Windows**  
1. Descarga el instalador desde python.org/downloads (selecciona la versión 3.12.x).
2. Ejecuta el instalador y marca la opción "Add Python to PATH".
3. Sigue las instrucciones del instalador.
4. Verifica la instalación abriendo una terminal (cmd o PowerShell) y ejecutando:
```bash
python --version

Deberías ver Python 3.12.x.



Descarga desde: https://www.python.org/downloads/release/python-31211/  
→ Marca **"Add Python to PATH"** durante la instalación

**macOS**  
Opción recomendada (Homebrew):

```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python 3.12
brew install python@3.12
