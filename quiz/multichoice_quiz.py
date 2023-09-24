import tkinter as tk
from tkinter import messagebox
import random


# Define your questions here
questions = [
    # scientific method questions
    {
        "question": "A method of research in which a problem is identified, relevant data are gathered, a hypothesis is formulated from these data, and the hypothesis is empirically tested: ",
        "options": ["A. Hypothesis Method", "B. Observation Method", "C. Experiment Method", "D. Scientific Method"],
        "answer": "D"
    },
    {
        "question": "What is the act of noting or recording something with instruments?",
        "options": ["A. Conclusion", "B. Scientific notation", "C. Significant figures", "D. Observation"],
        "answer": "D"
    },
    {
        "question": "What is a tentative explanation for an observation or scientific problem that can be tested by further investigation?",
        "options": ["A. Hypothesis", "B. Observation", "C. Experiment", "D. Conclusion"],
        "answer": "A"
    },
    {
        "question": "What is a test under controlled conditions that is made to demonstrate a known truth, examine the validity of a hypothesis, or determine the efficacy of something previously untried?",
        "options": ["A. Hypothesis", "B. Experiment", "C. Controlled variable", "D. Scientific method"],
        "answer": "B"
    },
    {
        "question": "A variable whose value is being altered to bring a change in some condition: ",
        "options": ["A. Dependent Variable", "B. Qualitative data", "C. Independent variable", "D. Controlled variable"],
        "answer": "C"
    },
    {
        "question": "The observed variable in an experiment or study whose changes are determined by the presence or degree of one or more independant variables: ",
        "options": ["A. Controlled variable", "B. Dependant variable", "C. Significant figures", "D. Independent variable"],
        "answer": "B"
    },
    {
        "question": "What is a sample in which a factor whose effect is being estimated is absent or is held constant, in order to provide a comparison?",
        "options": ["A. Mass", "B. Experiment", "C. Controlled variable", "D. Conclusion"],
        "answer": "C"
    },
    {
        "question": "What is the position reached after consideration of data obtained from an experiment?",
        "options": ["A. Hypothesis", "B. Scientific notation", "C. Observation", "D. Conclusion"],
        "answer": "D"
    },
    {
        "question": "Data described in terms of some quality or categorization that may be informal or may use ill-defined characteristics such as warmth and flavor.",
        "options": ["A. Qualitative data", "B. Quantitative data", "C. Significant figures", "D. Dimentional analysis"],
        "answer": "A"
    },
    {
        "question": "Data described in terms of quantity and in which numerical values are used.",
        "options": ["A. Qualitative data", "B. Independant variable", "C. Quantitative data", "D. Controlled variable"],
        "answer": "C"
    },
    {
        "question": "A property of matter equal to the measure of an object's resistance to changes in either its speed or direction of it motion.  The ____ of an object is not dependent on gravity and therefore is different from but proportional to its weight.",
        "options": ["A. Length", "B. Mass", "C. Temperature", "D. Volume"],
        "answer": "B"
    },
    {
        "question": "The amount of space occupied by a three-dimentional object or region of space.",
        "options": ["A. Volume", "B. Length", "C. Mass", "D. Significant figures"],
        "answer": "A"
    },
    {
        "question": "What is the measurement of the extent of something along its greatest dimention?",
        "options": ["A. Mass", "B. Length", "C. Dimentional analysis", "D. Volume"],
        "answer": "B"
    },
    {
        "question": "A measure of the average kinetic energy of the particles in a sample of matter, expressed in terms of units or degrees designated on a standard scale.",
        "options": ["A. Matter", "B. Metric system", "C. Volume", "D. Temperature"],
        "answer": "D"
    },
    {
        "question": "A decimal system of units based on the meter as a unit length.",
        "options": ["A. Volume", "B. Metric system", "C. Length", "D. Mass"],
        "answer": "B"
    },
    {
        "question": "A method of writing or displaying numbers in terms of a  decimal number between 1 and 10 multiplied by a power of 10.",
        "options": ["A. Scientific notation", "B. Scientific method", "C. Hypothesis", "D. Dimentional analysis"],
        "answer": "A"
    },
    {
        "question": "What is a technique that involves the study of dimentions of physical quantities?",
        "options": ["A. Experiment", "B. Scientific notation", "C. Scientific method", "D. Dimentional analysis"],
        "answer": "D"
    },
    {
        "question": "All of the numbers in a measurement that are known to be accurate plus one that is uncertain.",
        "options": ["A. Scientific method", "B. Significant figures", "C. Metric system", "D. Volume"],
        "answer": "B"
    },
    # matter questions
    {
        "question": "the evaporation and subsequant collection of a liquid by condensation as a means of purification.",
        "options": [""],
        "answer": ""
    },
    {
        "question": "the mass per unit valume of a substance commonly measured in grams per milliliter (g/ml) or grams per cubic centimeter (g/cm^3)",
        "options": [""],
        "answer": ""
    },
    {
        "question": "a homo mixture or solid solution of two or more metals ,the atomsa of one replaceing or occupying interstitial positions between the atoms of the other: Brass in a alloy of zinc and copper",
        "options": [""],
        "answer": ""
    },
    {
        "question": "uniform in struture or composition throughost. Homogeneous mixtures have atioms and molecules interspersed",
        "options": [""],
        "answer": ""
    },
    {
        "question": "consisting of dissimilar parts. Hetergeneous mistures have distinguishable phases",
        "options": [""],
        "answer": ""
    },
    {
        "question": "a composition of two or more substances that are not chemically combined with each other and are capable of being separated",
        "options": [""],
        "answer": ""
    },
    {
        "question": "a homogeneous mixture of two or more substances, which may be solids,liquids,gases, or a combination of these ",
        "options": [""],
        "answer": ""
    },
    {
        "question": "a pure, macroscopically homogenous substances consisting of atoms or ions of two or more different elements in difinite proportions then can not be separated by physical means. A compound usually has properties unlike those of its constituent elements.",
        "options": [""],
        "answer": ""
    },
    {
        "question": "a sample of matter, either an element or a compound, that consists of only one component with definite physical and chemical properties and a sefinite composition.",
        "options": [""]
        "answer" : ""
    },
    {
        "question": "a substance composed of atoms haveing an identical number of protons in each nucleus. Elements cannot be reduced to simpler substances by normal chemical means.",
        "options": [""],
        "answer": ""
    },
    {
        "question": "only peocess determind by the atomic and molecular composition and structure of the substances involved",
        "options": [""],
        "answer": ""
    },
    {
        "question": "any change not involving a change in the substances chimical identity. includes a change from one state (solis or liquid or gas) to another ithout a change in chemical composition",
        "options": [""],
        "answer": ""
    },
    {
        "question": "any of a chimicals properties that become evident during a chemial reactions, examples are reacivity and flammability",
        "options": [""],
        "answer": ""
    },
    {
        "question": "property of a compound that can change without involving a change in chemical composition, examples are the melting point and boiling point",
        "options": [""],
        "answer": ""
    }
    # Add more questions here
]


