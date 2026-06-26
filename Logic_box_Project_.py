print("Welcome to the  Pattern Generator and  Number Analyzer!")

while True:
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")
    x = int(input("Enter your Choice: "))
    
    match x:
        case 1:
            num = int(input("Enter the Number for raw: "))
            for i in range(1,num+1):
                print("*" * i)
        
        case 2:
            a = int(input("Enter Starting Number: "))
            b = int(input("Enter Ending Number: "))
            if a <= -1 or b <= -1:
                print("Please Enter positive Numbers of a & b ")
                continue
            sum = 0
            for i in range(a,b+1):
                sum += i
                
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                
            print(f"Sum of all numbers from {a} to {b} is : {sum} ")
            
        case 3:
            print("Exiting the program. Goodbye!")
            break
            
        case _:
            print("Invalid Input, Please try again.")
            break
                

   
        