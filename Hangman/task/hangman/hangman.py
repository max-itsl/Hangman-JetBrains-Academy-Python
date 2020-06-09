import random


print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
random.seed()
right_answer = random.choice(word_list)
if input("Guess the word "
         + right_answer[:3]
         + "-" * (len(right_answer) - 3)
         + ": > "
         ) == right_answer:
    print("You survived!")
else:
    print("You are hanged!")
