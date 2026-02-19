#kaun banega crorepati exercise

#create a program capable of displaying questions to the user like KBC
#Use the list datatype to store the questions and their correct answers
#Display the final amount the person is taking home after playing the game.


import random
import time

print("Welcome to the Kaun banega Crorepatik")

print("Let's start the game Now....")

quiz = [
        {
            
           "question": "What is the captital of INDIA?" ,
           "options" : ["A. New Delhi", "B. Mumbai", "C. Ranchi", "D. Madhya Pradesh"],
           "answer": "A"
           },

        {
        "question": "What is the Name of the Prime Minister of India?",
         "options": ["A. Jai Shankar", "B. Goyal sir", "C. Hari Prasad", "D. Narendra Modi" ],
          "answer": "D"
        },

        {
            "question": "Who is the famous influencer on the Globe?",
            "options": ["A. MrBeast", "B. Tseries", "C. Carryminati", "D. Sherlock Holmes"],
            "answer": "A"
        },
        {
            "question": "Which is the most played game in the INDIA?",
            "options": ["A. Baseball", "B. Cricket", "C. Tennis", "D. Holleyball"], 
            "answer" : "B"      
        }
]

#adding a score counter
score = 0
#selecting random question
#shuffle questions so the order is random
random.shuffle(quiz)

q = random.choice(quiz)

for q in quiz:
    print("\nQuestion: ")
    print(q["question"])

    print("\nOptions:")
    for option in q["options"]:
        print(option)

    print("\nYou have 10 seconds to answer!")

    start_time = time.time()

    user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

    end_time = time.time()

    time_taken = end_time - start_time

    if time_taken > 10:
        print("\n Time over!!")
        print("Correct answer is : ", q["answer"])
    else:
        if user_answer == q["answer"]:
            print("Correct answer!")
            score +=1
        else:
            print("Wrong answer")
            print("The correct answer is : ", q["answer"])

#printing the final score
print("\nYour Final score is : ", score, "/", len(quiz))