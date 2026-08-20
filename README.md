# Day-94-Multiply-Dictionary-Values

Day 94/100 - Python Program to Multiply All the Items in a Dictionary

# Multiply All Items in a Dictionary

A program to dynamically calculate the total mathematical product of all numerical values stored within a Python dictionary.

## 📝 Description

This program processes a predefined dictionary containing numerical values and calculates their aggregate product.

The core logic is efficiently handled within the `multiply_values(dictionary)` function. Because Python's standard built-in functions do not include a direct equivalent to `sum()` for multiplication, the script manually computes the total. It begins by initializing a `result` variable to `1` (the multiplicative identity, ensuring the first multiplication yields the value itself).

The program then uses a `for` loop to iterate through all the active values extracted using the `dictionary.values()` method. During each iteration, it updates the `result` by multiplying it by the current `value` using the `*=` operator. Once the loop finishes processing every item, the function returns the final calculated integer or float, which the driver code captures and prints cleanly to the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A predefined dictionary containing key-value pairs where all values are numerical types (`int` or `float`).



### Output:

* A formatted string stating: "The product of all values in the dictionary is: [total_product]".



### Rules:

1. The program must initialize a hardcoded dictionary (`my_dict`) containing numerical values.


2. The core multiplication logic must be encapsulated in a function named `multiply_values(dictionary)`.


3. The function must initialize a variable `result = 1` to track the running product.


4. The function must extract the dictionary values using the `.values()` method and iterate through them.


5. The function must multiply each consecutive value using the `*=` operator.


6. The driver code must capture the return value and print it to the console using an f-string.



---

## 💡 Examples

### Example 1 (Standard Integers)

**Input:**

```python
{"a": 5, "b": 10, "c": 2}

```

**Output:**

```text
The product of all values in the dictionary is: 100

```

**Explanation:** The `.values()` method extracts the sequence of numbers `[5, 10, 2]`. The loop multiplies them sequentially: starting at 1, $1 \times 5 = 5$, then $5 \times 10 = 50$, and finally $50 \times 2 = 100$.

### Example 2 (Zero in the Dictionary)

**Input:**

```python
{"x": 25, "y": 0, "z": 4}

```

**Output:**

```text
The product of all values in the dictionary is: 0

```

**Explanation:** Following standard multiplication rules, any number multiplied by zero equals zero. As soon as the loop encounters the `0` value for key "y", the running `result` becomes `0`, and all subsequent multiplications remain `0`.

### Example 3 (Negative Numbers)

**Input:**

```python
{"item1": -3, "item2": 4, "item3": -2}

```

**Output:**

```text
The product of all values in the dictionary is: 24

```

**Explanation:** The loop extracts `[-3, 4, -2]`. It calculates $1 \times -3 = -3$, then $-3 \times 4 = -12$, and finally $-12 \times -2 = 24$. Two negative values cancel out, resulting in a positive product.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 94.py").

```bash
git clone https://github.com/adiaryaz/Day-94-Multiply-Dictionary-Values.git
cd multiply-dictionary-values

```

2. **Run the program**:

```bash
python "Day 94.py"

```

Execute the script to see how Python efficiently iterates through a dictionary to compute the aggregate product of its values!
