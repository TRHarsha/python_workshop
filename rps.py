import random
tools = ["rock","paper","scissors"]
user=input("Enter your move [rock,paper,scissors]: ")
reply=random.choice(tools)
if user == reply:
    print("My move: ",reply)
    print("Try one more time")
elif user == "rock" and reply == "paper":
    print("My move: ",reply)
    print("I win")
elif user == "paper" and reply == "scissors":
    print("My move: ",reply)
    print("I win")
elif user == "scissors" and reply == "rock":
    print("My move: ",reply)
    print("I win")
else:
    print("My move: ",reply)
    print("YOU WIN")