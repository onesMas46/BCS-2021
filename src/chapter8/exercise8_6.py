numbers = list()
while True:
        num = input("Enter a number: ")
        if num == 'done':
            break
        else:
            num = float(num)
            numbers.append(num)
print("minimum: ", min(numbers))
print('maximum: ', max(numbers))


