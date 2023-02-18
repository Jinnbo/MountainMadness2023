import os
import openai
import requests

openai.organization = "org-CwEqJy6peUJwJURd46VnFBPF"
openai.api_key = "API-KEY"


def emojiTrans(input):
    texts = openai.Edit.create(model="text-davinci-edit-001",
                               input=input,
                               instruction="Translate the text to emojis")
    return texts


def generatePhrase():
    phrase = openai.Completion.create(model="text-davinci-003",
                                      prompt="Generate a simple random 2-5 word phrase",
                                      temperature=0.6,
                                      max_tokens=40,
                                      top_p=1,
                                      frequency_penalty=1,
                                      presence_penalty=1
                                      )
    return phrase


def parseJSON(jsonFile):
    return ((jsonFile.choices)[0].text).strip()[1:-1]
