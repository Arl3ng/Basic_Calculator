print("CALCULATOR")
print("+")
print("-")
print("*")
print("/")
operator = input("Enter your operator: ")
nums = [0,0]
j = 5
     
while j>=0 :
  if operator == "+" :
   for i in range(0,2):
    nums[i] = float(input("Enter number"+ " " + str(i+1)+": "))
   result = (nums[0])+(nums[1])
   print("Your result is :" + str(result)) 
   break

  elif operator == "-" :
    for i in range(0,2):
     nums[i] = float(input("Enter number"+ " " + str(i+1)+": "))
    result = nums[0]-nums[1] 
    print("Your result is :" + str(result)) 
    break

  elif operator == "*" :
    for i in range(0,2):
     nums[i] = float(input("Enter number"+ " " + str(i+1)+": "))
    result = nums[0]*nums[1] 
    print("Your result is :" + str(result))
    break 

  elif operator == "/" :
    for i in range(0,2):
     nums[i] = float(input("Enter number"+ " " + str(i+1)+": "))
    result = nums[0]/nums[1] 
    print("Your result is : " + str(result)) 
    break



  else:
   print("Tries left" + str(j))
   operator = input("You have entered an wrong operator please try again: ")
   

   j = j - 1


