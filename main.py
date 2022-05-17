import random

f = open("words.txt", "r")
words = f.read()
f.close()

def make_poem(start_word, suitable_words):
    suitable_words = random.choices(suitable_words, k=5)
    if len(set(suitable_words)) < len(suitable_words):
        print("Sorry we couldn't make a poem")
    else:
        suitable_words = " ".join(suitable_words)
        print(f"{start_word} {suitable_words}")

all_words = [word for word in words.split()]
input_word = input("Enter a refrence word...   ")
suitable_words = [suitable_word for suitable_word in all_words if suitable_word[-3:] == input_word[-3:]]

make_poem(input_word, suitable_words)


while True:
    if input("Do you want to regenirate the poem? (Y/N)   ").lower() == "y":
        make_poem(input_word, suitable_words)
    else:
        break