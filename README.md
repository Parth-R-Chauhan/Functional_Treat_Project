<div align="center">

# 📊 Data Analyzer and Transformer

### A Menu-Driven Python Project for Data Analysis and Transformation

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Data+Analyzer+and+Transformer;Analyze+1D+and+2D+Arrays;Filter+%7C+Transform+%7C+Sort;Python+Fundamentals+in+Action" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-00C2FF?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-Command_Line-111827?style=for-the-badge)

</div>

---

# 🌟 About The Project

**Data Analyzer and Transformer** is a menu-driven Python command-line program that lets users enter and analyse one-dimensional (1D) and two-dimensional (2D) integer data.

The program demonstrates Python concepts including functions, recursion, `*args`, `**kwargs`, lambda expressions, `filter()`, `map()`, sorting, and basic statistical calculations.

---

# 🎯 Project Objectives

- 📥 Accept user input as 1D or 2D data
- 📊 Calculate count, minimum, maximum, sum, and average
- 🧮 Calculate factorial using recursion
- 🔎 Filter values according to a threshold
- 🔁 Transform filtered values by multiplying them by 2
- ↕️ Sort 1D data in ascending or descending order
- 📋 Sort each row of 2D data
- 📈 Display dataset statistics
- 🧠 Practise important Python programming concepts

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 📥 Input Data

Enter integer values into a 1D list or multiple rows for a 2D list.

</td>
<td width="50%">

### 📊 Data Summary

Display element count, minimum, maximum, total sum, and average.

</td>
</tr>
<tr>
<td width="50%">

### 🧮 Factorial with Recursion

Calculate a number's factorial using a recursive function.

</td>
<td width="50%">

### 🔎 Filter & Transform

Keep values greater than or equal to a threshold, then double them using `map()` and `lambda`.

</td>
</tr>
<tr>
<td width="50%">

### ↕️ Sorting

Sort 1D data in ascending or descending order and display sorted rows for 2D data.

</td>
<td width="50%">

### 📈 Dataset Statistics

Calculate minimum, maximum, sum, and average using a function that returns multiple values.

</td>
</tr>
</table>

---

# 🧰 Technology & Concepts

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" />

</div>

| Concept | How It Is Used |
|---|---|
| 🐍 Python | Main programming language |
| 📋 Lists | Store 1D and 2D data |
| 🧩 Functions | Organize program operations |
| 🔁 Recursion | Calculate factorial |
| `*args` | Display a variable number of filtered values |
| `**kwargs` | Display dataset summary characteristics |
| `lambda` | Define short filtering and transformation expressions |
| `filter()` | Select values greater than or equal to the threshold |
| `map()` | Multiply filtered values by 2 |
| `sort()` | Sort a copied 1D list |
| `sorted()` | Return sorted rows for 2D data |
| 📊 Built-in functions | Use `min()`, `max()`, `sum()`, and `len()` |
| 📝 Docstrings | Display descriptions of functions |

---

# 🏗️ Project Structure

```text
Functional_Treat_Project/
│
├── function_treat.py
└── README.md
```



---

# 🔄 Application Workflow

```text
Start Program
     │
     ▼
Display Main Menu
     │
     ├── 1. Input 1D / 2D Data
     ├── 2. Display Data Summary
     ├── 3. Calculate Factorial
     ├── 4. Filter & Transform Data
     ├── 5. Sort Data
     ├── 6. Display Dataset Statistics
     └── 7. Exit
```

---

# 📌 Menu Options

| Option | Operation | Description |
|---:|---|---|
| 1 | Input Data | Enter a 1D list or 2D rows |
| 2 | Display Data Summary | Show count, minimum, maximum, sum, and average |
| 3 | Calculate Factorial | Calculate factorial through recursion |
| 4 | Filter & Transform Data | Filter by threshold and double matching values |
| 5 | Sort Data | Sort 1D data or each row of 2D data |
| 6 | Display Dataset Statistics | Show minimum, maximum, sum, and average |
| 7 | Exit | End the program |

---

# 💻 Example Main Menu

```text
=== DATA ANALYZER AND TRANSFORMER PROG ===
1. Input Data
2. Display Data Summary
3. Calculate Factorial (Recursion)
4. Filter & Transform Data (Lambda, filter, map, *args)
5. Sort Data
6. Display Dataset Statistics
7. Exit
Select an option (1-7):
```

---

# 🔍 Example: Filtering and Transformation

If the entered data is:

```python
[2, 5, 8, 10, 3]
```

And the threshold is `5`, the filter keeps values greater than or equal to `5`:

```python
[5, 8, 10]
```

The transformation multiplies each filtered value by `2`:

```python
[10, 16, 20]
```

---

# 📈 Data Statistics

For the selected dataset, the program calculates:

- **Total count** — number of elements
- **Minimum value** — smallest element
- **Maximum value** — largest element
- **Sum total** — sum of all elements
- **Average** — sum divided by the number of elements

The summary is also stored in the `dataset_summary` dictionary and displayed through `display_kwargs_summary(**kwargs)`.

---

# 🚀 How to Run the Project

## 1. Install Python

Install Python 3.x if it is not already installed.

## 2. Open the Project Folder

Open a terminal or command prompt in the folder containing your Python file.

## 3. Run the Program

```bash
python your_file_name.py
```

Replace `your_file_name.py` with your actual Python filename.

> This project uses Python's built-in features and does not require third-party packages.

---

# 📋 Requirements

- Python 3.x
- A code editor or terminal, such as VS Code or Command Prompt

No external Python libraries are required.

---

# 🧠 Skills Practised

- Python fundamentals
- Lists and nested lists
- Functions and return values
- Recursion
- `*args` and `**kwargs`
- Lambda expressions
- `filter()` and `map()`
- Sorting lists
- Basic descriptive statistics
- Menu-driven program design
- User input and conditional logic

---

# 🔮 Future Enhancements

- 🛡️ Handle invalid inputs and empty datasets safely
- 💾 Save and load data using files
- 📊 Add median and mode calculations
- 📈 Create charts using Matplotlib
- 📁 Import datasets from CSV files
- 🖥️ Build a graphical user interface
- 🧪 Add automated tests

---

# ⚠️ Current Program Notes

- Data is stored in memory while the program runs; it is not saved permanently.
- The 2D sorting option sorts and displays each row individually; it does not rearrange the original `data_2d` rows.
- The program expects valid integer input and non-empty data for several operations. Invalid input or an empty row/dataset may cause an error.
- The factorial function handles `0` and `1` as base cases and returns `"Invalid number"` for negative input.

---

# 👨‍💻 About The Developer

Parth Chauhan

---

<div align="center">

## 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Analyze+Data.;Transform+Values.;Practise+Python.;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>

<br><br>

**Made with ❤️ and Python**

</div>
