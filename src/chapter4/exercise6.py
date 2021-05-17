hours = int(input('Enter hours: '))
rate = float(input('Enter rate: '))
def computepay(hours rate):
    if hours > 40:
        pay = ((40 * rate) + (((hours - 40) * rate) * 1.5))
        print('pay: ', pay)
    else:
        pay = hours * rate
        print('pay: ', pay)
computepay(hours,rate)            