import os
import logging
from inferencia import extract_text, save_translation

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

IMAGES_DIR = "inputs"
OUTPUT_DIR = "outputs"

def main():
    if not os.path.exists(IMAGES_DIR):
        logger.error(f'Directorio {IMAGES_DIR} not found')
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Filtrar imágenes soportadas
    image_files = [
        f for f in os.listdir(IMAGES_DIR) 
        if f.lower().endswith((".png",".jpg",".jpeg"))
                   ]
    if not image_files:
        logger.warning(f'No se encontraron archivos de imagen en {IMAGES_DIR}')
        return

    logger.info(f'Se encontrarón {len(image_files)} imágenes para procesar ')

    for img_file in image_files:
        img_path = os.path.join(IMAGES_DIR, img_file)
        try:
            logger.info(f"Procesando {img_file}...")
            
            # 1️⃣ Guardar resultado
            text = extract_text(img_path,method='easyocr',languages=['es','en'])
            if not text.strip():
                logger.warning(f'No se ha extraído ningún texto de {img_file}')
                continue

            # 2️⃣ Guardar resultado
            output_path = save_translation(img_file.split(".")[0],text)
            logger.info(f"Guardar texto: {output_path}")

        except Exception as e:
            logger.error(f"Fallo para procesar {img_file}: {e}")
            continue

    logger.info("Procesamiento completado")

if __name__ == "__main__":
    main()
