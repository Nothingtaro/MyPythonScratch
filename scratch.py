num = int(input("Enter a number: "))

if num > 1:  
  for n in range(2, num+1):
    if num%n == 0:
      prime = False 
      
  if prime:
    print(f"{num} is not a prime number.")
  else:
    print(f"{num} is a prime number.")
else:
  raise ValueError("Your input is wrong. Try again.")

    
