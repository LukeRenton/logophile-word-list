# words=[]
# with open("merriam_scrape.txt", "r") as infile:
#   for line in infile:
#     if (line[0].isupper()):
#       continue
#     words.append(line.strip("\n"))
# print(words)
# with open("merriam_scrape.txt", "w") as infile:
#   for line in words:
#     infile.write(line + "\n")

words = []
count = 0
with open("rare_words.csv", "r", encoding="utf8") as infile:
  for line in infile:
    word = line.split(",")
    words.append(word[0])

with open("rare_words.txt", "w") as outfile:
  for word in words:
    outfile.write(word + "\n")