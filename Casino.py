import time
import sys

time.sleep(1)
print("Yokosou!")
time.sleep(1)
print("This is my Casino.")

while True:
    time.sleep(1)
    answer = input("Would you like to step in and try play the games...? ")

    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        time.sleep(1)
        print("Well then, I see you've made up your mind")
        time.sleep(1)
        print("This may not be easy...")
        break
    elif answer == "No" or answer == "no" or answer == "N" or answer == "n":
        time.sleep(1)
        print("")
        print("Wise Choice...")
        sys.exit()
    else:
        time.sleep(1)
        print("")
        print("Let me ask you again..")

print("")
print("[1] BlackJack",end=" ")
print("[3] Roulette")
print("[2] Poker",end="     ")
print("[4] Slot Machines")
print("")
casino_game = input("Please enter the game you'd like to play: ")
print("")

while True:
    time.sleep(1)
    if casino_game == "1":
        print("Ah, So you've selected BlackJack. This could be a lot of fun...")
        print("")
        time.sleep(1)
        print("Would you like a Tutorial?: ")
        tutorial_bj = input("      [Yes] [No]: ")
        #print("")
        if tutorial_bj == "Yes" or tutorial_bj == "yes" or tutorial_bj == "Y" or tutorial_bj == "y":
            time.sleep(1)
            print("")
            print("OBJECT OF THE GAME:")
            print("Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.")
            print("")
            print("CARD VALUE/SCORING:")
            print("It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.")
            print("")
            print("HOW TO PLAY:")
            print("There are 4 options you have when you recieve your cards. These consist of: Hit, Stand, Split, Double Down.")
            print("Hit - you're dealt one additional card.")
            print("")
            print("Stand - You keep the cards you have.")
            print("")
            print("Split - To first qualify you'll need two of the same cards. Once achieved You'll receive two cards more, one for each of the cards you've originally been dealt, pay a side bet, and then start playing with two independent hands.")
            print("Both their bets and their payoffs are independent too.")
            print("")
            print("Double Down - You need to place an additional bet, after which you'll receive one card more to add to your original hand.")
        elif tutorial_bj == "No" or tutorial_bj == "no" or tutorial_bj == "N" or tutorial_bj == "n":
            time.sleep(1)
            print("")
            print("Well then lets get started!")
            break
