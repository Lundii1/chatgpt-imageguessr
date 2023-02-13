import os
import time

import openai
import random
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

openai.api_key = ""
#Game
score = 0
dictionnary = ["Apple","Orange","France","Robot","Destruction","Pain","Anguish","Hello","World","Myth","Thor","Pharaoh","Video","Fortnite","American","Psycho","Scary","Maya","Atlantis","Cthulhu","Spain","Portugal","Wrench","Hammer","Keyboard","Mouse","Headset","Eyes","Happy","Music"]
usedPrompts = []
while score != -1:
    print("Loading...")
    PROMPT = dictionnary[random.randint(0, len(dictionnary) - 1)]
    while PROMPT in usedPrompts:
        PROMPT = dictionnary[random.randint(0, len(dictionnary) - 1)]
    usedPrompts.append(PROMPT)
    response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256"
    )
    print(response["data"][0]["url"])
# Retrieve the image
    if(os.path.exists(os.getcwd() + "/images") == False ):
        os.mkdir(os.getcwd() + "/images")
    urllib.request.urlretrieve(response["data"][0]["url"], "images/image.jpg")
    print("Try to guess the prompt that was given to the AI")
    image = Image.open("images/image.jpg", "r")
    convertedImage = "images/image.bmp"
    image.save(convertedImage)
    plt.imshow(image)
    plt.ion()
    plt.pause(0.001)
    plt.show()
    plt.pause(0.001)
    guess = input()
    plt.close()
    if (guess.lower() == PROMPT.lower()):
        if (len(usedPrompts) == len(dictionnary)):
            print("Congrats, you somehow managed to beat the game. Here, have this 🎂")
            break
        print("Congrats!")
        score +=1
        print("Your current score is: " + str(score))
    else:
        print("Wrong answer, the prompt was: " + PROMPT)
        score = -1
restart = input("Do you want to play again?")
if(restart.lower() == "yes"):
    os.system("program.py")