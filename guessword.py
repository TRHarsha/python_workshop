import random
counter = 0
crtopt=0
word = ["aiml","varun","derek","peace","crush","hithesh","python","educate"]
picword=random.choice(word)
ascii_msg=[]
char_msg=[]
for i in picword:
#ord converts char to ascii
    ascii=ord(i)
    ascii=ascii+random.randint(1,5)
    ascii_msg.append(ascii)
for i in ascii_msg:
    code=chr(i)
    char_msg.append(code)
for i in char_msg:
    print(i,end='')
print("\nGUESS THE WORD\n")
while(counter<7):
    word=input("Answer: ")
    wordlen=len(word)
    for i in range(0,wordlen):
        if word[i] == picword[i]:
           crtopt=crtopt+1
        else:
            break
    percentage=(crtopt/wordlen)*100
    if percentage >= 100:
        print("YOU GUESSED IT RIGHT")
        break
    else:
        print(percentage,"% that is ",crtopt,"letters is correct")
        key = input("Enter any key to try again")