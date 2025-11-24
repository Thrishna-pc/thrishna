student = {"name": "Tarun",
           "roll_number": "2345",
           "register_number": "REG2025",
           "department": "Computer Science",
           "semester": 2}
student["total_mark"] = 90
marks=student["total_mark"]
if marks>= 90:
     grade = "A"
elif marks >= 82:
     grade = "B"
elif marks >= 75:
     grade = "C"
elif marks>= 60:
     grade = "D"
elif marks >= 50:
     grade = "P"
else:
    grade = "F"  
student["grade"] = grade
del student["roll_number"]
print(student)
