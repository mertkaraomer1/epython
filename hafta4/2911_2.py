# q1=soru("en iyi programlama dili",["python","c#","c++","java"],"python")
# q2=soru("en popüler programlama dili",["python","c#","c++","java"],"java")
# sorular=[q1,q2]
# quiz=Quiz(sorular)
#text,choices,answer @intance attribute
#q1.checkAnswer('python') true or false4
#displayScore() skor bilgisini getirir

class Qestion():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
        
    def checkAnswer(self,answer):
        if answer not in self.choices:
            return "Hatalı Bilgi"
        else:
            return self.answer==answer
q1=Qestion("en iyi programlama dili",["python","c#","c++","java"],"python")
q2=Qestion("en popüler programlama dili",["python","c#","c++","java"],"java")  
print(q1.checkAnswer("python")) 
# sorular=[q1,q2]
# quiz=Quiz(sorular)
