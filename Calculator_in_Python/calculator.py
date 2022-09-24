def Calculator():
    def check_add():
        s1=int(input("Enter number to add = "))
        s2=int(input("Enter number to add = "))

        print(f"The addition of numbers is = {s1+s2}")
        print()

    def check_substraction():
        p1=int(input("Enter number to add = "))
        p2=int(input("Enter number to add = "))
        print(f"The {p1} subtracted by {p2} gives us result = {p1 - p2}")
        print()


    def check_multiply():
        s1=int(input("Enter number to add = "))
        s2=int(input("Enter number to add = "))
        print(f"The product of numbers is = {s1*s2}")
        print()


    def check_division():
        p1=int(input("Enter number to add = "))
        p2=int(input("Enter number to add = "))
        print(f"The {p1} divided by {p2} gives us result = {p1/p2}")
        print()


    def check_remainder():
        p1=int(input("Enter number to add = "))
        p2=int(input("Enter number to add = "))

        print(f"The {p1} divided by {p2} gives us remainder = {p1 % p2}")

    def print_details():
        print("Welcome to my Basic1 Calculator")
        print("1.Press 1 to check addition of numbers")
        print("2.Press 2 to check substraction of numbers")
        print("3.Press 3 to check multiplication of numbers")
        print("4.Press 4 to check division of numbers")
        print("5.Press 5 to check remainder of numbers")

        choice=int(input("Enter the choice = "))
        return choice

    while True:
        choice=print_details()
        if choice==1:
            check_add()
        elif choice==2:
            check_substraction()
        elif choice==3:
            check_multiply()
        elif choice==4:
            check_division()
        elif choice==5:
            check_remainder()
        else:
            break

Calculator()

