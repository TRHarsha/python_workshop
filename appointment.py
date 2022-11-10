print("Hi welcome to MahanBaba.com")
option=int(input("1.Book an appointment \n2.Reshedule the appointment \n3.Cancel an appointment \n4.Other Services \n5.customer support\nEnter your option: "))
#Booking an appointment
if option == 1:
    print("Thanks for choosing MahanBaba.com")
    during=input("We have 3 different slots \n morning,afternoon,evening \n Which one do you prefer: ")
    if during == "morning":
        time=input("We have 3 time line in the morning \n 7am,8am,9am \n At what time do wish to have the appointment: ")
        if time == "7am":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 17")
        if time == "8am":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 18")
        if time == "9am":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 19")
    elif during == "afternoon":
        time=input("We have 3 time line in the morning \n 12pm,1pm,2pm \n At what time do wish to have the appointment: ")
        if time == "12pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 12")
        if time == "1pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 21")
        if time == "2pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 22")
    elif during == "evening":
        time=input("We have 3 time line in the morning \n 5pm,6pm,7pm \n At what time do wish to have the appointment: ")
        if time == "6pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 35")
        if time == "7pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 36")
        if time == "8pm":
            print("Congratulations \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 37")
#Other services provided
elif option == 4:
    print("We appreciate your efforts to know other services")
    oservice=int(input("We also provide \n 1.Kundali Matching \n 2. Online Guna Milan \n 3.Just Checking \n Enter the no for more information: "))
    if oservice == 1:
        print("In Vedic Astrology, the concept of Kundli Matching or Horoscope Matching is very eminent. Marriage is the sacred bond between two separate \n entities, bringing them together for a long and healthy marital life. There are different names for matchmaking viz, Kundali Milan, Guna Milan,\n Horoscope Matching and Compatibility, Lagna Melapak etc \n For more information book an appointment with Mahan Baba")
        schedule=input("Do you want to schedule an appointment yes/no: ")
        if schedule == "yes":
            print("Thanks for choosing MahanBaba.com")
            during=input("We have 3 different slots \n morning,afternoon,evening \n Which one do you prefer: ")
            if during == "morning":
                time=input("We have 3 time line in the morning \n 7am,8am,9am \n At what time do wish to have the appointment: ")
                if time == "7am":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 17")
                if time == "8am":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 18")
                if time == "9am":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 19")
            elif during == "afternoon":
                time=input("We have 3 time line in the morning \n 12pm,1pm,2pm \n At what time do wish to have the appointment: ")
                if time == "12pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 12")
                if time == "1pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 21")
                if time == "2pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 22")
            elif during == "evening":
                time=input("We have 3 time line in the morning \n 5pm,6pm,7pm \n At what time do wish to have the appointment: ")
                if time == "6pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 7AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 35")
                if time == "7pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 8AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 36")
                if time == "8pm":
                    print("Congratulations:) \n The Mahan Baba has made an appointment wih you at 9AM Tomorrow Morning \n Please ensure stable internet connection and have ZOOM downloaded\n You'll recieve confirmation message on registered number \n TOKEN NO. 37")
        if schedule == "no":
            print("No problem ")
    elif oservice == 2:
        print("Thank for choosing online GUNA MILAN \nKoota                   |Maximum Points\n--------------------------------------\nVarna	                | 1\nVasya/Vashya	        | 2\nTara/Dina	        | 3\nYoni	                | 4\nGrah Maitri/Rasyadipati	| 5\nGana	                | 6\nRashi or Bhakoota	| 7\nNadi                    | 8\n")
        mm=int(input("Enter the points you have obtained ;) : "))
        if mm < 18:
            print("	Not recommended for marriage")
        elif mm >= 18 and mm <= 24:
            print("Average, Acceptable match and recommended for marriage")
        elif mm >= 24 and mm <= 32:
            print("	Very Good, successful marriage")
        elif mm >+ 32 and mm <= 36:
            print("Excellent Match")
#Reschedule an appointment
if option == 2:
    tkn = int(input("Enter your token Number "))
    if tkn == 17:
        print("\n You've Booked Morning 7A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 18:
        print("\n You've Booked Morning 8A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 19:
        print("\n You've Booked Morning 9A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 12:
        print("\n You've Booked Afternoon 12P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 21:
        print("\n You've Booked Afternoon 1P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 35:
        print("\n You've Booked Afternoon 5P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 36:
        print("\n You've Booked Evening 6P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    elif tkn == 37:
        print("\n You've Booked Eveneing 7P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
        print("\n You can reschedule your Appointment")
    else:
        print("\n Token number is not available \n Please go get an appointment \n THANK YOU!")
#Cancelling an Appointment
if option == 3:
    print(" For Cancelling An meeting pls fill this ")
    pno=input(" Registered Phone number:")
    tkn = int(input("Enter your token Number: "))
    if tkn == 17:
        print("\n You've Booked Morning 7A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 18:
        print("\n You've Booked Morning 8A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 19:
        print("\n You've Booked Morning 9A.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 12:
        print("\n You've Booked Afternoon 12P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 21:
        print("\n You've Booked Afternoon 1P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 35:
        print("\n You've Booked Afternoon 5P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 36:
        print("\n You've Booked Evening 6P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    elif tkn == 37:
        print("\n You've Booked Eveneing 7P.M Session \n Verifying Your Registered Mobile Number \n 5 4 3 2 1.....\n The number has been Successfully verified")
    else:
        print("\n Token number is not available \n Please go get an appointment \n THANK YOU!")
        exit()
    print("Reason for  Cancelling An meeting ")
    choose=int(input("\n1= Not interested \n2= Personal issue \n3= Cant say \n4= Got some other work \nenter the choice: "))
    if choose==1:
        print("ok we respect your opinion")
    elif choose==2:
        print("ok you can book another appointment some time later")
    elif choose==3:
        print("We are glad we could help \n Thank you")
    elif choose==4:
        print("We hope you could try rescheduling else no worries \n We have cancelled your apppointment")
#customer support
if option == 5:
    print("Type 'not reieved conformation mail' for mail ID related quieries")
    print("Type 'not able to connect to zoom' for zoom related quieries")
    print("Type 'Mahan baba voice is audible but no video' for video related quieries")
    print("Type 'Mahan baba voice is breaking' for voice issue related quieries")
    print("Type 'zoom link is not activated' for activation related quieries")
    problem= input("What help you need:")
    if problem == "not recieved confirmation mail":
        print("let us resend it again")
    elif problem == "not able to connect to zoom":
        print("try reinstalling the application")
        zoom=input("Zoom ID:")
        if zoom == "NA":
            print("We are happy we could help")
        else:
            print("Try login from different account")
    elif problem == "Mahan baba voice is audible but no video":
        print("ensure that all the permission are enabled")
    elif problem == "Mahan Baba voice breaking":
        print("check your internet connection then try again")
    elif problem == "Zoom link is not activated":
        print("wait for sometime, we will activate it soon")
    else:
        print("my problem is not mentioned above \n write us at customer_support@mahanbaba.in")
print("\n Thank You for choosing MAHAN BABA ^v^")