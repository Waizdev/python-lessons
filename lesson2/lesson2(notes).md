# ✅ Lesson 2: Conditional Statements & Loops

### 📌 Theory & Purpose

Real-world problems require logic: "if this happens, do that". This is where **conditions** come in.

Loops allow us to **repeat** actions efficiently, like printing messages or processing lists of items.

---

### 📘 Key Concepts

#### 🧾 Conditional Statements

```python
age = 17

if age >= 18:
    print("You can vote!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're too young to vote.")
```

**Structure**:
- `if`: Runs when condition is **True**
- `elif`: Else-if (another condition)
- `else`: Runs when no other condition matches

---

#### ⚖ Comparison Operators

| Operator | Meaning        |
|----------|----------------|
| `==`     | Equal          |
| `!=`     | Not Equal      |
| `>`      | Greater Than   |
| `<`      | Less Than      |
| `>=`     | Greater or Equal |
| `<=`     | Less or Equal  |

---

#### 🔐 Logical Operators

```python
x = 10

print(x > 5 and x < 20)   # True
print(x == 10 or x < 5)   # True
print(not x == 10)        # False
```

---

### 🔁 Loops in Python

#### 🔄 While Loop (runs until condition is false)
```python
i = 1
while i <= 5:
    print("Looping:", i)
    i += 1
```

#### 🔁 For Loop (runs over a sequence or range)
```python
for i in range(1, 6):  # 1 to 5
    print("Step:", i)
```

✅ `range(x, y)` goes from `x` to `y - 1`

---

### 🎮 Mini Project – Number Guessing Game

```python
secret = 7
guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
```

---

### 🧪 Practice Exercise
Build a program that:
- Asks the user for their age
- If they are 18 or older, prints "You can vote"
- Otherwise prints "You are too young to vote"

---
