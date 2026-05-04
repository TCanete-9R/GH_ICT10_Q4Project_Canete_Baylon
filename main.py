from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        display(f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}.", target="output")

classmates = [
    Classmate("Enzo", "Ruby", "Math"),
    Classmate("Koby", "Ruby", "Science")
]

def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    classmates.append(Classmate(name, section, subject))
    display("Added!", target="output")

def show_list(e):
    document.getElementById("output").innerHTML = ""
    for cm in classmates:
        cm.introduce()

# Initial data
days = np.array(['Mon','Tue','Wed','Thu','Fri'])
sales = np.array([1, 0, 7, 4, 9])  # starting absences

def draw_graph():
    plt.clf()
    plt.plot(days, sales, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Number of Absences")
    display(plt, target="plot")

# First render
draw_graph()

def update_graph():
    global sales

    day = document.getElementById("day").value
    value = int(document.getElementById("absences").value)

    index = np.where(days == day)[0][0]
    sales[index] = value

    # NumPy stats (like your original code)
    print("Shape:", sales.shape)
    print("Mean:", np.mean(sales))
    print("Max:", np.max(sales))

    draw_graph()
