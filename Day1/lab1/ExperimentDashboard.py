class ExperimentDashboard():

    def __init__(self):
        self.experiments =[]

    def  add_experiment(self, experiment):
            for exp in self.experiments:
                 if exp.name == experiment.name:
                      raise ValueError("Experiment name already exists")
                 
            self.experiments.append(experiment)
             
    def show_reports(self):
         for experiment in self.experiments:
          print(experiment.Report())
          
    def best_experiment(self):
        best = self.experiments[0]

        for exp in self.experiments:
         if exp.score1 >best.score1:
             best=exp
        return best     