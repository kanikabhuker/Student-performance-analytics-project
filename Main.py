import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Students.csv")

print(df)
print("Rows, columns:", df.shape)
print("colomns:",list(df.columns))
# Subjects we will calculate with
subjects = ["Maths", "Science", "English", "Computer"]

def calculate_total_and_average(data):
    # Total = sum of the 4 subjects for each student
    data["Total"] = data[subjects].sum(axis=1)
    # Average = total divided by number of subjects, rounded to 2 decimals
    data["Average"] = np.round(data["Total"] / len(subjects), 2)
    return data

df = calculate_total_and_average(df)
print(df[["Name", "Total", "Average"]])
# Grading rule: based on average marks
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 55:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def add_grade_and_result(data):
    # Loop through each student's average and collect their grade
    grades = []
    for avg in data["Average"]:
        grades.append(assign_grade(avg))
    data["Grade"] = grades

    # Pass rule: student must score 40 or more in EVERY subject
    passed = np.all(data[subjects] >= 40, axis=1)
    data["Result"] = np.where(passed, "Pass", "Fail")
    return data

df = add_grade_and_result(df)
print(df[["Name", "Average", "Grade", "Result"]])
def analyze(data):
    print("\n===== CLASS ANALYSIS =====")

    # Highest and lowest performer (idxmax gives the row number of the max)
    top = data.loc[data["Average"].idxmax()]
    low = data.loc[data["Average"].idxmin()]
    print(f"Highest average: {top['Name']} ({top['Average']})")
    print(f"Lowest average: {low['Name']} ({low['Average']})")

    # Overall class average
    print("Class average:", round(np.mean(data["Average"]), 2))

    # Pass / fail count
    print("Passed:", (data["Result"] == "Pass").sum())
    print("Failed:", (data["Result"] == "Fail").sum())

    # Subject-wise average using a loop
    print("\n--- Subject-wise average ---")
    subject_avgs = {}
    for sub in subjects:
        subject_avgs[sub] = round(np.mean(data[sub]), 2)
        print(sub, ":", subject_avgs[sub])

    best = max(subject_avgs, key=subject_avgs.get)
    print("Best subject:", best)

    # Top 3 students
    print("\n--- Top 3 students ---")
    top3 = data.sort_values("Average", ascending=False).head(3)
    print(top3[["Name", "Department", "Average", "Grade"]])

analyze(df)
# Save the full results so they can be checked later
df.to_csv("results.csv", index=False)
print("\nFull results saved to results.csv")