"""The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.

Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

For example:
Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""

import random

question  = input("Question:      ")
num = random.randint(1, 9)

if num == 1:
    resp = "Yes - definitely."
elif num == 2:
    resp = "It is decidedly so."
elif num == 3:
    resp = "Without a doubt."
elif num == 4:
    resp = "Reply hazy, try again."
elif num == 5:
    resp = "Ask again later."
elif num == 6:
    resp = "Better not tell you now."
elif num == 7:
    resp = "My sources say no."
elif num == 8:
    resp = "Outlook not so good."
else:
    resp = "Very doubtful."

print("Magic 8 Ball:  ", resp)