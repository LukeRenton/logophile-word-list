import numpy as np
import matplotlib.pyplot as plt

def get_beta_list():
  word_list = set()
  with open("Superior words.txt", encoding="utf8") as file:
    # reading each line   
      for line in file:
    
          # reading each word       
          for word in line.split():
              if (word.isupper() and len(word) > 4 and word.isalpha()):
                word_list.add(word.lower())
                if(not word.isalpha()):
                  print(word)
                
  with open("instagram_words.txt", "r") as file:
    for word in file:
      word_list.add(word.lower().strip("\n"))
  
  print(word_list)
  print(len(word_list))
  with open("WordListBeta.txt", "w") as file:
    for word in word_list:
      file.write(word + "\n")
      
def clean_beta_list(): 
  
  with open("WordListBeta (1).txt", "r") as infile, open("FinalBeta.txt","w") as outfile:
    for word in infile:
      if (len(word.split()) == 1):
        outfile.write(word.lower())
      
def clean_frequency_list():
  with open("FrequencyList.txt", "r") as infile, open("CleanedList.txt", "w") as outfile:
    for line in infile:
      pair = line.split()
      if (pair[1].isalpha()):
        outfile.write(pair[0] + " " + pair[1] + "\n")
      
def set_frequency_list():
  beta_list = []
  frequency_list = []
  with open("FinalBeta.txt", "r") as file:
    for line in file:
      beta_list.append(line.strip("\n"))
      
  with open("CleanedList.txt", "r") as infile, open("BetaListWithFrequencies.txt","w") as outfile:
    for line in infile:
      pair = line.split()
      if (pair[1] in beta_list):
        word = pair[0] + " " + pair[1]
        frequency_list.append(word)
        outfile.write(word + "\n")
  print(frequency_list)
  
  
  
def show_frequency_results():
  word_list = []
  with open("BetaListWithFrequencies.txt") as file:
    for line in file:
      word_list.append(line.strip("\n"))
  
  # Extract the numerical frequencies
  frequencies = [int(word.split(' ')[0]) for word in word_list]
  quartiles = np.quantile(frequencies, [0,0.25,0.5,0.75,1])      
  lower = quartiles[2]
  upper = quartiles[3]
  words = []
  print(lower)
  print(upper)
  with open("FrequencyList.txt", "r") as infile, open("FilteredList.txt", "w") as outfile:
    for line in infile:
      pair = line.split()
      word = pair[1]
      freq = int(pair[0])
      if (freq <= upper and freq >= lower and len(word) > 4):
        words.append(str(freq) + " " + word + "\n")
        outfile.write(str(freq) + " " + word + "\n")
  print(words)
        
def get_beta_listfq():
  with open("BetaListWithFrequencies.txt","r") as file:
    words = []
    for line in file:
      words.append(line.strip("\n"))
  print(words)
    
#get_beta_list()
#clean_frequency_list()
#clean_beta_list()
#set_frequency_list()
#get_beta_listfq()
show_frequency_results()


    

