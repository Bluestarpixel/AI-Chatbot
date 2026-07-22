import re

diseases = [
    "diabetes",
    "asthma",
    "cancer",
    "hypertension"
]

def extract_entities(text):

    entities = []

    for disease in diseases:

        if disease.lower() in text.lower():
            entities.append(disease)

    return entities