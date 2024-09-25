gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


question01 = int(input(
    "Do you like Dawn ou Dusk?"
    "\n1) Dawn"
    "\n2) Dusk\n"
    ))

if question01 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question01 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input\n")

question02 = int(input(
    "When I’m dead, I want people to remember me as:"
    "\n1) The Good"
    "\n2) The Great"
    "\n3) The Wise"
    "\n4) The Bold\n"
    ))

if question02 == 1:
    hufflepuff += 2
elif question02 == 2:
    slytherin += 2
elif question02 == 3:
    ravenclaw += 2
elif question02 == 4:
    gryffindor += 2
else:
    print("Wrong input\n")    

question03 = int(input(
    "Which kind of instrument most pleases your ear?"
    "\n1) The violin"
    "\n2) The trumpet"
    "\n3) The piano"
    "\n4) The drum\n"
    ))

if question03 == 1:
    slytherin += 4
elif question03 == 2:
    hufflepuff += 4
elif question03 == 3:
    ravenclaw += 4
elif question03 == 4:
    gryffindor += 4
else:
    print("Wrong input\n")

print()

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= ravenclaw:
    print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')

print()    