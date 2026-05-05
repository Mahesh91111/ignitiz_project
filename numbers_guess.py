import random

top_range =  input("Type a number: ")


if top_range.isdigit():
    top_range = int(top_range)

    if top_range < 0:
        print("please a type a number larget than 0")
        quit()
else:
    print("please a type a number which is grater than 0")
    quit()

random_number=random.randint(0,top_range)

guess = 0

while True:
    guess +=1
    user_guess =  input("Make a guess: ")
    if user_guess.isdigit():
     user_guess = int(user_guess)
    else:
      print("please a type a number which is grater than 0")
      continue
    if user_guess == random_number:
       print("you got it!")
       break
    elif user_guess > random_number:
          print("you are above the nummber! ")
    else:
        print("you were below below the number")
print("you got it",guess,"guess")


