file_name = "futurefree.txt"
with open(file_name , "r") as f:
    words = f.read().split()

for word in words:
    if len(word) - (2* (word.count("f")  + word.count("u")+ word.count("c") + word.count("k") + word.count("r"))) < 0:
        print("{} ειναι Κακη".format(word))
    else:
        print("{} ειναι καλη".format(word))


