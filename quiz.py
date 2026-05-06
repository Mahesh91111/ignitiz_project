print("welocome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("okay! Let's play") ##ok

score = 0

answer =  input("what does cpu stand for? ")
if answer == "central processing unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

answer =  input("what doess gpu stand for")
if answer == "graphics processiing unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

answer =  input("what does random stand for? ")
if answer == "Random Accesses unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

answer =  input("what does psu stand for? ")
if answer == "power supply unit":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

print("Ypu got"+str(score)+"questions correct!")
print("Ypu got"+str(score/4*100)+"%.")
