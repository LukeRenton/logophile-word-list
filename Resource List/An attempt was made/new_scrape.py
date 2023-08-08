from nltk.stem import WordNetLemmatizer 
from better_profanity import profanity

def valid_word(derived_word):
  return derived_word.isalpha() and len(derived_word) > 4
    
# fwords = []
# h = True
# with open("FrequencyList.txt", "r") as infile:
#   for line in infile:
#     word=line.split()
#     if (valid_word(word[1])):
#       fwords.append(word[0] + " " + word[1]) 
#       if (h and word[1] == "calistho"):
#         print("hello")
#         h = False

# def clean_up_derived(derived_words):
#   words = []
#   lemmatizer = WordNetLemmatizer()
#   root_words = set()

#   for word in derived_words:
#       root_word = lemmatizer.lemmatize(word)
#       root_words.add(root_word)
#   words = list(root_words)
#   with open("NewFrequencies.txt", "w", encoding="utf8") as outfile:
#     for word in words:
#       outfile.write(word + "\n")
    
# #clean_up_derived(fwords)
# new = []
# with open("NewFrequencies.txt", "r", encoding="utf8") as infile:
#   for line in infile:
#     word = line.split()
#     new.append(word[1])

# with open("NewFrequencies1.txt", "w", encoding="utf8") as outfile:
#   for word in new:
#     outfile.write(word + "\n")
# fwords = []
# with open("NewFrequencies1.txt", "r", encoding="utf8") as infile:
#   for line in infile:
#     fwords.append(line.strip("\n"))

# accepted = []
# rejected = []
# h = True
# with open("DerivedWordList.txt", "r", encoding="utf8") as infile:
#   for line in infile:
#     word = line.strip("\n")
#     if word in fwords:
#       accepted.append(word)
#     else:
#       rejected.append(word)
#     if (h and word == "cringed"):
#       print("hello")
#       h = False
      
# with open("FilteredBetaAccepted.txt", "w", encoding="utf8") as infile:
#   for word in accepted:
#     infile.write(word + "\n")

# with open("FilteredBetaRejected.txt", "w", encoding="utf8") as infile:
#   for word in rejected:
#     infile.write(word + "\n")

from wordfreq import zipf_frequency
from wordfreq import word_frequency

def load_filetered_beta():
  words = []
  with open("FilteredBetaAccepted.txt", "r") as infile1, open("FilteredBetaRejected.txt", "r") as infile2:
    for line in infile1:
      words.append(line.strip("\n"))
    for line in infile2:
      words.append(line.strip("\n"))
  return words

def get_zipf_frequency(words):
  words_zipf = []
  
  for word in words:
    words_zipf.append(str(zipf_frequency(word, 'en')) + " " + word)
    
  with open("f_beta.txt", "w") as outfile:
    for word in words_zipf:
      outfile.write(word+"\n")

def get_frequency(words):
  words_f = []
  for word in words:
    words_f.append(str(word_frequency(word, 'en')) + " " + word)
    
  with open("f_beta.txt", "w") as outfile:
    for word in words_f:
      outfile.write(word+"\n")
      
def get_avg_zipf():
  with open("NewBeta.txt", "r") as infile:
      # print("Word with maximum zipfrequency:", (lambda x: (x[1], x[0]))(min({zipf_frequency(line.strip("\n"), 'en'): line.strip("\n") for line in infile if zipf_frequency(line.strip("\n"), 'en') != 0 }.items())))
      # mini = min([zipf_frequency(line.strip("\n"), 'en') for line in infile if zipf_frequency(line.strip("\n"), 'en') != 0 ]) 
      # maxi = max([zipf_frequency(line.strip("\n"), 'en') for line in infile])
      zipf = [zipf_frequency(line.strip("\n"), 'en') for line in infile if zipf_frequency(line.strip("\n"), 'en') != 0]
      avg = (sum(zipf)/len(zipf))   
      # print(mini)
      return avg
      
def get_avg_frequency():  
  with open("FinalBeta.txt", "r") as infile:
      #print("Word with maximum frequency:", (lambda x: (x[1], x[0]))(max({word_frequency(line.strip("\n"), 'en'): line.strip("\n") for line in infile}.items())))
      # maxi =  max([word_frequency(line.strip("\n"), 'en') for line in infile if word_frequency(line.strip("\n"), 'en') != 0])
      f = [word_frequency(line.strip("\n"), 'en') for line in infile]
      avg = sum(f)/len(f)
      return avg
    
#1.01
#words = load_filetered_beta()  
#get_frequency(words)
#get_zipf_frequency(words) 
avg_zipf_beta_list = get_avg_zipf()
avg_frequency_beta_list = get_avg_frequency()
# print(avg_frequency_beta_list)
# print(avg_zipf_beta_list)

final_words = set()
with open("rare_words_lemmatized.txt", "r") as infile, open("RareFinal.txt", "w") as outfile:
  for line in infile:
    word = line.strip("\n")
    f = zipf_frequency(word, 'en')
    if (f >= 1.01 and f <= avg_zipf_beta_list):
      outfile.write(word + "\n")


# final_words = set()
# with open("zipf_beta.txt", "r") as infile:
#   for line in infile:
#     word = line.split()
#     if (float(word[0]) <= avg_zipf_beta_list):
#       final_words.add(word[1])

# # with open("f_beta.txt", "r") as infile:
# #   for line in infile:
# #     word = line.split()
# #     if (float(word[0]) == 0):
# #       continue
# #     if (float(word[0]) <= avg_frequency_beta_list):
# #       final_words.add(word[1])

# with open("FinalFinalFinal.txt", "w") as outfile:
#   for line in final_words:
#     outfile.write(line + "\n")
  
# counter = 0
# with open("FilteredBetaAccepted.txt", "r") as infile, open("NewBeta.txt", "r") as infile1:
#   for line in infile:
#     words.append(line.strip("\n"))
#   for line in infile1:
#     if (line.strip("\n") in words):
#       counter += 1
  
# print(str(counter) + "/730")
# print("DONE")