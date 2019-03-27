
#Solution using methods
r = open("Exercise_1_books.py")

with open("myfile1.txt", "w") as w:
    for line in r:
        w.write("Number: " + line)


#Solution using print() func
r2 = open("Exercise_1_roles.py")


with open("myfile2.txt", "w") as w2:
    for line in r2:
        print("Number: " + line, file = w2, end="")
