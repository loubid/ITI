import numpy as np 
experiments = np.array(["E1", "E2", "E3", "E4", "E5"])
print(experiments) # Print the experiment names
print(experiments.shape)# Print the shape of the array(5,)
print(experiments.ndim)# 1  one dimension
print(experiments.size) # 5  total elements
print(experiments.dtype)# string dtype (e.g. '<U2')
print(type(experiments))# Print the type of the array
result=np.array([
    # E1    E2    E3    E4     E5
    [0.82, 0.91, 0.76, 0.88, 0.69],
    [0.78, 0.88, 0.81, 0.84, 0.72],
    [0.80, 0.90, 0.79, 0.86, 0.70]]).T

print(result) # Print array 
print(result.shape) # print number of rows and columns 
print(result.ndim) #print how many cerl btackets("[]"") (rows and columns)
print(result.size) # print number of elements in array (5x3)
print(result.dtype) # print data type of elemnts in array float64 
print(type(result)) #print types of result 
results_percent = result * 100
print ("Accuracy|percision|Recall")
print(results_percent)

print( "#"*10 +"  Part2  " +"#"*10)

#print Recall for E2 
print(results_percent[1,2])
#print all acuuracy col  
print(results_percent[:,0])
#print first three ACC and percision 
print(results_percent[0:3,0:2])

arr = np.arange(24)
print(arr)
print(arr.shape)
print("#"*30)
arr2=arr.reshape(4,6)
print(arr2)
print("shape after reshape:", arr2.shape)   # (4,6)

print("#"*30)

flat=arr2.ravel()
print(flat)
print("shape after ravel:", flat.shape)     # (24,)
print(results_percent)
print( "#"*10 +"  Part3  " +"#"*10)
print(results_percent.mean()) # Overall mean
print(results_percent.mean(axis=0)) #Mean of each metric

print(results_percent.mean(axis=1)) #Mean score of each experiment
print(results_percent.std())
print(results_percent.var())
print("std (original):", result.std())
print("var (original):", result.var())
print(result)
print( "#"*10 +"  Part4  " +"#"*10)
print(result)
print("#"*30)
filtered =result[
    (result[:,0]>=0.80) &
    (result[:,2]>=0.80)
]
print(filtered)
print("filtered shape:", filtered.shape)   
#add new raw 
print("#"*30)

new_experiment = np.array([[0.85, 0.83, 0.87]])
result = np.vstack((result, new_experiment)) # will add new raw at the end 
print(result)

print("#"*30)

#add new col 
F1=np.zeros((result.shape[0],1))
result = np.hstack((result, F1))
print(result)
print(result.shape)