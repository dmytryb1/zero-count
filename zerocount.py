N = int(input('How many numbers? '))
list_numbers = []
zero_count = 0

for i in range(N):
    num  = int(input('Enter a number '))
    list_numbers.append(num)
    N = N - 1
    print(list_numbers)
    if num == 0:
        zero_count += 1
        if N == 0:
            print('The final amount of zeros is: ' + str(zero_count))
        else:
            print('The current amount of 0s is: ' + str(zero_count))



#count = 0
#i = input("numbers")
#
#for i in N:
#    i = int(input('Type a number'))
#    if i == 0:
#        count += 1