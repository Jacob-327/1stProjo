import random

# Symptom to disease mapping
disease_database = {
    "fever": "You might have the flu or an infection. Stay hydrated and consider seeing a doctor if symptoms persist.",
    "cough": "It could be a common cold, flu, or even allergies. If severe, consult a doctor.",
    "headache": "This could be due to stress, dehydration, or migraines. Rest and drink water.",
    "stomach pain": "You might have indigestion, food poisoning, or an ulcer. Monitor your diet and consult a doctor if needed.",
    "default": "I'm not sure about that symptom. Please consult a medical professional."
}

# Function to diagnose disease
def diagnose(symptom):
    symptom = symptom.lower()
    return disease_database.get(symptom, disease_database["default"])

# Main chatbot loop
def chatbot():
    print("Disease Diagnosis Chatbot: Hello! Describe your symptom or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Stay healthy!")
            break
        response = diagnose(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
