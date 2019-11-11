import sys
import numpy as np
sys.path.append("../")
from appJar import gui

app=gui("MAT211 Grade Calculator", "400x600")

def press(btn):

    #Lists need to be parsed
    exam_grades = app.getEntry("exam_grades")
    quiz_grades = app.getEntry("quiz_grades")
    mlp = float(app.getEntry("lab_grades"))
    basic = float(app.getEntry("basic"))
    final = float(app.getEntry("final_exam"))


    exam_list = exam_grades.split(",")
    quiz_list = quiz_grades.split(",")

    exam_list = [float(i) for i in exam_list]
    quiz_list = [float(i) for i in quiz_list]

    if len(quiz_list) > 7:
        quiz_list.remove(min(quiz_list))
        quiz_list.remove(min(quiz_list))

    if min(exam_list) < final:
        exam_list.remove(min(exam_list))
        exam_list.append(final)
    
    if final > basic:
        basic = final
        
    quiz_avg = sum(quiz_list) / len(quiz_list)
    exam_avg = sum(exam_list) / len(exam_list)
    final_grade = (quiz_avg * 0.13) + (exam_avg * 0.52) + (mlp * .10) + (final * .20) + (basic * .05)
    
    app.setLabel("grade", "Final Grade: " + str(final_grade))


app.setFont(20)
app.setBg("black")

#entries for data
app.addEntry("exam_grades",)
app.addEntry("quiz_grades")
app.addNumericEntry("final_exam")
app.addNumericEntry("lab_grades")
app.addNumericEntry("basic")

#output prompt
app.addLabel("grade", text = "Awaiting input")
app.setLabelBg("grade", "red")

#button
app.addButton("Calculate", press)

app.setEntryDefault("final_exam", "Enter Final Exam")
app.setEntryDefault("exam_grades", "Enter 4 exam grades")
app.setEntryDefault("quiz_grades", "Enter all quizzes")
app.setEntryDefault("lab_grades", "Enter MyMathLabs average")
app.setEntryDefault("basic", "Enter BKE grade")

app.go()