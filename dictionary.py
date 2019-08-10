import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def describer(word):
    word = word.lower()
    if word in data:
        print(data[word])
    elif word.title() in data:
        print(data[word.title()])
    elif word.upper() in data: #in case user enters words like USA or NATO
        print(data[word.upper()])
    elif len(get_close_matches(word, data.keys())) >0:
        question = ("Word not found, did you mean %s?" %get_close_matches(word, data.keys())[0])
        corrector = input(question)
        corrector = corrector.lower()
        corrector = corrector.strip(" ")
        if corrector == "y":
            describer(get_close_matches(word, data.keys())[0])
        elif corrector == "n":
            print("Type again please")
            go()
        else:
            print("answer invalid")

    else:
        print("Word doesn't exist, please check and retry")
        go()

def closer():
    decision = input("\nContinue? Press Y for yes and N for no:")
    decision = decision.lower()
    decision = decision.strip(" ")
    if decision == "y":
        go()
    elif decision == "n":
        print("Goodbye")
    else:
        print("answer invalid")
        closer()

def go():
    user_input = input("word:")
    describer(user_input)
    closer()

go()