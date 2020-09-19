
import random

print("Winning rules of the game-\n"
        +"Rock vs Paper->Paper wins \n"
        + "Rock vs Scissor->Rock wins \n"
        +"paper vs Scissor->Scissor wins \n")

while(True):
    print("Enter your choice- \n 1.Rock \n 2.Paper \n 3.Scissors\n")

    choice=int(input("Your choice:"))

    while choice>3 or choice<1:
        choice=int(input("Enter valid choice:"))

    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    else:
        choice_name="Scissors"

    #print user choice
    print("Your choice is : "+choice_name)

    print("\n <<<<< Now it's computer's turn >>>>")

    #random number chosen by computer
    comp_choice=random.randint(1,3)

    
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissors"

    print("\n Computer's choice is :" + comp_choice_name)

    #Condition for winning
    if((choice==1 and comp_choice==2) or (comp_choice==1 and choice==2)):
        
        result="Paper"
    
    elif((choice==1 and comp_choice==3)or (comp_choice==1 and choice==3)):
        
        result="Rock"

    elif((choice==2 and comp_choice==3)or (comp_choice==3 and choice==2)):
     
        result="Scissors"
    else:
        result=""

    #Printing the winner
    if result == choice_name:
        print("<<< CONGRATULATIONS YOU WON! >>>")

    elif result == comp_choice_name:
        print("<<< COMPUTER WINS! >>>")

    else :
        print("<<< TIE GAME- NO WINNER! >>>" )
        
    print("\nDo you want to play again? (Y/N)")
    ans=input()

    if ans=="n" or ans=="N":
        break

print("\n Thanks for playing :)")

    #END