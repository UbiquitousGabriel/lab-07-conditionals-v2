num1 = input("Please provide your first number.")
num2 = input("Please provide your second number.")
operation = input("What kind of operation would you like to do? mul, div, or mod?")
answer = ""
if (operation == "mul"):
    answer = (float(num1)*float(num2));

elif (operation == "div"):
    answer = (float(num1)/float(num2));

elif (operation == "mod"):
    answer = (float(num1)%float(num2));

else:
    answer = ("Please print a valid operation.")

print(answer)
