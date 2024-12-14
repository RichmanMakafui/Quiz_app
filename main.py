import tkinter as tk
from tkinter import messagebox
import json
import random
import time

# Load questions from a JSON file
def load_questions():
    # Example questions, you can replace this with a file if needed
    return [
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["30", "35", "40", "45"],
            "answer": "30"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "O3"],
            "answer": "H2O"
        },
        {
            "question": "What is the square root of 16?",
            "options": ["2", "4", "6", "8"],
            "answer": "4"
        }
    ]

# Function to start the quiz
def start_quiz():
    global current_question, score, timer_running
    current_question = 0
    score = 0
    timer_running = True
    update_score_label()
    next_question()

# Function to display the next question
def next_question():
    global current_question, timer_running
    if current_question < len(questions):
        question = questions[current_question]
        question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            options_buttons[i].config(text=option, state="normal", bg="#4CAF50", fg="white")
        current_question += 1
        start_timer()
    else:
        timer_running = False
        messagebox.showinfo("Quiz Over", f"Your final score is {score}/{len(questions)}")
        root.quit()

# Function to start the timer
def start_timer():
    global timer_running, time_left
    time_left = 10
    timer_label.config(text=f"Time Left: {time_left}s", fg="red")
    update_timer()

# Function to update the timer every second
def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}s")
        root.after(1000, update_timer)
    elif time_left == 0:
        check_answer(None)

# Function to check the user's answer
def check_answer(selected_option):
    global score, timer_running
    if timer_running:
        question = questions[current_question - 1]
        if selected_option == question["answer"]:
            score += 1
        update_score_label()
        next_question()

# Function to update the score label
def update_score_label():
    score_label.config(text=f"Score: {score}")

# Function to handle button click
def option_selected(option):
    check_answer(option)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Load the questions
questions = load_questions()

# Set up the GUI elements
score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14), bg="#f0f0f0")
score_label.pack(pady=10)

question_label = tk.Label(root, text="", font=("Helvetica", 16), width=50, height=3, anchor="w", bg="#f0f0f0")
question_label.pack(pady=20)

options_buttons = [tk.Button(root, text="", font=("Helvetica", 12), width=30, height=2, command=lambda option=opt: option_selected(option), relief="solid") for opt in range(4)]
for button in options_buttons:
    button.pack(pady=5)

timer_label = tk.Label(root, text="Time Left: 10s", font=("Helvetica", 12), bg="#f0f0f0")
timer_label.pack(pady=20)

start_button = tk.Button(root, text="Start Quiz", font=("Helvetica", 14), width=30, height=2, command=start_quiz, bg="#4CAF50", fg="white")
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
