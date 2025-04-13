# 🧠 Python AI Roadmap – Documented Notes

---

# ✅ Lesson 1: Variables, Data Types & Basic Operations

### 📌 Theory & Purpose
Variables are the most basic unit in any programming language. In Python, they're used to store data—like text, numbers, or even logic—that your program can use, process, or modify.

> Python is dynamically typed. You don’t need to declare the type of variable before using it.

---

### 📘 Key Concepts

#### 🧾 Variables and Assignment
```python
name = "Waiz"         # string
age = 20              # integer
height = 5.9          # float
is_student = True     # boolean
```

- **name** stores text data (called a string)
- **age** stores a whole number
- **height** stores decimal numbers
- **is_student** stores a True/False value (Boolean)

---

#### 📋 Data Types in Python

| Type     | Keyword | Example     | Description              |
|----------|---------|-------------|--------------------------|
| Integer  | `int`   | `10`        | Whole numbers            |
| Float    | `float` | `10.5`      | Decimal numbers          |
| String   | `str`   | `"hello"`   | Text                     |
| Boolean  | `bool`  | `True`/`False` | Logic-based (yes/no) |

✅ You can check types using `type()`:
```python
print(type(name))  # <class 'str'>
```

---

#### ➕ Arithmetic Operators

Python supports all basic math operations.

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a // b)  # 3 (floor division)
print(a % b)   # 1 (remainder)
print(a ** b)  # 1000 (10^3)
```

---

#### 🧵 String Formatting

Use **f-strings** for clean, readable output:

```python
name = "Waiz"
age = 20
loves_AI = True

print(f"My name is {name}, I'm {age}, and it's {loves_AI} that I love AI!")
```

---

### 🧪 Practice Idea
Build a **simple profile printer**:
```python
full_name = "Waiz Ahmed"
age = 20
language = "Python"
print(f"Hi! I'm {full_name}, {age} years old, and I love coding in {language}.")
```

---
