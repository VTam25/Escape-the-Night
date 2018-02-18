
#Blueprint 2018!!!

#This is a program for a choose your own adventure story about safety when going out

from sys import exit


def start():
    print("Welcome!")
    print("What is your name?")
    name = input('')
    print("Hello " + name)

    

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
    elif get_in == ("y"):
        print('Bye bye...GAME OVER')
        kidnap_end()
    elif get_in == ("n"):
        print("You text your friend to see if they arrived yet.")
        print("They haven't.")
        print("You realize that the car in front of you is a stranger, you back away.") 
        return None
    
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
                return None
    elif pic_scenario == ('n'):
                print("You stayed in the car and rested a little while your friends took pictures")
                return None
            
def baby_scenario():
    print("Suddenly, a shadow appears near a streelight. It's a stroller, and you hear a baby crying. Do you ignore it or investigate it on your own?")
    baby_scenario = input('')
    if baby_scenario != ('ignore it') and baby_scenario != ('investigate it on your own'):
        print("Not a valid answer.")
        print("Do you ignore it, investigate it on your own, or investigate with your friends?")
    elif baby_scenario == ('ignore it'):
        print('You are going to ignore the crying baby and wait with your friends. You and your friend have finished taking pictures and you all get back into the car.')
        return None
    elif baby_scenario == ('investigate it on your own'):
        print('You are going to check out the stroller by yourself. However, when you walk you to it, there is no baby! The next thing you know, there is a cloth over your mouth and nose, and you slowly black out... GAME OVER') 
        kidnap_end()

def ask_bubble_scenario():
    print(friend+ " finds a place to park and you guys start deciding on what to do next.")
    print(friend+ " says 'Hey there's a bubble tea shop nearby.")
    print("You start to get bored as they talk. Do you choose to...")
    print("Pull out your Nintendo DS or " + "Help your friends decide where to go")
    bubble_choice = input('')
    if bubble_choice != ('Pull out your Nintendo DS') and bubble_choice != ('Help your friends decide where to go'):
        print("Not a valid answer")
<<<<<<< HEAD
    elif bubble_choice == ('Pull out your Nintendo DS'):
        print("Did you bring your DS (y/n)?")
        game2 = input('')
        if game2 != ('y') and game2 != ('n'):
            print("Not a valid answer.")
        elif game2 == ('y'):
            print("You pulled out your DS")
            robbed_end()
        elif game2 == ('n'):
            print("You didn't bring your DS with you. Sorry.")
            print(friend+ "finds a place to park and you guys start deciding on what to do next.")
            print(friend+ " said 'Hey there's a bubble tea shop nearby.'")
    elif bubble_choice == ('Help your friends decide where to go'):
=======
    elif game = ('n') and choice = ('Pull out your Nintendo DS'):
        print("You didn't bring your DS with you. Sorry.")
        print("Your " +friend "finds a place to park and you guys start deciding on what to do next.")
        print(+friend " said 'Hey there's a bubble tea shop nearby.")
        return None
    elif choice = ('Pull out Nintendo DS'):
        print("You pulled out your Nintendo DS")
        return None
    elif choice = ('Help your friends decide where to go'):
>>>>>>> ecb046d7b15f3df8f1fb39c8ea1c5b456f75d2d1
        print("You decided to help your friends choose where to go")
        return None

def robbed_end ():
    print("")    






    



    
    
def kidnap_end():
    print("")
    exit()

def win_end():
    print("")
    exit()

def die_end():
    print("")
    exit()
    
#This is where we run the story
    
start()
print("What is your friend's name?")
friend = input('')
back_story()
gameoptions_to_bring()
phone()
car_scenario()
pic_scenario()
baby_scenario()
ask_bubble_scenario()
