#modules imported
import random
import time
import sys

#allows up to 100000 lottery rolls at a time
sys.setrecursionlimit(100000)

#starting stock value
stockval = 5

#version of game
version = "0.8"

#values such as cash, shares etc.
cash = 50
shares = 0
score = 0
golditems = 0

#achievements (currently not used)
pc = "locked"
achwhy = "locked"
achusb = "locked"

#print colours
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#the shop system (i should've used elif whooooops)
def shop():
    global score, cash, option, rng, achwhy, golditems, pc, achusb, stockval
    print(" ----------")
    prPurple("- welcome to the shop, check out some products!")
    prLightPurple("1 - score soda - fizzy, lemon flavoured ($25)")
    prLightPurple("2 - mystery breifcase - nobody knows how much cash is in it (1000 score)")
    prRed("3 - definitely not safe drink - what the hell even is this (250 score)")
    prYellow("4 - golden badge - will not confirm nor deny if this gives a luck boost (20000 score)")
    prYellow("5 - golden trophy - will not confirm nor deny if this gives a luck boost ($10000)")
    prRed("6 - suspicious potion - who knows what this does, drinking is not recommended (Free)")
    prLightPurple("7 - PC - plug usbs into this and get profit - ($1000)")
    prLightPurple("8 - green USB - plug this into a PC - ($250) [PC Required]")
    prLightPurple("9 - yellow USB - plug this into a PC - (1000 score) [PC Required]")
    prRed("10 - ?? USB - [description not found] - ($2) [PC Required]")
    prGreen("11 - blue USB - plug into a PC and have some good investments [PC Requried]")
    prPurple("- type 99 to leave!")
    prPurple("- you must have more cash than the product, it can't be equal bc ur lose by going bankrupt")
    print(" ----------")
    prGreen(f"Account Balance: ${cash}")
    prGreen(f"Score: {score}")
    print(" ----------")
    
    option = int(input(" pick: "))
    time.sleep(1)
    if option == 1 and cash >= 25:
        prPurple("- tastes amazing! ignore the fact that it has 888g of sugar")
        cash = cash - 25
        time.sleep(2)
        prYellow("Consuming...")
        rng = random.randint(1, 250)
        time.sleep(2)
        score = score + rng
        prGreen(f"You got {rng} score! Total Score: {score}")
        time.sleep(2)
        shop()
    else:
        if option == 2 and score >= 1000:
            score = score - 1000
            prPurple("- i will not confirm nor deny how much money is in this")
            time.sleep(2)
            prYellow("Opening...")
            rng = random.randint(50, 1000)
            time.sleep(3)
            cash = cash + rng
            prGreen(f"You got ${rng}! Total Cash: {cash}")
            time.sleep(2)
            shop()
        else:
            if option == 3 and score >= 250:
                score = score - 250
                prPurple("- why the hell do you want to buy this")
                time.sleep(2)
                prPurple("- sometimes i question your intelligence")
                time.sleep(2)
                prYellow("Consuming...")
                time.sleep(2)
                achwhy = "unlocked"
                prGreen("Achievement! - [why did you did that]")
                time.sleep(1)
                shop()
            else:
                if option == 4 and score >= 20000:
                    score = score - 20000
                    prPurple("- congrats, you deserve it!")
                    time.sleep(2)
                    prYellow("Harnessing Energy...")
                    time.sleep(3)
                    golditems = golditems + 1
                    prGreen(f"Golden Item Acquired - You now have {golditems} golden items!")
                    time.sleep(3)
                    shop()
                else:
                    if option == 5 and cash >= 10000:
                        cash = cash - 10000
                        prPurple("- congrats, you deserve it!")
                        time.sleep(2)
                        prYellow("Harnessing Energy...")
                        time.sleep(3)
                        golditems = golditems + 1
                        prGreen(f"Golden Item Acquired - You now have {golditems} golden items!")
                        time.sleep(3)
                        shop()
                    else:
                        if option == 6:
                            prPurple("- for legal reasons i am not allowed to give this to you")
                            time.sleep(2)
                            shop()
                        else:
                            if option == 7 and cash >= 1000:
                                prPurple("- you can plug USBs into this and generate money!")
                                cash = cash - 1000
                                time.sleep(2)
                                prYellow("Powering PC...")
                                time.sleep(3)
                                pc = "unlocked"
                                prGreen("PC is on and running! Try buying a USB!")
                                time.sleep(2)
                                shop()
                            else:
                                if option == 8 and pc == "unlocked" and cash >= 250:
                                    prPurple("- i think this USB gives score")
                                    cash = cash - 250
                                    time.sleep(2)
                                    prYellow("Plugging in USB...")
                                    rng = random.randint(10, 1000)
                                    time.sleep(2)
                                    score = score + rng
                                    prGreen(f"You got {rng} score from that! Total Cash: ${cash}.")
                                    time.sleep(2)
                                    shop()
                                else:
                                    if option == 9 and pc == "unlocked" and score >= 1000:
                                        prPurple("- pretty sure this USB gives cash")
                                        score = score - 1000
                                        time.sleep(2)
                                        prYellow("Plugging in USB...")
                                        rng = random.randint(10, 1000)
                                        time.sleep(2)
                                        cash = cash + rng
                                        prGreen(f"You got {rng} cash from that! Total Cash: ${cash}.")
                                        time.sleep(2)
                                        shop()
                                    else:
                                        if option == 10 and pc == "unlocked" and cash >= 2:
                                            prPurple("- i found this back in ohio, i guess you can have it")
                                            pc = "locked"
                                            cash = cash - 2
                                            time.sleep(2)
                                            prYellow("Plugging in USB...")
                                            time.sleep(3)
                                            prGreen("Plugged in USB.")
                                            time.sleep(3)
                                            prRed("Your PC is heating up!")
                                            time.sleep(2)
                                            prRed("There is smoke coming from your PC!")
                                            time.sleep(2)
                                            prRed("Your PC is on fire!")
                                            time.sleep(1)
                                            print(" ----------")
                                            time.sleep(2)
                                            prRed("You no longer have a PC.")
                                            prGreen("Achievement! [a suspicious USB]")
                                            achusb = "unlocked"
                                            time.sleep(3)
                                            shop()
                                        else:
                                            if option == 99:
                                                prPurple("- see you again!")
                                                time.sleep(4)
                                                back()
                                            else:
                                                if option == 11 and cash >= 1000 and pc == "unlocked":
                                                    prPurple("- this is probably illegal but who cares")
                                                    time.sleep(2)
                                                    cash = cash - 1000
                                                    prYellow("Plugging into PC...")
                                                    time.sleep(2)
                                                    prCyan(f"Old Stockval: {stockval}")
                                                    stockval = stockval + (random.randint(1,random.randint(20,300)))
                                                    prCyan(f"New Stockval: {stockval}")
                                                    time.sleep(3)
                                                    shop()


                                                else:
                                                    prPurple("- you can't buy that idiot")
                                                    time.sleep(2)
                                                    shop()
                                
