score = input("Enter Score: ")
Score = float(score)

if (1.0>=Score>=0.9):
    print("A")
elif (Score>=0.8):
    print("B")
elif (Score>=0.7):
    print("C")
elif (Score>=0.6):
    print("D")
elif (0.0<=Score<0.6):
    print("F")
else:
    print("Error")
