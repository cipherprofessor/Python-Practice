students = ["Mohsin","Muquat","Athar","Sadiya","Aayat","Eiman","Rupika","Bazila"]
for student in students:
    if student == "Eiman":
        break;
    print(student)

for student in students:
    if student == "Rupika":
        continue;
    print(student)