
disease_db = {
    "influenza": ["fever", "cough", "sore throat", "runny nose", "muscle aches"],
    "covid-19": ["fever", "cough", "shortness of breath", "loss of taste or smell", "fatigue"],
    "malaria": ["fever", "chills", "sweats", "headaches", "nausea"]
}

def find_possible_diseases():
    symptoms = input(
        "Enter symptoms (comma separated): "
    )

    symptoms_list = [
        symptom.strip().lower()
        for symptom in symptoms.split(",")
    ]

    scores = {}

    for disease, disease_symptoms in disease_db.items():

        matches = 0

        for symptom in symptoms_list:
            if symptom in disease_symptoms:
                matches += 1

        scores[disease] = matches

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nPossible conditions:\n")

    for disease, score in ranked:
        print(f"{disease}: {score} matching symptoms")

find_possible_diseases()