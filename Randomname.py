import random
counter = 0
boys=[
"ADIL HUSSAIN",	
"MUBARAK M",		
"RAJATH R PAI",	
"SAGAR KUMAR",	
"SAGAR MR",	
"SUCHITH A",	
"VAIBHAV UR",	
"ANKIT",	
"DARSHAN GM",
"EESHAN V C",
"PRAJWAL C S",	
"RAHUL.C.S",
"RAKEEN HARMAIN KHAN",
"SHANKAR S INDE",
"TAMEEM ABRAR UL HAQ",	
"VISHWAKIRAN.C.S",
"GAJENDRA",	
"ABDUL WAHAB SUFYAN",
"CHANDAN PATIL MG",
"GURUDATH RP",
"SIDDANNA MAHADEV DADDANNAVAR",
"SUPRAJ S SHEERYADA",
"GAGANDEEP RAO",
"KARTHIK KP",
"Ratan",
"Vishruth",
"Farhaan",	
"MALLIKARJUNA"]
girls =[
"HARSHITHA V",
"MAMATHA S C",
"ZOYA FATHIMA",
"ARPITHA R",
"KRUPA V",
"NISARGA M",
"SANJANA H V",
"SNEHA P",
"BHOOMIKA EN",
"NIREEKSHA B",
"PRATHIBHA P",
"SAMANVITHA SR",
"SHARANYA M KUMAR",
"SHREYA NS",
"SIRI K S",
"VARSHINI T NAIK",
"NANDINI A R",
"DHANYA MADHUKESHWAR BHAT",
"Priyanka","L1","L2","L3"]
while counter <10:
    picked=random.choice(boys)
    print(picked)
    boys.remove(picked)
    picked1=random.choice(boys)
    print(picked1)
    boys.remove(picked1)
    picked2=random.choice(boys)
    print(picked2)
    boys.remove(picked2)
    picked3=random.choice(girls)
    print(picked3)
    girls.remove(picked3)
    picked4=random.choice(girls)
    print(picked4)
    girls.remove(picked4)
    picked5=random.choice(girls)
    print(picked5)
    girls.remove(picked5)
    print("\n")
    counter += 1