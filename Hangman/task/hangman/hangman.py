import random


print("H A N G M A N\n")

word_list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
right_answer = random.choice(word_list)

secret_word = "-" * len(right_answer)
lives = 8
tried_chars = set()

while True:
    game = input('Type "play" to play the game, "exit" to quit:')
    if game == "play":
        while lives > 0:
            print(secret_word)
            if right_answer == secret_word:
                print(f"You guessed the word {right_answer}!\nYou survived!")
                break
            char = input("Input a letter: ")
            if 0 < len(char) < 2:
                if char.islower() and char.isalpha():
                    if char in tried_chars:
                        print("You already typed this letter")
                    else:
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
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should input a single letter")
            print()
        else:
            print("You are hanged!")
    elif game == "exit":
        break
    else:
        continue
