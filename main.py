from pyscript import document, display

name = "Eran" #String
age = 15 #integer
height1 = 167.0 #float
countries_to_visit = ["China", "Japan", "Tiki Tiki Phonk Land"] #list
student_type = True #boolean
student_info = {
    "color": "Purple",
    "car_brand": "Ford",
    "shoe_size": 9.5,
    "best_friend": "Louie Vonn"
}
fruits = {"Mango", "Grapes", "banana"} #set
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #tuple

display("Name:", name, target="output")
display("Age:", age, target="output")
display("Height:", height1, target="output")
display("Countries to Visit:", countries_to_visit, target="output")
display("Student:", student_type, target="output")
display("Student Info:", student_info, target="output")
display("Favorite Fruits:", fruits, target="output")
display("Days in a week:", days, target="output")

def calculate(e):
    document.getElementById("output").innerHTML = ""

    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)

    addition = num1 + num2
    subtraction = num1 - num2

    display(f"Addition: {addition}", target="output")
    display(f"Subtraction: {subtraction}", target="output")