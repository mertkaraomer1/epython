# q1=soru("en iyi programlama dili",["python","c#","c++","java"],"python")
# q2=soru("en popüler programlama dili",["python","c#","c++","java"],"java")
# sorular=[q1,q2]
# quiz=Quiz(sorular)
#text,choices,answer @intance attribute
#q1.checkAnswer('python') true or false4
#displayScore() skor bilgisini getirir
import random
class Qestion():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
        
    def checkAnswer(self,answer):
        if answer not in self.choices:
            return "Hatalı Bilgi"
            #raise ValueError("hatalı bilgi")
        else:
            return self.answer==answer
class Quiz():
    def __init__(self,questions):
        self.questions=random.sample(questions, len(questions))
        self.score=0
        self.questionsIndex=0
    def getQuestion(self):
        return self.questions[self.questionsIndex]
    def displayQuestions(self):
        question=self.getQuestion()
        print(f"Soru{self.questionsIndex+1}:{question.text}")
        for q in question.choices:
            print("-",q)
        answer=input("cevap=")
        if question.checkAnswer(answer):
            print("tebrikler bildiniz.")
            self.score+=1
        self.questionsIndex+=1
        self.loadQuestions()
    def loadQuestions(self):
        if len(self.questions)==self.questionsIndex:
            self.displayscore()
        else:
            self.displayProgres()
            self.displayQuestions()
            
    def displayscore(self):
        print("SONUÇ".center(100,"*"))
        puan=100/len(self.questions)
        toplampuan=round(self.score*puan)
        print(f"toplam{len(self.questions)} sorunun {self.score} tanesini bildiniz")
        print(f"Puanınız={toplampuan}")
    def displayProgres(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionsIndex+1
        print(f"toplam{totalQuestion} sorunun {self.score} sorusundasınız.")
                
q1=Qestion("en iyi programlama dili",["python","c#","c++","java"],"python")
q2=Qestion("en popüler programlama dili",["python","c#","c++","java"],"java")  
q3=Qestion("en çok zengin eden programlama dili",["python","c#","c++","js"],"java") 
# print(q1.checkAnswer("python")) 
sorular=[q1,q2,q3]
quiz=Quiz(sorular)
quiz.loadQuestions()










