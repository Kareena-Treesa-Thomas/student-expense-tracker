# Student-expense-tracker(Python Project)
A beginner-friendly Python CLI expense tracker designed to help students practice **core programming concepts** such as **lists, dictionaries, sets, recursion, and clean logic**.  
The project allows users to add expenses, view them, calculate total spending, and analyze spending by category — all through a simple command-line interface.

---

## Features
- Add expenses with **amount**, **category**, and optional **note**  
- View all recorded expenses in a structured list  
- Calculate **total spending** using recursion  
- Show **unique categories** using sets  
- Analyze spending per category and highlight the **highest spending category**  
- Simple and interactive **CLI interface**  

---

## How It Works?
1. User runs the Python program.  
2. The program displays a **menu** with  options: Add Expense, View Expenses, Total Spending, Category Analysis, and Exit.  
3. The user selects an option by typing the corresponding number.  
4. For “Add Expense,” the user enters amount, category, and optional note.  
5. For “View Expenses,” the program lists all added expenses.  
6. For “Total Spending,” the program calculates the total using **recursion**.  
7. For “Category Analysis,” the program shows spending per category and highlights the **highest spending category**.  
8. The user can exit the program anytime using the Exit option.
   
---


## Project Structure
```
student-expense-tracker/
│
├── expense_tracker.py # Main Python CLI code
├── README.md # Project description and instructions
├── LICENSE # MIT License
```

---

## How to Run the Project
1. Clone the repository:
```
git clone https://github.com/yourusername/student-expense-tracker.git
```
2. Navigate to the project folder:
```
cd student-expense-tracker
```
3. Run the Python program:
```
python expense_tracker.py
```

---

## Sample Output
```
=== Student Expense Tracker ===
1. Add Expense
2. View Expenses
3. Total Spending
4. Category Analysis
5. Exit
Enter choice: 1
Enter amount spent: 50
Enter category (food/travel/shopping/etc): food
Optional note: lunch
Expense added successfully!

Enter choice: 1
Enter amount spent: 200
Enter category (travel): bus
Expense added successfully!

Enter choice: 4
Unique Categories: {'travel', 'food'}
Spending per category:
food: 50.0
travel: 200.0
Highest spending category: travel (200.0)
```
---
## What I Learned
1.Lists, dictionaries, sets, and tuples for storing and managing data
2.Recursion for calculations
3.Designing a clean CLI interface
4.Structuring a mini-project professionally for GitHub
5.How to analyze data and generate insights using Python

## Future Scope
1.Save expenses to a file for persistence
2.Add priority or recurring expenses
3.Convert CLI into GUI using Tkinter
4.Generate weekly/monthly reports
5.Expand into web or mobile applications

## Author
```
Kareena Treesa Thomas- 💻🚀 – Tech enthusiast and aspiring developer. 
GitHub: https://github.com/Kareena-Treesa-Thomas
```
---
## License
This project is licensed under the MIT License – see the LICENSE file for details.

