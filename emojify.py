import os
import openai
import requests


def emojiTrans():
    openai.organization = "org-CwEqJy6peUJwJURd46VnFBPF"
    openai.api_key = "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"
    texts = openai.Edit.create(model="text-davinci-edit-001",
                               input="Hello World",
                               instruction="Translate the text to emojis")
    return texts
