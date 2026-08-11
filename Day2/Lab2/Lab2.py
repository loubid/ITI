import numpy as np 

class lab2:
    def __init__(self,Exnum,acc,percision,Recall):
        self.Exnum=Exnum
        self.acc=acc
        self.percision=percision
        self.Recall=Recall
        self.matrix=np.array([
        Exnum,
        acc,
        percision,
        Recall
        ]).T
exp=lab2(["E1","E2","E3","E4","E5"],
         [0.82,0.91,0.76,0.88,0.69],
         [0.78,0.88,0.81,0.84,0.72],
         [0.80,0.90,0.79,0.86,0.70]
         )

print( "#"*30 + "  Part1  " + "#"*30)

print(exp.matrix)
print(exp.matrix.shape) # (5,4) -> 5 experiments, 4 columns (name+3 metrics)
print(exp.matrix.ndim) # 2
print(exp.matrix.size) # 20
print(exp.matrix.dtype) # string dtype, because Exnum is mixed in
metrics = exp.matrix[:, 1:].astype(float) # just numbers 
print(type(exp.matrix))
metrics_percent = metrics * 100
print("Accuracy|Precision|Recall (percent):")
print(metrics_percent)
print()
print( "#"*30 + "  Part2  " + "#"*30)

#print Recall for E2 
print(metrics_percent[1, 2])

#print all acuuracy col  
print(metrics_percent[:, 0])

#print first three ACC and percision 
print(metrics_percent[0:3, 0:2])

arr = np.arange(24)
print(arr)
print("shape before reshape:", arr.shape)   # (24,)

arr2 = arr.reshape(4, 6)
print(arr2)
print("shape after reshape:", arr2.shape)   # (4,6)

flat = arr2.ravel()
print(flat)
print("shape after ravel:", flat.shape)     # (24,)

print()

print( "#"*30 + "  Part3  " + "#"*30)

print(metrics_percent.mean())            # Overall mean
print(metrics_percent.mean(axis=0))      # Mean of each metric
print(metrics_percent.mean(axis=1))      # Mean score of each experiment

print(metrics_percent.std())    # std on percentage values
print(metrics_percent.var())    # var on percentage values
print("std (original):", metrics.std())   # std on original 0-1 values
print("var (original):", metrics.var())   # var on original 0-1 values

print()

print( "#"*30 + "  Part4  " + "#"*30)

print(metrics)
print("#"*30)

#filter rows where Accuracy >= 0.80 AND Recall >= 0.80
filtered = metrics[
    (metrics[:, 0] >= 0.80) &
    (metrics[:, 2] >= 0.80)
]
print(filtered)
print("filtered shape:", filtered.shape)   # confirm still 3 columns

#add new raw 
print("#"*30)

new_experiment = np.array([[0.85, 0.83, 0.87]])
metrics = np.vstack((metrics, new_experiment)) # will add new raw at the end 
print(metrics)

print("#"*30)

#add new col 
F1 = np.zeros((metrics.shape[0], 1))
metrics = np.hstack((metrics, F1))
print(metrics)
print(metrics.shape)