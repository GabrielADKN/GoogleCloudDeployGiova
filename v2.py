import openai
import os

# Initialiser l'API de OpenAI avec une clé d'API valide
openai.api_key = "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"

# Question text
question = "comment cultiver l'ananas?"


def repondre_ia(question):
    # Call the OpenAI API to get the answer to the question
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="repond a la question suivante d'une facon claire et conscise avec un maximum de 70 mots : "  + question,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        #stop=["\n"]
        #max_tokens=100,
        #n=1,
        #stop=["\n"],
        #stop=None,
        #temperature=0
    )
    # Extract the generated answers from the API response
    #answer = response.choices[0].text
    #answer = response.choices[0].text.strip()
    return response.choices[0]['text'].strip()


# Display the generated answer
print(repondre_ia(question))
