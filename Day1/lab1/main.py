from Experiment import Experiment
from ClassificationExperiment import ClassificationExperiment
from RetrievalExperiment import RetrievalExperiment
from ExperimentDashboard import ExperimentDashboard
# Create experiments
exp1 = ClassificationExperiment(
    "Image Classification",
    "Loubid",
    0.83,
    5
)

exp2 = RetrievalExperiment(
    "Arabic RAG Search",
    "Ahmed",
    0.91,
    10
)


exp3 = ClassificationExperiment(
    "Sentiment Analysis",
    "Mohamed",
    0.87,
    3
)

exp4 = RetrievalExperiment(
    "Arabic RAG Search",
    "Ahmed",
    0.91,
    10
)


# Create dashboard
dashboard = ExperimentDashboard()
# Add experiments
dashboard.add_experiment(exp1)
dashboard.add_experiment(exp2)
dashboard.add_experiment(exp3)
#dashboard.add_experiment(exp4)#for check Bouns 

# Show reports
print("----- EXPERIMENT REPORTS ----\n")

dashboard.show_reports()


# Best experiment
print("\n-----BEST EXPERIMENT -----\n")
best = dashboard.best_experiment()
print("Name:", best.name)
print("Researcher:", best.researcher)
print("Score:", best.score1)