"""This is an interactive UNC basketball game program based off of a game from Feb 8th, 2018."""


from random import randint


__author__ = "730163077"
player: str = ""
points: int = 0
EMOJI0 = "\U0001F622 \U0001F627 \U0001F973 \U0001F40F \U000026F9 \U0001F93E \U0001F3C0 \U0001F604"
EMOJI1 = "\U0001F914 \U0001F3C6 \U0001F525 \U0001F62D \U0000274C  \U0001F606 \U0000231A"
# Fulfills requirement 7


def main() -> None:
    """Entrypoint of program."""  # Fulfills requirement 0, 2
    global points
    points = 0
    greet()
    choice1()
    print(choice2())
    points = choice3(points)
    loop()
    choice4()
    end()


def greet() -> None:
    """Greetings."""  # Fulfills requirement 1
    global player
    player_with_ball = "\U000026F9"
    ball = "\U0001F3C0"
    print(f"Hello new UNC men's basketball player! {player_with_ball} ")
    print("Tonight we play Duke, our rivals.")
    print("We need your help to win.")
    print("Make the right choices and we WILL rush Franklin tonight!!\n")
    player = input("What is your name? ")
    print(f"Hello { player }! Here's the ball, get on the court! {ball} \n") 


def choice1() -> None:
    """Returns a choice."""  # Fulfills requirement 3
    # Choices are case-sensitive, type as shown
    print("In this game, you have to act quick!")
    global points
    global player
    question_face = "\U0001F914"
    sad = "\U0001F622"
    swirly = "\U0001F635"
    scared = "\U0001F627"
    choice1 = input(f"Shoot a three or pass to Luke Maye or throw the ball to Ramses? {question_face} ")
    if choice1 == "Shoot a three":
        points = points + 2
        print(f"You missed {sad} . Duke rebounds. RUN back { player }! \n")
    else:
        if choice1 == "pass to Luke Maye":
            points = points + 3
            print("Score! Up two points. \n")
        else:
            if choice1 == "throw the ball to Ramses":
                points = points + 1
                print(f"Ramses is not on the team!? {swirly} You caused a turnover!")
                print(f"Coach Williams is calling you. {scared} Get on the bench.\n")
                print(f"Your game is over champ, better luck next time { player }.")
                print(f"You scored { points } points.")
                start_over = input("Would you like to play again? Y or N ? \n")
                if start_over == "Y":
                    main()
                else:
                    if start_over == "N":
                        print("Thank you for playing!")
                        quit()
    

def choice2() -> str:
    """Returns a random choice."""  # Fulfills requirement 8, 10
    global player
    global points
    fire = "\U0001F525"
    slamdunk = "\U0001F93E"
    print(f"You are playing a great game { player }! Keep it up!! {fire}  ")
    choice2 = randint(1, 400)
    if choice2 < 100:
        points = points + 3
        return "You have stolen the ball from Grayson Allen! He is now crying. Great job! \n"
    else:
        if choice2 < 200:
            points = points + 5
            return f"Theo Pinson passed you the ball. Slam Dunk!! {slamdunk} \n"
        else:
            if choice2 < 300:
                points = points + 2
                return "Wendell Carter Jr. fouls you. Time to make a free throw. \n"
            else:
                if choice2 < 400: 
                    points = points + 4
                    return "Timeout! Drink some water, you are playing a great game. \n"
    return choice2


def choice3(points: int) -> int:
    """Takes points and prints a statement corresponding to how many points already have."""  # Fulfills requirement 5
    global player
    if points == 5:
        points += 3
        print(f"We are falling behind. { player }, we need you to score. You have { points } points! \n")
    else:
        if points == 6:
            points += 6
            print("Marvin Bagley loses the ball out of bounds. Cameron Johnson passes to you for an easy layup.")
            print(f"You have { points } points { player }. \n")
        else:
            points += 1
            print("You dribble behind your back and nearly break Grayson Allen's ankle!")
            print(f"You have { points } points { player }.\n")
    return points


def loop() -> None:
    """This is a loop."""  # Fulfills requirement 9
    global points
    global player
    x = "\U0000274C"
    smile = "\U0001F604"
    while True:
        loop = input("Now, pass to Platek or pass to B-Rob or quit? ")
        if loop == "pass to Platek":
            points += 3
            print(f"Platek is blocked! {x} Recover { player }, find an opening!")
            print(f"You have scored { points } points so far! \n")
        else:
            if loop == "pass to B-Rob":
                points += 3
                print(f"Nice pass { player }, B-Rob makes a three! You have scored { points } points so far! \n")
                break
            else:
                if loop == "quit":
                    points += 1
                    print(f"You scored { points } points. Thank you for playing. {smile}")
                    quit()
    print("Keep it up, hotshot! \n")
    

def choice4() -> None:
    """Returns a final choice."""  # Fulfills requirement 4
    global player
    global points
    excited = "\U0001F606"
    clock = "\U0000231A"
    print("We have two minutes left in the second half. It all comes down to this.")
    print(f"We need you { player }! Play smart.")
    choice1 = input("Pass to Joel Berry or throw the ball from half court or foul Grayson Allen? \n")
    if choice1 == "Pass to Joel Berry":
        points = points + 3
        print("Joel Berry scores! Great teamwork! \n")
    else:
        if choice1 == "throw the ball from half court":
            points = points + 10
            print(f"You made it! You are lucky, Coach Williams would not have been happy if you missed. {excited} \n")
        else:
            if choice1 == "foul Grayson Allen":
                points = points + 5
                print(f"Good foul. You stopped the clock. {clock}")
                print("Allen misses, you rebound and throw to Platek down the court, score!! \n")
    print(f"You scored { points } points { player }.")
    

def end() -> None:
    """This is the ending."""
    global player
    global points
    trophy = "\U0001F3C6"
    party_hat = "\U0001F973"
    ram = "\U0001F40F"
    print(f"Carolina Victory! {trophy} 82-78! Awesome job { player }.")
    print(f"What are you still doing here? Let's go to Franklin!! {party_hat} {ram} ")
    quit()
    

if __name__ == "__main__":
    main()   