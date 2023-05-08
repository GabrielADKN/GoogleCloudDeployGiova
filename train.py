# -*- coding: utf-8 -*-

"""
Created on Mon Aug  29 08:35:39 2022

@author: GabrielADKN
"""

import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
# boucler chaque phrase dans nos modèles d’intentions
for intent in intents['intents']:
    tag = intent['tag']
    # ajouter à la liste des tags
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokeniser chaque mot de la phrase
        w = tokenize(pattern)
        # ajouter à notre liste de mots
        all_words.extend(w)
        # ajouter à la paire xy
        xy.append((w, tag))

# stemmer et mettre en minuscule chaque mot
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# supprimer les doublons et trier
all_words = sorted(set(all_words))
all_words = all_words
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

# créer des données d’entraînement
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # X: sac de mots pour chaque pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss n’a besoin que d’étiquettes de classe, pas d’étiquettes à chaud
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-paramètres
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # prendre en charge l’indexation de telle sorte que le jeu de données[i] puisse être utilisé pour obtenir le i-ème échantillon
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # nous pouvons appeler len(dataset) pour renvoyer la taille
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Perte et optimisation
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Entraîner le modèle
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # Passe avant
        outputs = model(words)
        # si y serait un one-hot, nous devons appliquer
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)

        # Rétrograder et optimiser
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

# print(f'training complete. file saved to {FILE}')

# s = "élévé"
# print(s)