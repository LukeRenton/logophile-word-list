import requests
import os
import time
from nltk.corpus import wordnet
defintion_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
os.chdir("Resource List\Defintions scrape")

def combine_lists():
    word_list = set()

    with open("BackupWords.txt", "r") as infile1, open("FinalAlpha.txt", "r") as infile2:
        for line in infile1:
            word_list.add(line.strip("\n"))
        for line in infile2:
            word_list.add(line.strip("\n"))
    with open("words.txt", "w") as outfile:
        for word in word_list:
            outfile.write(word + "\n")
    print("done")

def get_defintion(word_to_get):
    syns = wordnet.synsets(word_to_get)
    if (len(syns) == 0):
        return None
    defintions = []
    # word_to_get +=" " + syns[0].definition()
    for s in syns:
        defintions.append(s.definition())
    return defintions

def get_slower_defintion(word_to_get):
    defintion_page = requests.get(defintion_url + word_to_get)
    if (defintion_page.status_code == 200):
        defintion = defintion_page.json()[0]["meanings"][0]["definitions"][0]["definition"]
        return [defintion]
    else:
        return None

def retrieve_words():
    word_list = []
    with open("words.txt", "r") as file:
        for line in file:
            word_list.append(line.strip("\n"))
    return word_list

def retrieve_defitions():
    words = retrieve_words()
    words_with_defintions = {}
    for word in words:
        definition = get_defintion(word)
        if (definition != None):
            words_with_defintions[word] = definition
        else:
            defintion = get_slower_defintion(word)
            if (defintion != None):
                words_with_defintions[word] = defintion         

    with open("defintions.txt", "w", encoding="utf8") as file:
        for word in words_with_defintions:
            file.write(word + "\n====================\n")
            counter = 0
            for defintion in words_with_defintions[word]:
                counter += 1
                file.write(str(counter) + ". " + defintion + "\n")
            file.write("\n")

retrieve_defitions()