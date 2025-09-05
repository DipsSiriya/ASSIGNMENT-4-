"""Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

stdmrk = {'om':72,'dipesh':72.40,'Alice':45}
stdname = input("Enter the student's name: ")
if stdname in stdmrk:
    print(f"{stdname}'s marks :{stdmrk[stdname]}")
else:
    print("Student not found")