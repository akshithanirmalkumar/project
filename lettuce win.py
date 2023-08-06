print("welcome to the quiz game")

competitor = input("do you want to play the game?")

if competitor.lower() != "yes":
    quit()

print("lets start the game") 

question= input("what did second generation computers use for circuitry?")
if question.lower() == "transistors":
    print("correct")

else:
    print("incorrect")    


question= input("what house was harry potter sorted into?") 
if question.lower() == "gryffindor":
    print("correct")

else:
    print("incorrect") 


question= input("which character goes missing in the first season of stranger things?")
if question.lower() == "will byers":
    print("correct")

else:
    print("incorrect")


question= input("how many rings make up the olympic games symbol?")
if question.lower() == "five":
    print("correct")

else:
    print("incorrect")


question= input("which word in the dictionary is spelled incorrectly?")
if question.lower() == "incorrectly":
    print("correct")

else:
    print("incorrect") 


question= input("in which year did the band One Direction was formed?")
if question.lower() == "2010":
    print("correct")

else:
    print("incorrect")

 