#asking for the wager, this is used in most of the games
def wagask():
    prYellow("How much cash would you like to wager? (use numbers)")
    global wager
    wager = int(input(" Enter: "))
    if wager >= cash:
        if wager == cash:
            prPurple("- are you seriously wagering all of your money?")
            time.sleep(2)
            prPurple("- whatever thats your problem")
        else:
            print(" ----------")
            prRed("You don't have enough cash for that!")
            time.sleep(3)
            back()

#stock market
def stocks():
    global stockval, option, cash, shares
    if stockval < 0:
        stockval = 0
        stockval = round(random.uniform(1, 5), 2)
    else:
        stockval = stockval + round(random.uniform(-3, 3), 2)
    stockval = round(stockval, 2)
    print(" ----------")
    prCyan("Stock Market: ")
    prGreen(f"Value: ${stockval}")
    prLightPurple("1 - buy a share")
    prLightPurple("2 - sell a share")
    prLightPurple("99 - exit")
    print(" ----------")
    prGreen(f"Balance: ${cash}")
    prGreen(f"Shares: {shares}")
    print(" ----------")
    option = int(input(" choose what you want to do: "))
    if option == 1 and cash >= stockval:
        amount = int(input(" how many shares do you want to buy? "))
        afteramount = amount * stockval
        if cash >= afteramount:
            cash = cash - afteramount
            shares = shares + amount
            time.sleep(1)
            prGreen(f"You now own {shares} shares. (+{amount})")
            time.sleep(2)
            stocks()
        else:
            prRed("You don't have enough money for that!")
            time.sleep(2)
            stocks()
    else:
        if option == 2 and shares != 0:
            amount = int(input(" how many shares do you want to sell? "))
            if shares >= amount or shares == amount:
                afteramount = amount * stockval
                shares = shares - amount
                time.sleep(2)
                prGreen(f"You sold {amount} shares for ${afteramount}, you now have {shares} shares.")
                cash = cash + afteramount
                time.sleep(2)
                stocks()
            else:
                prRed("You don't have that many shares!")
                time.sleep(2)
                stocks()
        else:
            if option == 99:
                prYellow("Exiting...")
                time.sleep(2)
                back()

