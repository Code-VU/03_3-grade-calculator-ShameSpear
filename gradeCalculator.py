def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        hrs = float(input("Enter score:"))
    except ValueError:
        print("Bad score")
        return
    if hrs >= 1:
        print("Bad score")
        return
    if hrs >= 0.9:
        print0("A")
    elif hrs >= 0.8:
        print("B")
    elif hrs >= 0.7:
        print("C")
    elif hrs >= 0.6:
        print("D")
    elif hrs < 0.6:
        print("F")    
    # end assignment

#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F    

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
