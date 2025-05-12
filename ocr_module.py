import easyocr

def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path, detail=0)
    extracted_text = ' '.join(results)
    return extracted_text
