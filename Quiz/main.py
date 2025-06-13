import mysql.connector
import random
import time
import os
import csv
from InquirerPy import inquirer

username = input("Enter your username: ")
score = 0


# Connect to the MySQL database
db = mysql.connector.connect(
    host="sql.endora.cz",
    port="3313",
    user="weizzx",
    password="8^td)A3;t3]vyWH",
    database="weizzx"
)


# Loading animation
for i in range(101):
    print(f"Loading... {i+1}%")
    time.sleep(0.0125)  # Simulate loading time
    os.system('cls')
    if i == 100:
        print("Loading complete!")

time.sleep(0.5)  # Pause before starting the quiz
os.system('cls')



#Quiz loop in range of 6 questions
for i in range(6):

    cursor = db.cursor()

    question_id = (random.randrange(1, 20))

    cursor.execute("SELECT question_text FROM questions WHERE id = %s", (question_id,))
    question_text = cursor.fetchone()

    if not question_text:
        print("Question not found.")
        continue

    question_text = question_text[0]

    cursor.execute("SELECT option_a, option_b, option_c, option_d FROM questions WHERE id = %s", (question_id,))
    option = cursor.fetchone()

    if option:
        options = {
            "A": option[0],
            "B": option[1],
            "C": option[2],
            "D": option[3],
        }
    else:
        print("Option not found.")


    # Build choices like A) Option A, B) Option B, ...
    choices = [f"{key}) {options[key]}" for key in options]

    # Let user select one using arrow keys
    selected = inquirer.select(
        message=question_text,
        choices=choices,
        pointer="👉",
        instruction="(Use arrow keys and press Enter to select)"
    ).execute()

    # Fetch correct answer from the DB
    cursor.execute("SELECT correct_option FROM questions WHERE id = %s", (question_id,))
    correct_option = cursor.fetchone()

    # Validate answer
    try:
        correct_option = correct_option[0]  # should be 'A', 'B', 'C', or 'D'
        selected_letter = selected[0]  # e.g. "A" from "A) Something"
        
        if selected_letter == correct_option:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong!")
    except:
        print("Error: correct option not found.")



print(f"Your final score is: {score}/6")

if score >= 3:
    print("Congratulations! You passed the quiz!")
    isPassed = True
else:
    print("Sorry, you did not pass the quiz. Better luck next time!")
    isPassed = False

cursor.execute("INSERT INTO scoreboard (username, score, isPassed) VALUES (%s, %s, %s)", (username, score, isPassed,))

with open("results.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([username, score, "Passed" if isPassed else "Failed"])

cursor.close()
db.close()