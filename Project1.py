#generate two random arrays. the first one uniformally distributed between -3 and 3; the second one normally distributed with mean 0 and std 1. 
#Find mean, std, min, max, Q1, Q2 and Q3 of the two arrays.
#Find out the portion of data with values lower than -2, -1.5, -1
#Draw two histograms in the same plot. 

import numpy as np 
import matplotlib.pyplot as plt

#funcions 
def mean(array):
	mean=0 
	for i in range(len(array)):
		mean=mean+(array[i])
	mean=mean/(len(array))
	return mean 

def std(array,mean):
	std=0 
	for i in range(len(array)):
		std=std+(array[i]-mean)*(array[i]-mean)
	std=std/len(array)
	std=np.sqrt(std)
	return std 

def m(array):
	m=array[0]
	for i in range(1,len(array)):
		if array[i]<m:
			m=array[i]
	return m
	
def M(array):
	M=array[0]
	for i in range(1,len(array)):
		if array[i]>M:
			M=array[i]
	return M 
	
def Q1(array):
	Q1=array[int((len(array)+1)/4)]
	return Q1	
	
def Q2(array):
	Q2=array[int((len(array)+1)/2)]
	return Q2
	
def Q3(array):
	Q3=array[int((len(array)+1)*3/4)]
	return Q3
	
def lower(array,x):
	a=0
	for i in range(len(array)):
		if array[i]<x:
			a=a+1
	lower=a/len(array)
	return lower
		
	
#creating arrays
np.random.seed(42)
array1=np.random.uniform(-3,3,1000)
array2=np.random.normal(0,1,1000)

#sorting arrays for Q1 Q2 Q3
array1=np.sort(array1)
array2=np.sort(array2)


#mean 
print('mean')
mean1=mean(array1)
print(mean1)
mean2=mean(array2)
print(mean2)

#std
print('std')
print(std(array1,mean1))
print(std(array2,mean2))
 
#minimum 
print('minimum')
print(m(array1))
print(m(array2))

#maximum 
print('maximum')
print(M(array1))
print(M(array2))

#Q1
print('Q1')
print(Q1(array1))
print(Q1(array2))

#Q2
print('Q2')
print(Q2(array1))
print(Q2(array2))

#Q3
print('Q3')
print(Q3(array1))
print(Q3(array2))

#lower -2
print('lower -2')
print(lower(array1,-2))
print(lower(array2,-2))

#lower -1.5
print('lower -1.5')
print(lower(array1,-1.5))
print(lower(array2,-1.5))

#lower -1
print('lower -1')
print(lower(array1,-1))
print(lower(array2,-1))

#histogram array1
plt.hist(array1,bins=20,alpha=0.5)
plt.hist(array2,bins=20,alpha=0.5)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Array1')
plt.show()
