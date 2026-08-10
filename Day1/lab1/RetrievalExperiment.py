from Experiment import Experiment

class RetrievalExperiment(Experiment):

    def __init__(self,name,researcher,score, top_k):
        super().__init__(name,researcher,score)
        self.top_k=top_k
#@Override

    def Report(self):
                return (f"Esperimnet--> {self.name}\n"
                f"Researcher--> {self.researcher}\n"
                f"Score--> {self._score1}\n"
                f"top_k--> {self.top_k}")

# rert1 = RetrievalExperiment(
#     "Document Retrieval",
#     "Ahmed",
#     0.88,
#     10
# )
# print(rert1.Report())
