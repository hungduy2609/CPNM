#Ngọc Diệp đã sửa file
import numpy as np 
a = np.array([1,4,5,6])
print('one dim:\n',a)

b = np.array([[1,2,3,4],[5,6,7,8]])
print('two dim:\n',b)
print(b.shape)

d =  np.array([[[1,2,3,4],[3,4,5,6],[3,4,5,6]],[[2,3,4,4],[2,3,4,5],[2,3,4,5]]])
print('three dim with shape:\n',d.shape)

e = np.full((10),1)
print('\n dim array of size 10 and all values are 1 :',e)

f = np.random.randint(19,size=(2,3))
print('\n dim array(2,3) and cells values are real numbers in [5,19]',f)

g = np.random.randint(20,size=(2,3))
print('\n 2-dim array(2,3) and values are integers of [10,20] ',g)

a2 = np.array([[1,2,3,4],[5,6,7,8]])
print('\n get row number of A:',a2.shape[0])
print('\n get row number of A:',a2.shape[1])

a3 =  np.array([[[1,2,3,4],[3,4,5,6],[3,4,5,6]],[[2,3,4,4],[2,3,4,5],[2,3,4,5]]])
print('\n  create a 3-dim array and show its shape:',a3.shape)

a4 = [1,2,3]
print('\n list ',a4) 
arr = np.array(a4)
print('\n convert a -> :' ,arr)

a5 = np.array([1,2,3,4,5,6])
ac = np.reshape(a5, (-1, 2))
print('\n create an 1-dim array and convert it to 2-dim array with shape(m,n)',ac)

a = np.array([i for i in range(101)])
print('\n create an 1-dim array [1 2 .. 100]',a)
print('\n get sub-array containing 20 first elements:',a[:20])
print('\n get sub-array containing 20 last elements:',a[80:-1])

_A = [ [1, 2, 3, 4, 5], [6, 7, 8, 9 , 10] ] 
A = np.array(_A) 
print('create an matrix A like:',A)