#asking how many tickets for lottery
def lotask():
    prYellow("How many tickets would you like to buy? (use numbers)")
    global wager, cash
    wager = int(input(" Enter: "))
    if wager >= cash:
        if wager == cash:
            prPurple("- are you seriously spending all of your money on lottery tickets?")
            time.sleep(2)
            prPurple("- thats not very smart but whatever ur choice")
            time.sleep(2)
            print(" ----------")
            cash = cash - wager
            prYellow("Reviewing Tickets...")
            print(" ----------")
            time.sleep(5)
            lottery()
        else:
            print(" ----------")
            prRed(f"You don't have enough cash for {wager} tickets!")
            time.sleep(3)
            back()
    cash = cash - wager
    print(" ----------")
    prYellow("Reviewing Tickets...")
    print(" ----------")
    lottery()

#lottery system
def lottery():
    global rng, wager, cash, score, lotlose, lotwin
    rng = random.randint(1,100)
    if random.randint(1,100) == rng:
        lotwin = lotwin + 1
        cash = cash + 100
        score = score + 100
        wager = wager - 1
        if wager == 0:
            back()
        else:
            lottery()
    else:
            wager = wager - 1
            lotlose = lotlose + 1
            score = score + 1
            if wager == 0:
                time.sleep(5)
                prYellow(f"All Tickets used, Total Won: {lotwin}, Total Lost: {lotlose}, Cash: {cash}")
                time.sleep(3)
                back()
            else:
                lottery()

#rock paper scissors game
def rps():
    prCyan("rock, paper or scissors? make your pick (cAsE sEnSiTiVe - if you do not use the correct text its an automatic loss)")
    global rng, multi, pick
    multi = 1
    rng = random.randint(1, 3)
    pick = input(" make your pick: ")
    if pick == "rock" and rng == 1:
        wagadd()
    else:
        if pick == "paper" and rng == 2:
            wagadd()
        else:
            if pick == "scissors" and rng == 3:
                wagadd()
            else:
                if rng == 1:
                    prRed("The opponent chose rock")
                    wagsub()
                else:
                    if rng == 2:
                        prRed("The opponent chose paper.")
                        wagsub()
                    else:
                        if rng == 3:
                            prRed("The opponent chose scissors.")
                            wagsub()

#slot machine system
def slots():
    prCyan("- beep boop i am a slot machine")
    global rng, multi, pick
    time.sleep(2)
    multi = 10
    slot1 = random.randint(1, 3)
    slot2 = random.randint(1, 3)
    slot3 = random.randint(1, 3)
    prYellow("Rolling...")
    time.sleep(1)
    prCyan("(x) (x) (x)")
    time.sleep(1)
    prCyan(f"({slot1}) (x) (x)")
    time.sleep(1)
    prCyan(f"({slot1}) ({slot2}) (x)")
    time.sleep(2)
    prCyan(f"({slot1}) ({slot2}) ({slot3})")
    time.sleep(3)
    if slot1 == 1 and slot2 == 1 and slot3 == 1:
        wagadd()
    else:
        if slot1 == 2 and slot2 == 2 and slot3 == 2:
            wagadd()
        else:
            if slot1 == 3 and slot2 == 3 and slot3 == 3:
                wagadd()
            else:
                wagsub()
    
