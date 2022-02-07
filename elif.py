print("Enter the marks for 5 subjects")
subject_1 =int(input("Enter the marks for subject 1:"))
subject_2 =int(input("Enter the marks for subject 2:"))
subject_3 =int(input("Enter the marks for subject 3:"))
subject_4 =int(input("Enter the marks for subject 4:"))
subject_5 =int(input("Enter the marks for subject 5:"))

total = subject_5 +subject_4+subject_3+subject_2+subject_1
mean= total/5
if mean >=70 and mean <=100:
    print("Excellent")
elif mean>=60 and mean <=69:
    print("Good job")
elif mean>=50 and mean <=59:
    print("fair")
elif mean>=40 and mean <=49:
    print("tia bidii sana")
else:
    print("total score is",total)
    print("the total mean is", mean)
    print("you failed terribly")


