import random


print("H A N G M A N\n")

word_list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
right_answer = random.choice(word_list)

secret_word = "-" * len(right_answer)
lives = 8
tried_chars = set()

while lives > 0:
    print(secret_word)
    if right_answer == secret_word:
        print("You guessed the word!\nYou survived!")
        break
    char = input("Input a letter: ")
    if char not in tried_chars:
        tried_chars.add(char)
        if char not in right_answer:
            lives -= 1
            print("No such letter in the word")
        else:
            for j in range(len(right_answer)):
                if right_answer[j] == char:
                    temp_list = list(secret_word)
                    temp_list[j] = char
                    secret_word = "".join(temp_list)
    else:
        lives -= 1
        print("No improvements")
    print()
else:
    print("You are hanged!")
