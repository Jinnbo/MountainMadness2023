import openai
import urllib.request

# Get the api token
with open('token.txt') as f:
    lines = f.readlines()
openai.api_key = lines[1]

# Generate the image

def generateImage(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )

    # Save the image
    url = response["data"][0]["url"]
    urllib.request.urlretrieve(url, "images/1.png")



