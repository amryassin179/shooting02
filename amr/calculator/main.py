while True:
  #input first number
  while True:
      try:
        first_numer = float(input("enter first number: "))
        break
      except ValueError:
        print("please enter a numaric number")
  
    #input operation type
  while True:
    operation = input("enter operation type: ")
    if operation in("+","-","*","/"):
      break
    else:  
      print("wront operation please enter -,+,*,/")
    
    #input second number
  while True:
    try:
      second_number = float(input("enter second number: ") )
      if second_number==  0 and operation=="/":
        raise ZeroDivisionError
      break
    except ValueError:
       print("please enter a numaric number: ")
        
    except ZeroDivisionError:
       print("can not divide by zero please enter another number")
       
  if operation== "+":
    resault=print(first_numer+second_number)
  elif operation=="-":
    resault=print(first_numer-second_number )
  elif operation=="*":
    resault=print(first_numer*second_number)
  elif operation=="/":
    resault=print(first_numer/second_number)
  else:
    print("wrong opertion please enter +,-,/,*")  
   
  
  repeat= input("do you want to do another operation? yes/no: ")
  if repeat =="no":
    print("thanks for using my calculator")
    break 
      
  
      
    
print("program exited") 