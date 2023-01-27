def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        score = float(input("Enter Score:"))
        if score > 1.0:
            grade = "Bad score"
        elif score >= 0.9 and score <= 1.0:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score > 0.6:
            grade = "D"
        elif score <= 0.6 and score >= 0:
            grade = "F" 
        else:
            grade = "Bad score"
    except:
        grade = "Bad score"

    print(grade)
    
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
