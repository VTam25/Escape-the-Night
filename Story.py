
#Blueprint 2018!!!

#This is a program for a choose your own adventure story about safety when going out

from sys import exit


def start():
    print("Welcome!")
    print("What is your name?")
    name = input('')
    print("Hello " + name)
    print("What is your friend's name?")


def back_story():
    print("You are out with your friends in Cambridge exploring the MIT campus for a fun time!")
    print("You guys decide to go shopping and choose some other things to do. YAY!")
    print("***flash*** A catchy alarm goes off on your cell phone. It's 4:20pm. You whisper to yourself that there's only an hour left until you have to go out with friends.")
    print("You start to get ready...")
    print("What are you going to bring?")


def gameoptions_to_bring():
    print("Do you want to bring a game (y/n)?")
    game = input('')
    if game != ('y') and game != ('n'):
        print("Not a valid answer.")
        print("Do you want to bring a game (y/n)?")
    elif game == ("y"):
        print("What game are you planning to bring?")
        print("Pokemon Black & White? " + "Nintendogs? " + "Super Smash Bros? " + "Kirby: Triple Deluxe? ")
        game_choice = input('')
        if game_choice != ('Pokemon Black & White') and game_choice != ('Nintendogs') and game_choice != ('Super Smash Bros') and game_choice != ('Kirby: Triple Deluxe'):
            print("Not a valid answer.")
            print("Pokemon Black & White? " + "Nintendogs? " + "Super Smash Bros? " + "Kirby: Triple Deluxe? ")
        elif game_choice == ('Pokemon Black & White'):
            print("You chose to take Pokemon Black & White.")
            return None 
        elif game_choice == ('Nintendogs'):
            print("You chose to take Nintendogs.")
            return None 
        elif game_choice == ('Super Smash Bros'):
            print("You chose to take Super Smash Bros")
            return None 
        elif game_choice == ('Kirby: Triple Deluxe'):
            print("You chose to take Kirby: Triple Deluxe")
            return None
    elif game == ('n'):
        print("You did not choose to bring a game")
        return None
    
def phone():
    print("Will you bring your phone (y/n)?")
    phone = input('')
    if phone != ('y') and phone != ('n'):
        print("Not a valid answer.")
        print("Will you bring your phone (y/n)?")
    elif phone == ('y'):
        print("You chose to bring your phone.")
        print("Your phone is at 50%, do you want to bring a portable charger (y/n)?")
        portable_charger = input('')
        if portable_charger != ('y') and portable_charger != ('n'):
            print("Not a valid answer.")
            print("Your phone is at 50%, do you want to bring a portable charger (y/n)?")
        elif portable_charger == ('y'):
            print("You will bring your portable charger with you.")
            return None
        elif portable_charger == ('n'):
            print("You will not bring your portable charger with you.")
            return None 
    elif phone == ('n'):
        print("You did not bring your phone.")
        print("Good luck.")
        return None


def car_scenario():
    print("You head out the door and get ready to meet " + friend)
    print("You see a car that looks like your friend's pull up to you and it honks at you to get in.")
    print("The windows are tinted but you heard your friend had recently gotten their windows tinted.")
    print("Do you get in the car (y/n)?")
    get_in = input("")
    if get_in != ("y") and get_in != ("n"):
        print("Not a valid answer")
        print("Do you get in the car (y/n)?")
    elif get_in == ("y"):
        kidnap_end()
    elif get_in == ("n"):
        print("You text your friend to see if they arrived yet.")
        print("They haven't.")
        print("You realize that the car in front of you is a stranger, you back away.") 
        pic_scenario()
    
def pic_scenario():
    print("Congrats, you aren't an idiot! You wait for for your friend's actual car to pull up and hop in.")
    print("You and your friends are now headed into the city.")
    print("You look out the window and see a beautiful sunset to your right")
    print("'Guys look at that view!' someone says. 'Wow, lets go take some pictures' your friend suggests")
    print("Your group decides to go take some pictures. Do you go with them? (y/n)")
    pic_scenario = input('')
    if pic_scenario != ('y') and pic_scenario != ('n'):
                print("Not a valid answer")
                print("Do you go with them to take pictures? (y/n)")
    elif pic_scenario == ('y'):
                print("You decided to take some insta-worthy pics with your friends!")
                baby_scenario()
    elif pic_scenario == ('n'):
                print("You stayed in the car and rested a little while your friends took some pictures. After a while they come back and keep driving.")
                ask_bubble_scenario()
            
def baby_scenario():
    print("Suddenly, a shadow appears near a streelight. It's a stroller, and you hear a baby crying. Do you ignore it or investigate it on your own?")
    baby_scenario = input('')
    if baby_scenario != ('ignore it') and baby_scenario != ('investigate it on your own'):
        print("Not a valid answer.")
        print("Do you ignore it, investigate it on your own, or investigate with your friends?")
    elif baby_scenario == ('ignore it'):
        print('You are going to ignore the crying baby and wait with your friends. You and your friend have finished taking pictures and you all get back into the car.')
        ask_bubble_scenario()
    elif baby_scenario == ('investigate it on your own'):
        print('You are going to check out the stroller by yourself.') 
        kidnap_end()