# randomly choose a certain number of questions
# Check if there are at least 10 questions in the pool
if len(questions) < 10:
    print("Not enough questions in the pool.")
else:
    # Select 10 random questions from the list
    selected_questions = random.sample(questions, 10)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Quiz")
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.option_radios = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value="", font=("Helvetica", 10))
            radio.pack(anchor="w")
            self.option_radios.append(radio)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(selected_questions):
            question = selected_questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            self.radio_var.set("")  # Clear the radio selection
            for i in range(4):
                self.option_radios[i].config(text=question["options"][i], value=question["options"][i][0])
        else:
            self.show_results()

    def check_answer(self):
        question = selected_questions[self.current_question_index]
        user_answer = self.radio_var.get()
        if user_answer == question["answer"]:
            self.score += 10

        self.current_question_index += 1
        self.next_question()

    def show_results(self):
        total_score = len(selected_questions) * 10
        letter_grade = ""

        if self.score >= 0.9 * total_score:
            letter_grade = "A"
        elif self.score >= 0.8 * total_score:
            letter_grade = "B"
        elif self.score >= 0.7 * total_score:
            letter_grade = "C"
        elif self.score >= 0.6 * total_score:
            letter_grade = "D"
        else:
            letter_grade = "F"

        messagebox.showinfo("Quiz Result", f"Your score: {self.score}/{total_score}\nLetter Grade: {letter_grade}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry("500x400")
    root.mainloop()
