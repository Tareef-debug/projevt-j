import matplotlib.pyplot as plt

students_name = ["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
students_marks = [35,50,20,45,25,40,25,40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("students_name")
    plt.ylabel("students_marks")
    plt.show()

marks_line_chart

def percentage_line_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Students percentage Graph")
    plt.xlabel("students name")
    plt.ylabel("students marks")
    plt.show()
percentage_line_chart