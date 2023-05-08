
"""
Created on Wed Aug  31 08:35:39 2022

@author: GabrielADKN
"""

import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from recherche_ecrit import recherche_ecrit
from reformateur import reformater

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "AgriBot"

def get_response(sentence):
    sentence = sentence.lower()
    sentence2 = sentence
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.9:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                resultat = random.choice(intent['responses'])
                str(resultat)
        resultat = reformater(resultat)
        return resultat
    else:
        try:
            sentence2 = sentence2.lower()
            resultat = recherche_ecrit(sentence2)
            resultat = reformater(resultat)
            return resultat
        except Exception:
            resultat = "Je n'ai pas compris, veuillez reformuler votre demande ou nous contacter via ce lien : <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a> "
            return resultat


if __name__ == "__main__":
    print("Discutons, entrer (quit) pour quitter")
    while True:
        sentence = input("You: ")
        sentence = sentence.lower()
        if sentence == "quit":
            break
        resp = get_response(sentence)
        print(f"{bot_name}: {resp}")