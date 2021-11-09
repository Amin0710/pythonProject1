# Start
# The Main Menu
t = 0
while (t == 0):
    t = 1
    print('''
-----------------------------------------------------------------------------------------
The Innovation University of Australia (IUA) Grade System
-----------------------------------------------------------------------------------------
''')
# Taking The input of ID
sid = input('Please enter the student ID (6-digit number) :')
# checking if it is an integer or not
try:
    z = int(sid)
    # if a valid number or not
    if (z < 999999 and z > 100000):
        input("Please enter the student Name: ")  # taking input of name
    # do not need to read as we are not using the name later in this program
    else:
        print("INVALID input!!!  Try again with a valid input")

    print("Please enter all marks out of 100.")
    # Taking The input of  Ass1
    a1 = input('Please enter the marks for Assignment 1:')
    # checking if it is an integer or not
    try:
        x = int(a1)
        # if a valid number or not
        if (x <= 100 and x >= 0):
            a2 = input("Please enter the marks for Assignment 2: ")  # Taking The input of  Ass2
        else:
            print("INVALID input!!!  Try again with a valid input")
        try:  # checking if it is an integer or not
            y = int(a2)
            # if a valid number or not
            if (y <= 100 and y >= 0):
                final = input("Please enter the marks for Final Exam: ")  # Taking The input of  Final
            else:
                print("INVALID input!!!  Try again with a valid input")
                try:  # checking if it is an integer or not
                    f = int(final)
                    # if a valid number or not
                    if (f <= 100 and f > 0):
                        print(" Thank You! ")
                    else:
                        print("INVALID input!!!  Try again with a valid input")

                    wa1 = float(x * 20 / 100)
                    wa2 = float(y * 30 / 100)
                    wass = float(wa1 + wa2)
                    wf = float(f / 100 * 50)
                    ws = float(wass + wf)
                    if (ws > 0 and ws <= 50):
                        b = float(0.0)
                    elif (ws > 50 and ws <= 70):
                        b = float((ws - 50.0) / 10.0)
                    elif (ws > 70 and ws <= 90):
                        b = float(((ws - 70.0) * 15.0 / 100.0) + 2.0)
                    else:
                        b = float(((ws - 90.0) / 5.0) + 5.0)

                    mwb = float(ws + b)
                    b = format(b, '.1f')
                    mwb = format(mwb, '.1f')

                    if (mwb > 100):
                        mwb = 100.0
                    else:
                        mwb = mwb
                    print("Weighted mark for Assignment 1: ", wa1)
                    print("Weighted mark for Assignment 2: ", wa2)
                    print("Total weighted mark of the assignments: ", wass)
                    print(" ")

                    print("Weighted mark for the Final Exam: ", wf)
                    print("Total weighted mark for the subject: ", ws)
                    print(" ")

                    print("Bonus mark: ", b)
                    print("Total mark with bonus: ", mwb)
                    print(" ")

                    print("Do you want to enter marks for another student (Y/N)? ")
                    key = input()
                    if (key == Y):
                        t = 0
                    else:
                        print("INVALID input!!!  Try again with a valid input1")






                # if f not a integer
                except ValueError:
                    print("INVALID input!!!  Try again with a valid input2")
        # if a2 not a integer
        except ValueError:
            print("INVALID input!!!  Try again with a valid input3")
    # if a1 not a integer
    except ValueError:
        print("INVALID input!!!  Try again with a valid input4")
# if ID not a integer
except ValueError:
    print("INVALID input!!!  Try again with a valid input5")
