try:
    print("## CALCULATOR ##\n")
    
    First=(int(input("enter your first number : ")))

   
    
    Second=(int(input("enter your Second number : ")))


    op=(input("Choose Your Operation : + , - , * , / , ALL or all : "))


    


    if op==("+"):
        print(First ,"+" ,Second,"=" ,First+Second)
      
    elif     op=="ALL" or op== "all":
      print(First, "+", Second, "=", First + Second)
      print(First, "-", Second, "=", First - Second)
      print(First, "*", Second, "=", First * Second)
      print(First, "/", Second, "=", First / Second)
        



      
    elif     op==("-"):
        print(First, "-",Second ,"=" ,First-Second)
      
    elif     op==("*"):
        print(First,"*",Second,"=", First*Second)
      
    elif      op==("/"):
        print(First, "/",Second,"=", First/Second)
      
    else:
        print("\n#-Invalid Operation-# \nValid Operations are : + , - , * , / , ALL or all  ")

except ValueError:
    print("\n#-Only Numbers Please-#\n")

finally:
    print("\n---->Code Executed Successfully<----")

