import gensim.downloader as api
from nltk.stem import WordNetLemmatizer 
from better_profanity import profanity

def valid_word(derived_word):
  return derived_word.isalpha() and len(derived_word) > 4 and not profanity.contains_profanity(derived_word)

def get_similar_words():
  sample_words = []
  with open("merriam_scrape.txt", "r") as infile:
      for line in infile:
          sample_words.append(line.strip("\n").lower())
  
  # Train the Word2Vec model on the list of sentences (list of lists)
  # model = Word2Vec(bulk_list, vector_size=100, window=5, min_count=1, sg=1)
  model = api.load("word2vec-google-news-300")
  
  similar_words = {}
  for word in sample_words:
      if word in model.key_to_index:
          # Find similar words for the word
        similar_words[word] = model.most_similar(word)
        
        # Filter similar words based on the root words
        #cleaned_similar_words = [(sim_word, sim_score) for sim_word, sim_score in similar_word_pairs if (sim_word == PorterStemmer().stem(sim_word))]
        
        # Add cleaned similar words to the similar_words dictionary
        #similar_words[word] = cleaned_similar_words
  # Display the results
  with open("FormattedDerviedWordList2.txt", "w", encoding="utf8") as file:
    derived_words = set()
    for word, similar in similar_words.items():
        derived_words.add(word)
        file.write("Words similar to " + word + ":\n" +"==============================\n")
        for sim_word, sim_score in similar:
          if valid_word(sim_word):
            derived_words.add(sim_word)
          file.write(sim_word + " : " + str(sim_score) + "\n")
        file.write("\n")
        
    print("Length of word list before cleanup: " + str(len(derived_words)))
    clean_up_derived(derived_words)
    
    
words = []
with open("rare_words.txt", "r") as infile:
  for line in infile:
    word = line.strip("\n")
    if (valid_word(word)):
      words.append(word)


def clean_up_derived(derived_words):
  words = []
  lemmatizer = WordNetLemmatizer()
  root_words = set()

  for word in derived_words:
      root_word = lemmatizer.lemmatize(word)
      root_words.add(root_word)
  words = list(root_words)
  print("Length of word list after cleanup: " + str(len(words)))
  with open("rare_words_lemmatized.txt", "w", encoding="utf8") as outfile:
    for word in words:
      outfile.write(word + "\n")
clean_up_derived(words)    
# get_similar_words()
