def adding_report(report = "T"):
    total = 0
    items = ""

    while True:
        intOrQ = input("Enter an integer or \"Q\" to quit the program")

        if intOrQ.upper().isdigit():
            items += intOrQ + "\n"
            total += int(intOrQ)
        elif intOrQ.upper().startswith("Q"):
            if report.upper() == "A":
                print("Items: \n" + items)
                print("Total \n" + str(total))
                break
            else:
                print("Total \n" + str(total))
                break
        else:
            print("\"" + intOrQ + "\" is invalid input")

print("Choose between two report types, \"All Items\" (A) or \"Total only\" (T)")


while True:
    x = input("Enter \"A\" or \"T\":")
    if x.upper() == "A":
        print("Report type A selected")
        adding_report(x)
        break
    elif x.upper() == "T":
        print("Report type T selected")
        adding_report(x)
        break
    else:
        print("Invalid input")