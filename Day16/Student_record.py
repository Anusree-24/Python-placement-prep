name=input("Enter your name:")
Dept=input("Enter your department:")
with open("student_record.txt","w") as file:
    file.write("Name: "+ name +"\n")
    file.write("Department:"+ Dept +"\n")
print("student record saved")
