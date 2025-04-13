
# ✅ Lesson 3: Loops (The Heartbeat of Programming)

### 📌 Why Loops?
Loops help you **repeat** tasks without writing code over and over.  
We’ll look at:
- `while` loops (run while condition is true)
- `for` loops (run for a fixed number of steps)
- `range()`, `break`, `continue`, and even a mini-project 👀

---

### 🔄 `while` Loop

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```
💡 Runs as long as `count <= 5`.  
If you forget `count += 1`, it loops *forever* (infinite loop)!

---

### 🔁 `for` Loop + `range()`

```python
for i in range(5):
    print("i =", i)
```

| Code              | Output         |
|------------------|----------------|
| `range(5)`       | 0 to 4         |
| `range(1, 6)`    | 1 to 5         |
| `range(2, 10, 2)`| 2, 4, 6, 8     |

---

### 🚪 `break` & `continue`

```python
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
```

---

### 🔂 Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```
This will run 3×2 = 6 times.

---

### 💻 Mini Project – Countdown Timer

```python
import time

count = 5
while count > 0:
    print(f"Timer: {count}")
    time.sleep(1)  # waits 1 second
    count -= 1

print("Time's up!")
```

---

### 🧠 Practice Ideas (Try These!)

#### 1. Print numbers 1 to 10 using both loops

```python
# Using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Using for loop
for i in range(1, 11):
    print(i)
```

#### 2. Print even numbers from 1 to 20

```python
for i in range(2, 21, 2):
    print(i)
```

#### 3. Simple menu (loop until 'exit')

```python
while True:
    user_input = input("Type something (or 'exit' to stop): ")
    if user_input == "exit":
        print("Exiting...")
        break
    else:
        print("You typed:", user_input)
```

#### 4. Print pattern using nested loops

```python
rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

---
