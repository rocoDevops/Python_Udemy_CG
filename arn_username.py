arn = "arn.aws.iam::123456789:user/cdebnath"
print (arn.split("/")[1]) #It will split the string into two parts.

text = "Python is awesome"
print (text.split(" ")[2])

name = "chandan"
print(name.upper())

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

data = "Chandan is DevOps"
substring = "is"
if substring in data:
    print(substring, "found in the data")

# Integer variables
num1 = 10
num2 = 5
# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)
# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)
# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)