def ask_bubble_scenario():
    print(friend+ " finds a place to park and you guys start deciding on what to do next.")
    print(friend+ " says 'Hey there's a bubble tea shop nearby.'")
    print("You start to get bored as they talk. Do you choose to...")
    print("Pull out your Nintendo DS or " + "help your friends decide where to go?")
    bubble_choice = input('')
    if bubble_choice != ('Pull out your Nintendo DS') and bubble_choice != ('Help your friends decide where to go'):
        print("Not a valid answer")
        print("Do you choose to pull out your Nintendo DS or help your friends decide where to go?")
    elif bubble_choice == ('Pull out your Nintendo DS'):
        print("Did you bring your DS (y/n)?")
        game2 = input('')
        if game2 != ('y') and game2 != ('n'):
            print("Not a valid answer.")
            print("Did you bring your DS (y/n)?")
        elif game2 == ('y'):
            print("You pulled out your DS")
            phone_decision()
        elif game2 == ('n'):
            print("You didn't bring your DS with you. Sorry.")
            print(friend+ " finds a place to park and you guys start deciding on what to do next.")
            print(friend+ " said 'Oh I heard there's a laser tag place nearby.'")
            laser_tag()
    elif bubble_choice == ('Help your friends decide where to go'):
        print("You decided to help your friends choose where to go")
        laser_tag()

def phone_decision ():
    print("You've played for a few minutes and you looked up and start to walk around looking for your group but soon realize you are alone, confused, and S H O O K.")
    print("You try calling them. Where is your phone? in your pocket or at home?") 
    choice = input('')
    if choice != ('home') and choice != ('pocket'):
        print("Not a valid answer. Where is your phone? in your pocket or at home?")
    elif choice == ('pocket'):
        print("Do you want to call your friends? (y/n)")
        choice2 = input('')
        if choice2 != ('y') and choice2 != ('n'):
            print("Not a valid answer. Do you want to call your friends? (y/n)")
        elif choice2 == ('y'):
            print("Your phone is running out. To call them you must use a portable charger")
            print("Did you bring your portable charger? (y/n)")
            choice3 = input('')
            if choice3 != ('y') and choice3 != ('n'):
                print("Not a valid answer. Did you bring your portable charger? (y/n)")
            elif choice3 == ('y'):
                print("Ok you plug in your phone and call your friends.")
                print("They tell you to meet them at laser craze")
                laser_tag()
            elif choice3 == ('n'):
                print("RIP. Good luck")
                robbed_end()
        elif choice2 == ('n'):
            print("RIP. Good luck")
            robbed_end()
    elif choice == ('home'):
        print("RIP Good Luck") 
        robbed_end()


def robbed_end ():
    print("You are unable to call your friends because you did not bring your phone and/or did not bring your portable charger.")
    print("You begin to panic and walk around looking for your friends when you notice a figure following you")
    print("You ignore it thinking it's a coincidince until you feel a hand on your bag...")
    print("YOU'VE BEEN ROBBED! This could have been prevented if you had only brought your phone and charger :( sorry")
    end()    

def taxi_decision ():
    print("Congrats! you made the right decision to bring your phone and portable charger!")
    print("You decide to call a taxi cab.") 
    print("Do you want to just leave your friends and go home or meet them at the laser tag place? tag or home?")
    choice=input('')
    if choice != ('laser tag') and choice != ('home'):
        print("Not a valid answer. Do you want to just leave your friends and go home or meet them at a laser tag place?")
    elif choice == ('laser tag'):
        print("You decide to take the cab to the laser tag place to meet up with your friends")
        return None 
    elif choice == ('home'):
        print("You decide to just go home and call it a night.")
        win_end()

def laser_tag ():
	print("You made it to the laser craze place and joined a game with your friends.")
	print("You're having a fun time tagging people when you see a figure in the distance.")
	print("What do you do? shoot, run, or run to your friends?")
	choice = input('')
	if choice != ("shoot") and choice != ("run") and choice != ("run to your friends"):
		print("Not a valid answer. What do you do? Shoot, Run, or Run to your friends?")
	elif choice == ('shoot'):
		print("UH OH the guy's laser gun was actually A REAL GUN!!!")
		die_end()
	elif choice == ('run'):
		print("UH OH the guy's laser gun was actually A REAL GUN! You escaped but your friends did not!!!")
		print("You wait for hours with the paramedics and police until they say you can finally go home.")
		win_end()
	elif choice == ('run to your friends'):
		print("UH OH the guy's laser gun was actually A REAL GUN! You and your entire group died!!!")
		win_end()
    
def kidnap_end():
    print("Your mouth was suddenly covered with a cloth that has chloroform on it.")
    print("Everything goes dark. You've been kidnapped.")
    print("So sad. This could've easily been prevented. Choose wisely next time :)")

def win_end():
    print("You made it home safe and sound! Sorry for the rough night. Have a good night sleep!")
    end()

def die_end():
    print("You die. So sorry :(")
    end()

def end ():
    print("Visit our Github to look at our supplementary website")
    exit()
    
#This is where we run the story
    
start()
friend = input('')
back_story()
gameoptions_to_bring()
phone()
car_scenario()


