class QuizBrain:
    def __init__(self,qList):
        self.questionNo=0
        self.questionList=qList
    def nextQuestion(self):
        currentQuestion=self.questionList[self.questionNo]
        input(f"Q.{self.questionNo}: {currentQuestion.text} (True/False): ")