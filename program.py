# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32
for i in range(32):
  myNumber = i+1
  result = myNumber
  if result % 15 == 0:
    result = 'fizzbuzz'
  elif myNumber % 3 == 0:
    result = 'fizz'
  elif myNumber % 5 == 0:
    result = 'buzz'
  print(result)

