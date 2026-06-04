a=int(input("enter a number between 1 to 10:"))
match a:
    case 1:
        print("you won a charger")
    case 2:
        print("you won a phone")
    case 3:
        print("you won a laptop")
    case _:
        print("you entered a number outside the range 1 to 10")