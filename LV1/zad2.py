while True:
    try:
        grade = float(input("Input the grade: "))
    except:
        print("The input has to be a float!")
    if grade >= 0.0 and grade <= 1.0:
        break

if grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")