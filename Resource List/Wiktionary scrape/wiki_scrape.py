import requests
import sys
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
URL = "https://simple.wiktionary.org/wiki/Wiktionary:Academic_word_list"
defintion_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
print("Trying to get data from: " + URL)
page = requests.get(URL)
if (page.status_code == 200):
  print("Successfully retrieved webpage data now extracting the desired words")
  soup = BeautifulSoup(page.content, "html.parser")
  word_links = soup.find_all('a')
  

  #refine the list
  def refine_list(words, start, finish):
    return words[words.index(start):words.index(finish) + 1]

  words = refine_list([link.text for link in word_links], 'sector', 'collapse')
  
  print("All words have been successfully extracted")
  options = "\nPlease select an option below (i.e. if you want to display the list enter in the number 1): \n\n1. Display the original word list \n2. Remove a word from the word list \n3. Remove words containing a certain character \n4. Get a words definition \n5. Get fast defintion \nAnything else. Exit \n\nEnter your option here: " 
  def remove_words_with_character(words, regex):
    for word in words:
      if (word.find(regex) != -1):
        words.remove(word)
        print("We removed word: " + word + " from the word list")
    print("New word list: ")    
    return words 

  def remove_word(words, remove_word):
    words.remove(remove_word)
    return words
  
  while((answer := input(options)) != "5"):
    if (answer == "1"):
      print("Here is the word list:")
      print(words)
    elif (answer == "2"):
      remove = input("Enter the word you would like to remove: ")
      print(remove_word(words, remove))
    elif (answer == "3"):
      remove_character = input("Enter the character you would like to remove: ")
      print("New word list: ")
      print(remove_words_with_character(words, remove_character))
    elif (answer == "4"):
      word_to_get = input("Enter the word to get the definition for: ")
      defintion_page = requests.get(defintion_url + word_to_get)
      print(defintion_page.content)
    elif (answer == "5"):
      print("wasuuip")
      word_to_get = input("Enter the word to get the definition for: ") 
      print("wasuuip")
      syns = wordnet.synsets(word_to_get)
      print("wasuuip")
      print(syns[0].definition())
    else:
      word_to_get = input("Enter the word to get the definition for: ") 
      syns = wordnet.synsets(word_to_get)
      print(syns[0].definition())
    
  with open("word_list.txt", "w") as f:
    for word in words:
      f.write(word + " ")
else:
  print("Failed to retrieve webpage data. The url may be incorrect or you have no internet connection.")
  