
#Blueprint 2018!!!

#This is a program for a choose your own adventure story about safety when going out

from sys import exit


def start():
    print("Welcome!")
    print("What is your name?")
    name = input('')
    print("Hello " + name)
    print("What is your friend's name?")
    friend = input('')
    

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
    



























def pic_scenario():





























def baby_scenario():





























def ask_bubble_scenario():
    print("You and/or your friend have finished taking pictures and you all get back into the car.")
    print("Your " +friend "finds a place to park and you guys start deciding on what to do next.")
    print(+friend " said 'Hey there's a bubble tea shop nearby.")
    print("You start to get bored as they talk. Do you...")













    






    
    

def kidnap_end():
    print("")

def win_end():
    print("")

#This is where we run the story
    
start()
back_story()
gameoptions_to_bring()
phone()


