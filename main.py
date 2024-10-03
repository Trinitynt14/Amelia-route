def amelia():
    positive = input("are you sure?: ")
    if positive == "yes" or positive == "Yes":
        print('\033c')
        print("You chose the girl!")
        print("She looks at you not surprised or happy but neutural")
        print("she's smiling though...thats good right?")
        print("you two are lead to a room with a dining table")
        print("it's quite fancy")
        print(" ")
        print("you both sat down and after a few second of silence she speaks")
        print(" ")
        print("so your nice, to meet you.")
        print("I'm Amelia! I was honestly quite surprised you chose me")
        print(" ")
        like = input("you must like me if you choose me right? ")
        if like == "yes" or like == "Yes":
            print('\033c')
            print("really. thats surprising,and sudden")
            print("you've just met me how are you so sure")
            print(" ")
            print("she's being playful but it's so weird")
            print(" ")
            romance = input("do you consider yourself a romantic? ")
            if romance == "yes" or romance == "yes":
                print('\033c')
                print("oh really?")
                print("hopefully you aren't clingy.")
                print("that's annoying.")
                print(" ")
                death = input("are you scared of death?")
                if death == "no" or death == "No":
                    print('\033c')
                    print("really?!")
                    print("man you're really really interesting")
                    print("We have to part ways now. you'll probably choose me later on.")
                else:
                    if death == "yes" or death == "Yes":
                         print('\033c')
                         print("hm...")
                         print("you're really boring. I'm leaving now")
                         print(" ")
                         print("that could have gone better")
            else:
                if romance == "no" or romance == "No":
                    print('\033c')
                    print("oh really?")
                    dates = input("you'll still take me on dates though,right?")
                    if dates == "no" or dates == "No":
                        print('\033c')
                        print("my, you're boring.")
                        print("...That's all I needed to know")
                        print(" ")
                        print("she left. you have a feeling that didn't go too well")
                    else:
                        if dates == "yes" or dates == "Yes":
                            print('\033c')
                            print("that's good")
                            print("you're quite interesting")
                            print("I think this went well")
                            print(" ")
                            print("she left. you think it went well")
                            
        else:
            if like == "no" or like == "No":
                print('\033c')
                print("that's not shocking we just met")
                print("i'll make you like me though")
                print(" ")
                print("thats totally not creepy at all")
                print(" ")
                pets = input("do you like lions?")
                if pets == "yes" or pets == "yes":
                    print('\033c')
                    print("wonderful!")
                    print("I have two pet lions that I think would adore you!")
                    (" ")
                    choose = input("I think i've taken quite a liking to you. You'll choose me, right? ")
                    if choose == "yes" or choose == "Yes":
                        print('\033c')
                        print("Great! I'm glad we came to this agreement.")
                        print("dont change your mind later, Okay?")
                        print("she says before she leaves")
                    else:
                        if choose == "no" or choose == "No":
                            print("yes you will.")
                            print("I've taken a liking to you so of course you will")
                            print("you wouldn't want to see me sad would you?")
                            print(" ")
                            print("she's not giving you time to respond...")
                            print(" ")
                            print("I'll see you when you pick me alright.")
                            print(" ")
                            print("she stands up and then leaves")
                else:
                    if pets == "no" or pets == "No":
                        print('\033c')
                        print("oh.")
                        print("maybe it's best I dont take you to the circus then")
                        print(" ")
                        print("she seems dissapointed so you try cheering her up")
                        print("she gives a robotic laugh")
                        print(" ")
                        laugh = input("are you trying to cheer me up? ")
                        if laugh == "yes" or laugh == "Yes":
                            print('\033c')
                            print("you're so sweet")
                            print("hopefully you're quite agreeable later on aswell")
                            print(" ")
                            print("she leaves. it went well you think")
                        else:
                            if laugh == "no" or laugh == "No":
                                print("hm... I can't tel if you're joking or not.")
                                print("hopefully we have more time together later")
                                print(" ")
                                print("she leaves humming to herself")
                            
            
                
    else:
        if positive == "no" or positive == "No":
            print("placeholder")
amelia()
