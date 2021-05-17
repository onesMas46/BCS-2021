def desp():
    print('=' * 50)
    print('Customer code: ', code)
    print('Beggening meter reading: ',ireading)
    print('Ending meter reading: ',freading)
    print('Gallons of water used: ',volwater)
    print('Amount billed: $',round(amount, 2))
    print('*' * 50)
while True:
    code = input('Enter customer code: ')
    code = code.upper()
    if code == "C" or code == "R" or code == "I":
            Beggening = input("Enter begenning meter reading: ")
            ending = input("Enter ending meter reading: ")
            if len(Beggening) <= 9 and len(ending) <= 9:
                ireading = int(Beggening) 
                freading = int(ending)
                volwater = (abs(freading - ireading)) * 0.1
                if code == "R":
                    amount = ((5 + 0.0005) *  volwater)
                    desp()
                elif code == "C":
                    if volwater > 4_000_000:
                        amount = ((1_000 * 4_000_000) + (0.00025 * (volwater - 4_000_000)))
                        desp()
                    else:
                        amount = (1_000 * volwater) 
                        desp()
                else:
                    if volwater > 10_000_000:
                        amount = (2_000 * 10_000_000) + ((volwater - 10_000_000) * 0.00025) 
                        desp()  
                    elif 4_000_000 < volwater <= 10_000_000:
                        amount = volwater * 2_000
                        desp()
                    else:
                        amount = 1_000 * volwater
                        desp()
            else:
                print("invalid input of meter readings!!")  
                continue         
    else:
        print("Invalid input of customer code")  