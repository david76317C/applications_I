import os
import logging
import easyocr
import pytesseract

from PIL      import Image
from datetime import datetime


logger     = logging.getLogger(__name__)
OUTPUT_DIR = "outputs"

def extract_text(image_path,method='easyocr',languages=['es','en']):
    try:
        if (method =='easyocr'):
            reader = easyocr.Reader(languages, gpu=False)
            result = reader.readtext(image_path)
            text = ' '.join([res[1] for res in result if res[2] > 0.5])
        elif (method == 'pytesseract'):
            image = Image.open(image_path)
            custom_config = r'--oem 3 --psm 6 -l spa+eng'
            text = pytesseract.image_to_string(image, config=custom_config)
        else:
            raise ValueError("Método OCR no compatible. Use 'easyocr' o 'pytesseract' ")
        return text.strip()
        
    except Exception as e:
        logger.error(f'La extracción de texto falló para {image_path}: {e}')
        raise RuntimeError(f'La extracción del texto a fallado: {e}')


def save_translation(filename: str, text: str) -> str:
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'{filename}_{timestamp}.txt'
    path = os.path.join(OUTPUT_DIR, output_filename)
    
    with open(path,'w',encoding='utf-8') as f:
        f.write(f"# Generado en {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(text)
    return path
