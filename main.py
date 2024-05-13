def viewPrev():
    file = None
    try:
        view = input("Would you like to access your old diary entry? (y/n): ")
        if view == "y": x = True
        else: x = False

        while x:
            file = input("When did you write the diary? (mmddyr): ")
            file = open(file)
            for i in file:
                print(i)

            view = input("Would you like to access your old diary entry? (y/n): ")
            if view == "y":
                x = True
            else:
                x = False
            file.close()

    except Exception as e:
        print(e)

def diary():
    viewPrev()
    file = None
    try:
        wantToWrite = input("Do you want to write a diary entry today? (y/n): ")
        if wantToWrite == "y": x = True
        else: x = False

        while x:
            file = input("Enter the date (format mmddyr): ")
            file = open(file, "w")

            writeWhat = input("What would you like to write?: ")
            file.write(writeWhat)

            wantToWrite = input("Do you want to write a diary entry today? (y/n): ")
            if wantToWrite == "y":
                x = True
            else:
                x = False
            file.close()

    except Exception as e:
        print(e)


diary()