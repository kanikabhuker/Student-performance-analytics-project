# Student Performance Analytics System

**Student:** Kanika Bhuker
**College:** Fateh Chand College for Women, Hisar
**Internship:** Python with AI (EWB Courses)

## Objective
This project analyzes student academic data using Python. It calculates total and average marks, assigns grades, identifies pass/fail students, and finds subject-wise performance and top performers. It shows how raw marks can be turned into meaningful results automatically.

## Technologies Used
- Python
- NumPy
- Pandas
- VS Code
- GitHub

## Dataset Description
`students.csv` contains 20 student records with these columns: Student_ID, Name, Department, Maths, Science, English, Computer and Attendance. Marks are out of 100 and attendance is in percentage. The data is created for this project, with realistic values.

## Implementation
1. **Loading data:** the CSV file is read into a Pandas DataFrame, and its shape and columns are displayed.
2. **Total and average:** total marks are the sum of the four subjects, and the average is rounded using NumPy.
3. **Grading rule:** A (85+), B (70-84), C (55-69), D (40-54), F (below 40), based on the average.
4. **Pass/Fail rule:** a student passes only if they score 40 or more in every subject (checked with `np.all` and `np.where`).
5. **Analysis:** highest and lowest average, class average, pass/fail count, subject-wise averages and the top 3 students.
6. **Saving results:** the final table is saved to `results.csv`.

## Key Features
- Reusable functions: `calculate_total_and_average()`, `assign_grade()`, `add_grade_and_result()`, `analyze()`
- Loops used for grading and subject-wise analysis
- NumPy used for mean, rounding and conditions
- Pandas used for loading, sorting and filtering data
- Clear, readable output in the terminal

## Final Outcome
The program ran successfully and produced these results:
- Highest average: Simran Kaur (93.75)
- Lowest average: Vikas Kumar (36.5)
- Class average: 64.71
- Passed: 14 students, Failed: 6 students
- Best subject: English (average 66.45)
- Top 3 students: Simran Kaur, Sneha Gupta, Isha Arora

The project achieved its goal of converting raw student data into clear, useful analysis.

## Challenges & Learning
- **Pandas not installed:** I got an error at first, and solved it by installing the libraries with `pip install pandas numpy`.
- **File name mismatch:** I created `student.csv` by mistake instead of `students.csv`, and fixed it by renaming the file.
- **New to the concepts:** I learned how DataFrames, NumPy functions, loops and reusable functions work together in a real project.
- **GitHub:** I learned to create a repository, upload files and write a README.

## GitHub Repository
https://github.com/kanikabhuker/Student-performance-analytics-project
