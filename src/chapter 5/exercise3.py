import math
def disp():
    print("    The machine contains:")
    print(dimes,"dimes")
    print(quarters,"quarters")
    print(nickles,"nickles")
    print(one_dollar,"one dollar notes")
    print(five_dollar,"five dollar notes")
print("=============== Restart ========================")
print("Welcome to the vending machine the change maker")
print("*" * 40)
dimes = 25
quarters = 25
nickles = 25
one_dollar = 0
five_dollar = 0
disp()
while True:
    a = input("Enter the purchase price in form (xx.xx) or 'q' to quit: ")
    if a.upper() == "Q":
        disp()
        quit()
    else:
        value = round(float(a) * 100)
        if value % 5 == 0:
            dollars = int(value / 100)
            cents = value - (dollars * 100)
            print("  Menu for deposits  ")
            print("'q' - deposit a quarter")
            print("'n' - deposit a nickle")
            print("'d' - deposit a dime")
            print("'o' - deposit a one dollar bill")
            print("'f' - deposit a five dollar bill")
            print("'c' - cancel the deposit ")
            while True:
                print("payment due: " + str(dollars) + "dollars and " + str(cents) + "cents")
                choice = input("indicate your purchase: ")
                if choice == "n":
                    n = math.trunc(cents / 5)
                    cents = cents - (n * 5)
                    nickles = nickles + n
                elif choice == "q":
                    q = math.trunc(cents / 25)
                    cents = cents - (q * 25)
                    quarters = quarters + q
                elif choice == "d":
                    d = math.trunc(cents / 10)
                    dimes = dimes + d
                    cents = cents - (d * 10)
                elif choice == "o":
                    one_dollar = one_dollar + 1
                    dollars = dollars - 1
                elif choice == "f":
                    five_dollar = five_dollar + 5
                    dollars + dollars -5
                elif choice == "c":
                    disp()
                    quit()
                else:
                    print("Invalid purchase choice" + choice)
        else:
            print("Invalid purchase: price must be a non negative multiple of 5.")