import pandas as pd 
import random

names = [
    "Akshara","Aditya","Akash","Vishal","Neha",
    "Ganesh","Radhika","Nikhil","Manoj","Monika",
    "Suyash","Nilam","Priya","Yash","Darshan",
    "sai","Gauravi","Vaishvani","Ankita","Kartik"
]

data = []

for i in range (1,201):
    name = random.choice(names)+ " "+ str(i)

    maths = random.randint(35,100)
    science = random.randint(35,100)
    english = random.randint(35,100)
    physics = random.randint(35,100)

    attendence = random.randint(55,100)
    study_hours = round(random.uniform(1,8),1)
    previous_persentage = random.randint(40,95)

    average = round(
        (maths + science + english + physics) /4,2   
    )

    data .append([
        i,
        name,
        random.choice(["Male","Female"]),
        random.randint(15,18),
        random.choice(["10th","11th","12th"]),
        maths,
        science,
        english,
        physics,
        attendence,
        study_hours,
        previous_persentage,
        average
    ])

columns = [
    "Student Id",
    "Name",
    "Gender",
    "Age",
    "Class",
    "Maths",
    "Science",
    "English",
    "Physics",
    "Attendence",
    "Study_hours",
    "Previous_percentage",
    "Average"
]

df = pd.DataFrame(data,columns=columns)

df.to_csv("studnet_old.csv",index=False)

print("✅ Dataset created successfuilly!")
print("Total Student:",len(df))
print("File: student_old.csv")
