# Interactive Personal Data Collector

This project is a simple Python program designed to collect personal information from the user, display the data along with their data types and memory IDs, and estimate the user's birth year based on their age.

## 📌 Features

* Collects the user's:

  * Name
  * Age
  * Height
  * Favourite Number
* Displays each value with:

  * Data type (`type()`)
  * Memory address (`id()`)
* Calculates the approximate birth year.
* Provides clear and interactive terminal output.

## 🧾 Code Overview

The script performs the following steps:

1. Prompts the user for inputs.
2. Converts data into appropriate types (`int`, `float`, `str`).
3. Prints collected information with `type()` and `id()` functions.
4. Calculates:

   ```python
   2025 - age
   ```
5. Displays a thank‑you message.

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Save the script as `fundamental_booster.py`.
3. Open your terminal and run:

   ```bash
   python fundamental_booster.py
   ```

## 🧠 Example Input/Output

**User Input:**

* Name: Rahul
* Age: 20
* Height: 5.8
* Favourite Number: 7

**Program Output:**

* Shows values, types, and memory IDs
* Shows approximate birth year: `2025 - 20 = 2005`

## 📂 File Structure

```
project-folder/
│
├── fundamental_booster.py
├── README.md
```

## 💡 Purpose

This program helps beginners understand:

* User input handling
* Typecasting in Python
* Using `type()` and `id()` functions
* Basic arithmetic operations

## ✔️ Author

Created for practice and learning Python fundamentals.

---

Thank you for using the **Interactive Personal Data Collector**!
