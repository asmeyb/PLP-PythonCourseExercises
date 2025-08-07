firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))

print(f"The first number is: {firstNumber}")
print(f"The second number is: {secondNumber}")

print(f"The sum of {firstNumber} and {secondNumber} is: {firstNumber + secondNumber}")
print(f"The difference of {firstNumber} and {secondNumber} is: {firstNumber - secondNumber}")
print(f"The product of {firstNumber} and {secondNumber} is: {firstNumber * secondNumber}")
print(f"The quotient of {firstNumber} and {secondNumber} is: {firstNumber / secondNumber if secondNumber != 0 else 'undefined'}") 