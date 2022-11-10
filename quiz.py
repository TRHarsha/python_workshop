print("Welcome to INDIA's FIRST quiz ")
name=input("Lets begin with your first question \nWhat is your name: ")
print("Hello, ",name," That was a grace round \nRules of the quiz are as follows \nThere will be 10 Questions \nEach correct answer carries 5 points")
print("Your INDIA's FIRST QuiZ starts now\n1. India's first British Governor General of Bengal \n   a.Warren Hastings\n   b.Tim Cook\n   c.Jackie Chan\n   d.Jack Sparrow")
answer=input("\n What is your answer: ")
if answer == "a":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=5
else:
    print("Its Warren Hastings\n Better Luck in Next Question\n\n\n")
print("2. India's first Field Marshal \n   a.Amithshaw\n   b.Manekshaw\n   c.Mihir Jain\n   d.Sahil Sing")
answer=input("\n What is your answer: ")
if answer == "b":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its S. H. F. J. Manekshaw\n Better Luck in Next Question\n\n\n")
print("3. India's first Man to climb Mount Everest without Oxygen \n   a.Phu Dorjee\n   b.R. D. Katari\n   c.Thomas Elmhirst\n   d.G. Shankar Kurup")
answer=input("\n What is your answer: ")
if answer == "a":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Phu Dorjee\n Better Luck in Next Question\n\n\n")
print("4. India's first Test Tube Baby (Documented \n   a.Aridni\n   b.Parinaya\n   c.Indira\n   d.Vindira")
answer=input("\n What is your answer: ")
if answer == "c":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Indira\n Better Luck in Next Question\n\n\n")
print("5. India's first paperless Newspaper \n   a.Today's News\n   b.Inshorts\n   c.Daily Hunt\n   d.The News Today")
answer=input("\n What is your answer: ")
if answer == "d":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its The News Today\n Better Luck in Next Question\n\n\n")
print("6. The first Indian to cross seven important seas by swimming \n   a.Bhalwan Chaudhury\n   b.Bula Chaudhury\n   c.Barath Chaudhur\n   d.Birendhra Chaudhury")
answer=input("\n What is your answer: ")
if answer == "b":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Bula Chaudhury\n Better Luck in Next Question\n\n\n")
print("7. The first Indian to Ski to the North Pole \n   a.Ajeet Baja\n   b.Arati Saha Gupta\n   c.Sukumar Sen\n   d.	Acharya Vinoba Bhave")
answer=input("\n What is your answer: ")
if answer == "a":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Ajeet Baja\n Better Luck in Next Question\n\n\n")
print("8. India's first Talkie Film \n   a.Adhikarunye\n   b.Alam Ara\n   c.Ek wakth tha\n   d.Chichoore")
answer=input("\n What is your answer: ")
if answer == "b":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Alam Ara\n Better Luck in Next Question\n\n\n")
print("9. India's first Woman Lieutenant General \n   a.Durga Banerjee\n   b.Arudhanti Roy\n   c.Puneeta Arora\n   d.Santosh Yadav")
answer=input("\n What is your answer: ")
if answer == "c":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n ")
    i=i+5
else:
    print("Its Puneeta Arora\n Better Luck in Next Question\n\n\n")
print("10. India's first Woman Pilot in Indian Air Force \n   a.Harita kaur Dayal\n   b.Karnam Malleswari\n   c.Leela Seth\n   d.Ashapurna Devi")
answer=input("\n What is your answer: ")
if answer == "a":
    print("\a Congratulations \a\a\a\a\n You earned 5 points\n")
    i=i+5
else:
    print("Its Harita kaur Dayal\n Better Luck in Next Round\n\n\n")
print("\n CONGRATULATIONS ^u^ \n You scored: ",i,)
if i == 50:
    print("$10,000 is yours ",name)
if i >= 40 and i <= 49:
    print("$5,000 is yours ",name)
if i >= 30 and i <= 39:
    print("$1,000 is yours ",name)
if i >= 20 and i <= 29:
    print("$500 is yours ",name)
if i >= 10 and i <= 19:
    print("$50 is yours ",name)
if i >= 5 and i <= 9:
    print("$5 is yours ",name)
if i <= 5:
    print("Diary Milk Choclate of rs.10 to you ",name)