#highlow game system
def hl():
    prCyan("Higher Lower, Try and guess the number from 1-20! (x1 of wager) (you get 4 chances)")
    global rng, multi, pick, hints
    multi = 1
    time.sleep(1)
    pick = int(input(" pick a number from 1-20: "))
    time.sleep(1)
    if rng == pick:
                prGreen(f"Congrats you guessed the number! It was {rng}!")
                time.sleep(2)
                wagadd()
    else:
        if hints == 0:
            prRed(f"You ran out of chances... The Number was {rng}")
            time.sleep(2)
            wagsub()
        else:
            if rng <= pick and hints != 0:
                prYellow("Lower")
                hints = hints - 1
                hl()
            else:
                if rng >= pick and hints != 0:
                    prYellow("Higher")
                    hints = hints - 1
                    hl()

#dice game system
def dice():
    prCyan("pick a number from 1-6, if the dice rolls that number you win x2 of your wager")
    global rng, multi, pick
    rng = random.randint(1, 6)
    pick = int(input(" pick idot: "))
    multi = 2
    time.sleep(1)
    prYellow("Rolling the dice...")
    time.sleep(3)
    if rng == pick:
        prGreen(f"The Dice Landed on {rng}, you picked {pick}!")
        print(" ----------")
        wagadd()
    else:
        prRed(f"The Dice Landed on {rng}, you picked {pick}.")
        print(" ----------")
        wagsub()

#menu   
def back():
    global stockval, cash

    if cash == 0:
        print(" ----------")
        prPurple("- looks like someone ran out of money")
        time.sleep(3)
        prPurple("- and thats why you don't gamble")
        time.sleep(2)
        print(" ----------")
        prRed(f"You went bankrupt! Score: {score}, Golden Items: {golditems}.")
        print(" ----------")
        time.sleep(3)
        prPurple("- get better lol")
        print(" ----------")
        exit()
    
    stockval = stockval + round(random.uniform(-3, 3), 2)
    cash = round(cash)

    print(" ----------")
    prPurple(f"rng hell - {version}")
    prLightPurple("1 - rock paper scissors (1/3) - x1 multi")
    prLightPurple("2 - roll the dice (1/6) - x2 multi")
    prLightPurple("3 - lottery - buy a lottery ticket ($1) and have a chance at winning $100 (1/100)")
    prPurple("4 - shop - head to the shop and buy some items")
    prLightPurple("5 - slots - use the slot machine - x10 multi")
    prLightPurple("6 - highlow - guess what the number is from 1-20 (4 chances) - x1 multi")
    prPurple("7 - stock market - invest your money and probably lose it all if you're unlucky")
    prGreen(f"Account Balance - ${cash}")
    prYellow(f"Score: {score}")
    print(" ----------")
    option = int(input(" pick what you want to do (use the numbers): "))
    print(" ----------")
    time.sleep(2)
    
    if option == 1:
        wagask()
        rps()
    else:
        if option == 2:
            wagask()
            dice()
        else:
            if option == 3:
                prCyan("Lottery Ticket - $1, Prize - $100!")
                global lotwin, lotlose
                lotwin = 0
                lotlose = 0
                lotask()
            else:
                if option == 4:
                    time.sleep(1)
                    shop()
                else:
                    if option == 5:
                        wagask()
                        slots()
                    else:
                        if option == 6:
                            global hints, rng
                            rng = random.randint(1,20)
                            hints = 3
                            wagask()
                            hl()
                        else:
                            if option == 7:
                                time.sleep(1)
                                stocks()
                            else:
                                prRed("error when choosing")
                                back()

#adding wager to balance on win
def wagadd():
    prGreen(f"You just won ${wager} (x{multi})!")
    global cash, score, aftermulti
    aftermulti = wager * multi
    cash = cash + aftermulti
    score = score + aftermulti
    time.sleep(3)
    back()

#subtracting wager from balance on loss
def wagsub():
    prRed(f"You just lost ${wager}!")
    global cash, score
    cash = cash - wager
    score = score + wager
    time.sleep(3)
    back()

#intro (totally real loading)
prYellow("Buying Stocks...")
time.sleep(random.uniform(0,1))
prYellow("Analysing Market...")
time.sleep(random.uniform(0,1))
prYellow("Spending Money...")
time.sleep(random.uniform(0,1))
prGreen("Loading Finished!")
print(" ----------")
prGreen("      ----- ")
prGreen("     |  .. |")
prGreen("     |  -- |")
prGreen("      ----- ")
prGreen(" periodic studios")
time.sleep(3)
back()