class Experiment:

    company="ITI AI Lab"

    def __init__(self,name,researcher,score):
        self.name=name
        self.researcher=researcher
        self.score1=score

        
    @property
    def score1(self):
       
       return self._score1
    
    @score1.setter
    def score1(self,value):
       
       if 0  <=value<= 1:
            self._score1=value
       else:
            raise ValueError("score must be between 0 and 1")

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["researcher"],
            data["score"]
        )
experiment_data = {
    "name": "Sentiment Analysis",
    "researcher": "Ahmed",
    "score": 0.87
}
ex1 = Experiment("Loubid","Ali",0.75)
print(ex1.score1)
print(ex1._score1)
ex2=Experiment.from_dict(experiment_data)
print(ex2)

#ex2 = Experiment("Loubid","Ali",1.005)#Error!
#print(ex2.score1)
print(f"Name: {ex2.name}")
print(f"Researcher: {ex2.researcher}")
print(f"Score: {ex2.score1}")
print("#"* 50)
print(f"Name: {ex1.name}")
print(f"Researcher: {ex1.researcher}")
print(f"Score: {ex1.score1}")






    



#score must be between 0 and 1 

