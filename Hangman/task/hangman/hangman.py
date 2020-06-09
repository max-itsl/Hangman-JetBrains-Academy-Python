import random


print("H A N G M A N\n")

word_list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
right_answer = random.choice(word_list)

secret_word = "-" * len(right_answer)

for i in range(8):
    print(secret_word)
    char = input("Input a letter: ")
    if char not in right_answer:
        print("No such letter in the word")
    else:
        for j in range(len(right_answer)):
            if right_answer[j] == char:
                list1 = list(secret_word)
                list1[j] = char
                secret_word = "".join(list1)
    print()

print("Thanks for playing!\nWe'll see how well you did in the next stage")
