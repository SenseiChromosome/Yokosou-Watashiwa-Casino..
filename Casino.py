import time
import sys
import random

#ASCII Art for my game
print("""   

                          ____          _             
                         / ___|__ _ ___(_)_ __   ___  
                        | |   / _` / __| | '_ \ / _ \ 
                        | |__| (_| \__ \ | | | | (_) |
                         \____\__,_|___/_|_| |_|\___/ 

""")

time.sleep(1)
print("Yokosou!")         #Welcoming to the casio
time.sleep(1)
print("This is my Casino.")

while True:     #Asking if they'd like to play the games within the casino
    time.sleep(1)
    answer = input("Would you like to step in and try play the games...? (y/n) ")

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
print("[3] Roulette")               #The games that I offer within the casino
print("[2] Poker",end="     ")
print("[4] Slot Machines")
print("")
casino_game = input("Please enter the game you'd like to play: ")
print("")

while True:
    time.sleep(1)               #Game - BlackJack
    if casino_game == "1":
        print("Ah, So you've selected BlackJack. This could be a lot of fun...")
        print("")
        time.sleep(1)
        print("Would you like a Tutorial?: ")       #asking if they'd like a tutorial for the game BlackJack
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

time.sleep(1)

card_value = {
  1:1,
  2:2,
  3:3,
  4:4,
  5:5,
  6:6,
  7:7,
  8:8,
  9:9,
  10:10,
  "Jack":10,
  "Queen":10,
  "King":10,
  "Ace":11
}

while True:
    bust = 22
    dealers_cards1 = [5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    dealers_cards2 = [10,"Jack","Queen","King","Ace"]
    cards =[2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    random_card1 = random.choice(cards)
    random_card2 = random.choice(cards)
    random_card3 = random.choice(cards)
    random_card4 = random.choice(cards)
    random_dealers_cards1 = random.choice(dealers_cards1)
    random_dealers_cards2 = random.choice(dealers_cards2)
    dealers_card_total = card_value[random_dealers_cards1] + card_value[random_dealers_cards2]
    players_card_total = card_value[random_card1] + card_value[random_card2]
    choice_hit = False
    #choice_hit2 = False

    print("")
    print("-------------------------------------------------------------------")
    print("")
    print("DEALERS CARDS: ")
    print("")
    print(f'    [{random_dealers_cards1}][?]     ')
    print(""
        "")
    print("YOUR CARDS: ")
    print("")
    print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]" + "       " + "Total: " + str(players_card_total)) #+ "[" + str(random_card3) + "]")
    time.sleep(1)
    print("")
    print(f"What's your next move?")
    print("")
    choice_bj = input("[Hit] [Stand] [Split] [Double Down]: ")

    """
    if random_card1 == card_value:
    random_card1 += random_card_total
    print(random_card_total)
    """

    if choice_bj == "hit":
        #choice_hit2 = True
        players_card_total = card_value[random_card1] + card_value[random_card2] + card_value[random_card3]
        if players_card_total >= bust:
            print(f"\nYou've gone Bust!")
            print(f"Your total was {players_card_total}!")
            #sys.exit()
        choice_hit = True
        if players_card_total < bust:
            print("")
            print("\nDEALERS CARDS: ")
            print("")
            print(f'    [{random_dealers_cards1}][{random_dealers_cards2}]     ')
            print("")
            print("YOUR CARDS: ")
            print("")
            print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]" + "[" + str(random_card3) + "]" + "       " + "Total: " + str(players_card_total))
            time.sleep(1)
            print("")
            print(f"What's your next move? {players_card_total}")
            print("")
            choice_bj = input("[Hit] [Stand] [Split] [Double Down]: ")
            if choice_bj == "stand":
                #print("")
                print("\nDEALERS CARDS: ")
                print("")
                print("    [" + str(random_dealers_cards1) + "]" "[" + str(random_dealers_cards2) + "]     ")
                print("")
                print("YOUR CARDS: ")
                print("")
                print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]" + "[" + str(random_card3) + "]")
                time.sleep(1)
                if dealers_card_total > players_card_total:
                    print(f"\nYou lost!")
                else: 
                    print(f"\nYou Won!")
                print("-------------------------------------------------------------------")
                """
            if choice_bj == "hit" and choice_hit == True:
                 choice_hit2 = True
                 players_card_total = card_value[random_card1] + card_value[random_card2] + card_value[random_card3] + card_value[random_card4]
            if players_card_total >= bust:
                    print(f"\nYou've gone Bust!")
                    print(f"Your total was {players_card_total}!")
                    #sys.exit()
            choice_hit = True
            
            if players_card_total < bust:
                    print("")
                    print("\nDEALERS CARDS: ")
                    print("")
                    print(f'    [{random_dealers_cards1}][{random_dealers_cards2}]     ')
                    print("")
                    print("YOUR CARDS: ")
                    print("")
                    print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]" + "[" + str(random_card3) + "]" + "[" + str(random_card4) + "]"  +     " Total: " + str(players_card_total))
                    time.sleep(1)
                    print("")
                    print(f"What's your next move? {players_card_total}")
                    print("")
                    choice_bj = input("[Hit] [Stand] [Split] [Double Down]: ")
                    if choice_bj == "stand" and choice_hit2 == True:
                        print("\nDEALERS CARDS: ")
                        print("")
                        print("    [" + str(random_dealers_cards1) + "]" "[" + str(random_dealers_cards2) + "]     ")
                        print("")
                        print("YOUR CARDS: ")
                        print("")
                        print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]" + "[" + str(random_card3) + "]" + "[" + str(random_card4) + "]"  +     " Total: " + str(players_card_total))
                        time.sleep(1)
                        if dealers_card_total > players_card_total:
                            print(f"\nYou lost!")
                        else: 
                            print(f"\nYou Won!")
                        print("-------------------------------------------------------------------")
                        """
                        

                


    if choice_bj == "stand" and choice_hit == False:
        print("")
        print("DEALERS CARDS: ")
        print("")
        print("    [" + str(random_dealers_cards1) + "]" "[" + str(random_dealers_cards2) + "]     ")
        print("")
        print("YOUR CARDS: ")
        print("")
        print("    [" + str(random_card1) + "]" + "[" + str(random_card2) + "]") #+ "[" + str(random_card3) + "]")
        if dealers_card_total > players_card_total:
            print(f"\nYou lost!")
        else: 
             print(f"\nYou Won!")
        print("-------------------------------------------------------------------")
    
        time.sleep(1)
        print("")



    #random_card = random.choices(cards, k=3)
    #print(random_card)
