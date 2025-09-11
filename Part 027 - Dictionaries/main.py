student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for name, score in student_scores.items():
    if score >= 91:
        student_grades[name] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[name] = "Acceptable"
    else:  # score <= 70
        student_grades[name] = "Fail"
print(student_grades)
