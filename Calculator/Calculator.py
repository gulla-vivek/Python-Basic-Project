print ('Hello')
value1 = int(input('Please enter a value'))
value2 = int(input('Please enter a value'))


print('Which operation would yu like to do')
print('1.Addition')
print('2. Subtraction')
print('3.Multiplication')
print('4.Division')

choice = input('Enter a choice btw 1-4 :')

if choice =='1':
    print('Result :' ,value1+value2)
elif choice == '2':
    print('Result :',value1 -value2)
elif choice == '3' :

        print('Result :', value1 * value2)

elif choice == '4':
    if value2 !=0:
        print('Result :' ,value1/value2)
    else:
        print('Division by zero is not allowed')

else:
    print('Invalid choice')