
print("\nHere are your probabilities before your game starts.\n")
print("Royal Flush: 0.000154%")
print("Straight Flush: 0.000139%")
print("Four of a kind: 0.0240%")
print("Full House: 0.1441%")
print("Flush: 0.19654%")
print("Straight: 0.3925%")
print("Three of a kind: 2.1128%")
print("2 pair: 4.7539%")
print("One pair: 42.2569%")
print("No pair: 50.1%")

print("\nIf you type a face card, please type in a number. Example: Ace = 1, Jack = 11, Queen = 12\n")


firstCardsuit = input("\nWhat is the suit of your first card? :\n")

firstCardnum = int(input("\nWhat is the number or face of your first card? :\n"))

secondCardsuit = input("\nWhat is the suit of your second card? :\n")

secondCardnum = int(input("\nWhat is the number or face of your second card?:\n"))


firstCardsuit = firstCardsuit.lower()
secondCardsuit = secondCardsuit.lower()




def royalflushpreflop():
  print("\nRoyal Flush:<1%")



def straightflushpreflop():
  if(firstCardnum - secondCardnum <= abs(5)):
    print("straightflush:<1%")
  else:
    print("straightflush:<1%")

def fourofakindpreflop():
  if(firstCardnum == secondCardnum):
    print("fourofakind:8%")
  else:
   print("fourofakind:2%") 

def fullhousepreflop():
  if(firstCardnum == secondCardnum):
    print("fullhouse:10%")
  else:
    print("fullhouse:>1%")

def flush():
  if(firstCardsuit == secondCardsuit):
     print("Flush : 22%")
  else:
    print("flush: <1%")
      
def threeofakind():
  if(firstCardnum==secondCardnum):
    print("threeofakind:12%")
  else:
    print("threeofakind:1%")


def twopairpreflop():
  if(firstCardnum==secondCardnum):
    print("twopair:42%")
  else:
    print("twopair:24%")

def highcardpreflop():
  if(firstCardnum == 1 or secondCardnum ==1):
    print(" High Card: 100%")
  elif(firstCardnum == 13 or secondCardnum == 13):
    print("High Card: 92.3%")
  elif(firstCardnum ==12or secondCardnum == 12):
    print("High Card: 84.6% ")
  elif(firstCardnum ==12 or secondCardnum == 12):
    print("High Card: 76.9%")
  elif(firstCardnum == 10 or secondCardnum == 10):
    print("High Card: 69.2%")
  elif(firstCardnum == 9  or secondCardnum == 9):
    print("High Card: 61.5%")
  elif(firstCardnum == 8 or secondCardnum == 8):
    print("High Card: 53.8%")
  elif(firstCardnum == 7 or secondCardnum == 7):
    print("High Card: 46.1%")
  elif(firstCardnum == 6 or secondCardnum == 6):
    print("High Card: 38.5%")
  elif(firstCardnum == 5 or secondCardnum == 5):
    print("High Card: 30.7%")
  elif(firstCardnum == 4 or secondCardnum == 4):
    print("High Card: 23.1%")
  elif(firstCardnum == 3 or secondCardnum == 3):
    print("High Card: 15.4%")
  else:
      print("High Card: 0%")
  


def pairpreflop():
  if(firstCardnum == secondCardnum):
    print("Pair: 100%")
  else:
    print("pair:50%")


      


def preflop():
  royalflushpreflop()
  straightflushpreflop()
  fourofakindpreflop()
  fullhousepreflop()
  flush()
  threeofakind()
  twopairpreflop()
  pairpreflop()
  highcardpreflop()

preflop()
#flop() or tab1
#turn()
#river
