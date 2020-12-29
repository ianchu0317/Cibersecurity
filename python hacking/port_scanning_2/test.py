word = input("Insert a word with a coma: ")
if "," in word:
    word = word.split(", ")
    print (word)

print ("Lo introcido es ", word, ".")