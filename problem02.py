# Write a program to accept marks of 6 students and display them in a sorted 
# manner. 
marks=[]
n1=int(input("Enter the marks of student 1: "))
marks.append(n1)
n2=int(input("Enter the marks of student 2: "))
marks.append(n2)
n3=int(input("Enter the marks of student 3: "))
marks.append(n3)
n4=int(input("Enter the marks of student 4: "))
marks.append(n4)
n5=int(input("Enter the marks of student 5: "))
marks.append(n5)
n6=int(input("Enter the marks of student 6: "))
marks.append(n6)
print(marks)
marks.sort()
print(marks)