import spacy

# Load pretrained Med7 model (first run will auto-download)
def load_med7_model():
    nlp = spacy.load("en_core_med7_lg")
    return nlp

def extract_medical_entities(text, nlp):
    doc = nlp(text)
    extracted = {
        "DRUG": [],
        "DOSAGE": [],
        "FREQ": [],
        "ROUTE": [],
        "DURATION": []
    }
    for ent in doc.ents:
        if ent.label_ in extracted:
            extracted[ent.label_].append(ent.text)
    return extracted
