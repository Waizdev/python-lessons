# Conditionals – Practice Questions
# Question:1

try:
    a = int(input(f"enter your number :"))
    if a % 2 == 0:
        print(f"given number \"{a}\" is even")
    else:
        print(f"given number \"{a}\" is odd")
except:
    print(f"invalid input")
print("\n")
# Question:2

age = int(input(f"enter your age :"))
if age <= 13:
    print(f"you are a child")
elif age > 13 and age < 17:
    print(f"you are a teenager")
elif age > 18:
    print(f"you are an adult")
else:
    print("invalid age!")
print("\n")
# Question:3

x = int(input(f"enter number 1 :"))
y = int(input(f"enter number 2 :"))
if x > y:
    print("first number is greater!")
    print(f"{x} is greater than {y}")
elif x == y:
    print("given numbers are equal!")
    print(f"{x} is equal to {y}")
else:
    print("second number is greater!")
    print(f"{y} is greater than {x}")
print("\n")
# Question:4

alpha = input("enter an alphabet :")
if alpha.lower() == 'a':
    print(f"entered alphabet is vowel")
elif alpha.lower() == 'e':
    print(f"entered alphabet is vowel")
elif alpha.lower() == 'i':
    print(f"entered alphabet is vowel")
elif alpha.lower() == 'o':
    print(f"entered alphabet is vowel")
elif alpha.lower() == 'u':
    print(f"entered alphabet is vowel")
else:
    print("invalid input")

    
    
