class QuizBrain:
    def __init__(self,qList):
        self.questionNo=0
        self.questionList=qList
        self.score=0
    
    def stillQuestions(self):
        if self.questionNo<len(self.questionList):
            return True
        return False
    
    def nextQuestion(self):
        currentQuestion=self.questionList[self.questionNo]
        self.questionNo+=1
        userAnswer=input(f"Q.{self.questionNo}: {currentQuestion.text} (True/False): ")
        self.checkAnswers(userAnswer,currentQuestion.answer)
    
    
    def checkAnswers(self,userAnswers,correctAnswers):
        if userAnswers.lower()==correctAnswers.lower():
            print("That's Right!")
            self.score+=1
        else:
            print("That's Wrong!")
        print(f"Correct Answer is: {correctAnswers}")
        print(f"Your current Score is {self.score}/{self.questionNo}")