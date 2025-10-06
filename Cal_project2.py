def add(a,b):
    answer = a + b 
    print(str(a) + '+'+str(b) + '=' + str(answer))
def sub(a,b):
    answer = a - b 
    print(str(a) + '-'+str(b) + '=' + str(answer))
def mult(a,b):
    answer = a * b 
    print(str(a) + '*'+str(b) + '=' + str(answer))
def div(a,b):
    answer = a / b 
    print(str(a) + '/'+str(b) + '=' + str(answer))
def mod(a,b):
    answer = a % b 
    print(str(a) + '% '+str(b) + '=' + str(answer))
while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Modulus')
    print('F. Exit')

    choice = input('Enter your Choice: ')
    
    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        add(a , b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        sub(a , b)
    elif choice == 'c' or choice == 'C':
        print('Multiplicaion')
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        mult(a , b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        div(a , b)
    elif choice == 'e' or choice == 'e':
        print('Modulus')
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        mod(a , b)
    elif choice == 'f' or choice == 'F':
        print('Exit()')
    
    
