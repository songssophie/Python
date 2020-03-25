
# Introduction to Python - basic numpy


```python
import numpy as np
```

## Calculation


```python
#np array, unlike list, can caculate every element in the array for two arrays
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_height = np.array(height)
np_weight = np.array(weight)
```


```python
print(np_height)
print(np_weight)
```

    [1.73 1.68 1.71 1.89 1.79]
    [65.4 59.2 63.6 88.4 68.7]



```python
np_weight/np_height**2
```




    array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])




```python
weight/height**2 #this is one disadvantage for list
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-87f65dbe42f3> in <module>
    ----> 1 weight/height**2
    

    TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'



```python
weight+height #extend list
```




    [65.4, 59.2, 63.6, 88.4, 68.7, 1.73, 1.68, 1.71, 1.89, 1.79]




```python
np_weight+np_height #perform calculation
```




    array([67.13, 60.88, 65.31, 90.29, 70.49])




```python
#np array only contain one type
np.array([1,"type",True])
```




    array(['1', 'type', 'True'], dtype='<U21')



## Subsetting


```python
bmi = np_weight/np_height**2
bmi[0]
```




    21.85171572722109




```python
bmi>23
```




    array([False, False, False,  True, False])




```python
height < 1 # one of the difference of list and array
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-c00dd4fe5234> in <module>
    ----> 1 height < 1
    

    TypeError: '<' not supported between instances of 'list' and 'int'



```python
bmi[bmi>23]
```




    array([24.7473475])



## 2D numpy arrays

### Types


```python
type(np_height)
```




    numpy.ndarray




```python
np_2d = np.array([height,weight])
print(np_2d)
```

    [[ 1.73  1.68  1.71  1.89  1.79]
     [65.4  59.2  63.6  88.4  68.7 ]]



```python
type(np_2d)
```




    numpy.ndarray




```python
np_2d.shape #no brackets
```




    (2, 5)



### subsetting


```python
np_2d[0]
```




    array([1.73, 1.68, 1.71, 1.89, 1.79])




```python
np_2d[0,1]
```




    1.68




```python
np_2d[0][1]
```




    1.68




```python
np_2d[:,3:4]
```




    array([[ 1.89],
           [88.4 ]])




```python
np_2d[:,3:]
```




    array([[ 1.89,  1.79],
           [88.4 , 68.7 ]])



## Basic statistics


```python
np.mean(np_2d[0])
```




    1.7600000000000002




```python
np.median(np_2d[0,:])
```




    1.73




```python
np.corrcoef(np_2d[0],np_2d[1])
```




    array([[1.        , 0.97514969],
           [0.97514969, 1.        ]])




```python
np.std(np_2d[1])
```




    10.14487062509917




```python
np.sum(np_2d[1])
```




    345.3




```python
np.sort(np_2d[1])
```




    array([59.2, 63.6, 65.4, 68.7, 88.4])




```python
np.random.normal(0,4,50) #argument: mean, std, number
```




    array([ 3.68854216, -0.21329036,  8.61126405,  4.91062166, -0.67651883,
            6.19576935,  1.28882138,  6.30871079,  2.43007649, -6.90666665,
           -0.23631822,  6.36811662, -1.47022685, -0.64192573, -5.17991577,
           -1.37770443, -4.5513869 ,  0.42087609,  1.43565444, -3.18885366,
            4.3683576 , -3.62774883, -7.42223169,  1.01106689,  0.67741423,
           -1.21572357, -2.75238801, -1.31013177,  3.34150357,  1.85105916,
            0.07719944,  4.58574064, -7.88722593, -0.12278556,  1.35101677,
            6.05442984, -1.18503423, -3.17891162,  1.25110056, -4.14233435,
            1.86313391, -2.65099422,  2.05855116, -5.75372793, -2.01504722,
           -6.56012957,  2.76362613,  7.0559426 , -8.43142342, -3.55341382])




```python
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height,weight))
print(np_city)
```

    [[ 1.89 40.65]
     [ 1.89 34.95]
     [ 1.5  43.03]
     ...
     [ 1.86 66.48]
     [ 1.7  66.63]
     [ 1.88 71.44]]

