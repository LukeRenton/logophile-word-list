words = []
with open("rare_words_lemmatized.txt", "r") as infile1, open("FinalAlpha.txt", "r") as infile2, open("BackupWords.txt", "w") as outfile:
  for line in infile2:
    words.append(line.strip("\n"))
  for line in infile1:
    word = line.strip("\n")
    if (not word in words):
      outfile.write(word + "\n")
      