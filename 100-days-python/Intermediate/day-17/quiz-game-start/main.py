from _data import questionData
from question_model import Question
import quizbrain
questionBank=[]

for question in questionData:
    questionText=question["text"]
    questionAnswer=question["answer"]
    newQuestion=Question(text=questionText,answer=questionAnswer)
    questionBank.append(newQuestion)


quiz=quizbrain.QuizBrain(questionBank)

while quiz.stillQuestions():
    quiz.nextQuestion()
    print(" ")
    
print("You've completed the quiz!")
print(f"Your Score is: {quiz.score}/{quiz.questionNo}")
