# auto_test.py

import os
from ocr_module import extract_text_from_image
from ner_module import extract_medical_entities
import utils

# Directory with sample prescriptions
sample_dir = 'data/'
sample_files = [f for f in os.listdir(sample_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

if not sample_files:
    print("No sample prescription images found in the 'data/' folder.")
else:
    for file in sample_files:
        print(f"\nProcessing: {file}")
        image_path = os.path.join(sample_dir, file)
        
        # Step 1: OCR
        text = extract_text_from_image(image_path)
        print("Extracted Text:")
        print(text)
        
        # Step 2: Clean text
        cleaned_text = utils.clean_text(text)
        
        # Step 3: NER extraction
        entities = extract_medical_entities(cleaned_text)
        print("\nExtracted Medical Entities:")
        for label, items in entities.items():
            print(f"{label}: {', '.join(items) if items else 'None'}")
