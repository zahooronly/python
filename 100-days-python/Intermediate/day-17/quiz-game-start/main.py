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
quiz.nextQuestion()