from Experiment import Experiment

class ClassificationExperiment(Experiment) :
    def __init__(self,name,researcher,score ,number_of_classes):
        super().__init__(name,researcher,score)
        self.number_of_classes=number_of_classes

#@Override
    def Report(self):
            return (f"Esperimnet--> {self.name}\n"
                    f" Researcher--> {self.researcher}\n"
                    f" Score--> {self._score1}\n" 
                    f"number_of_Classes--> {self.number_of_classes}")

class1 = ClassificationExperiment(
    "Image Classification",
    "Loubid",
    0.95,
    5
)
print(class1.Report())