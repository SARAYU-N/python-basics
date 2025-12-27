while(1):
    print("\n****Calculator***\n")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    a=int(input("enter number a:"))
    b=int(input("enter number b:"))
    print("enter choice(1-4):")
    choice=int(input())
    match choice:
        case 1:
            print(a,"+",b,"=",a+b)
        
        case 2:
            print(a,"-",b,"=",a-b)
        
        case 3:
            print(a,"*",b,"=",a*b)
        
        case 4:
            if(b!=0):
                print(a,"%",b,"=",a/b)
            else:
                print("can't divide by zero!")   
    if(choice>4):
        print("invalid choice") 
    c=int(input("want to continue?(1/0):"))
    if(not c):
        print("ending calculator!")
        break




        
        
    

    

