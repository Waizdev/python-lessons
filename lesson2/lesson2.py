"""conditionals"""
#these allows user to make decison as per required by the problem or given statement 

#understanding of if elif and else
age = 18
if age >= 18:
    print("You're an adult.")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")

#understanding of while
count = 0
while count < 5:
    print("Count is", count)
    count += 1
#understanding of for

for i in range(5):
    print("i is", i)

#mini project
# Guessing game
secret = 7

guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")

#quick exercise
age = int(input(f"enter your age :"))

if  age >= 18:
    print(f"you can vote")
else:
    print(f"you are too yound cant vote")

#break and continue

# break: stops the loop
for i in range(10):
    if i == 5:
        break
    print("Break Loop i:", i)

# continue: skips this loop and continues
for i in range(5):
    if i == 2:
        continue
    print("Continue Loop i:", i)

