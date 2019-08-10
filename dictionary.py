import json
from difflib import get_close_matches
import wikipedia as wk

data = json.load(open("data.json"))

def wikipedia_open(word):
    word = word.strip("wikipedia")
    if "search" in word:
            word = word.strip("search")
            print(wk.search(word))
    elif "summary" in word:
            word = word.strip("summary")
            print(wk.summary(word, sentences = 3))
    else:
            print("Plese Specify action")
            go()

        

def decoder(word):
    a_bool = 'wikipedia' in word
    if a_bool == True:
        wikipedia_open(word)
    else:
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
                decoder(get_close_matches(word, data.keys())[0])
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
    decoder(user_input)
    closer()

go()