

```python
import pandas as pd
```

## Obtain data frame

**Data frame from dictionary**


```python
dictionary = {"country":["Brazil", "Russia", "India", "China", "South Africa"], 
        "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"], 
        "area":[8.516, 17.10, 3.286, 9.597, 1.221],
        "population":[200.4, 143.5, 1252, 1357, 52.98]}
```


```python
brics = pd.DataFrame(dictionary)
brics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>India</td>
      <td>New Delhi</td>
      <td>3.286</td>
      <td>1252.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>South Africa</td>
      <td>Pretoria</td>
      <td>1.221</td>
      <td>52.98</td>
    </tr>
  </tbody>
</table>
</div>



**Data frame from csv**


```python
brics = pd.read_csv("brics.csv")
brics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BR</td>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RU</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>IN</td>
      <td>India</td>
      <td>New Delhi</td>
      <td>3.286</td>
      <td>1252.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CH</td>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SA</td>
      <td>South Africa</td>
      <td>Pretoria</td>
      <td>1.221</td>
      <td>52.98</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics = pd.read_csv("brics.csv",index_col=0)
brics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.40</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.50</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
      <td>New Delhi</td>
      <td>3.286</td>
      <td>1252.00</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.00</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>South Africa</td>
      <td>Pretoria</td>
      <td>1.221</td>
      <td>52.98</td>
    </tr>
  </tbody>
</table>
</div>



## Index and select


```python
brics["country"]
```




    BR          Brazil
    RU          Russia
    IN           India
    CH           China
    SA    South Africa
    Name: country, dtype: object




```python
type(brics["country"]) #1D labelled array
```




    pandas.core.series.Series




```python
brics[["country"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>South Africa</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(brics[["country"]])
```




    pandas.core.frame.DataFrame




```python
brics[["country","capital"]] #extract colums
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
      <td>New Delhi</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>South Africa</td>
      <td>Pretoria</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics[1:4] #extrac rows
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.5</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
      <td>New Delhi</td>
      <td>3.286</td>
      <td>1252.0</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use loc to extract rows, loc-label
brics.loc["RU"]
```




    country       Russia
    capital       Moscow
    area            17.1
    population     143.5
    Name: RU, dtype: object




```python
type(brics.loc["RU"])
```




    pandas.core.series.Series




```python
brics.loc[["RU"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.1</td>
      <td>143.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics.loc[["RU","CH"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.5</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics.loc[["RU","CH"],["country","capital"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics.loc[:,["country","capital"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
      <td>New Delhi</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>South Africa</td>
      <td>Pretoria</td>
    </tr>
  </tbody>
</table>
</div>




```python
#use iloc
brics.iloc[:,[1,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>capital</th>
      <th>area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brasilia</td>
      <td>8.516</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Moscow</td>
      <td>17.100</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>New Delhi</td>
      <td>3.286</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>Beijing</td>
      <td>9.597</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>Pretoria</td>
      <td>1.221</td>
    </tr>
  </tbody>
</table>
</div>




```python
brics.iloc[[0,2,4],[1,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>capital</th>
      <th>area</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brasilia</td>
      <td>8.516</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>New Delhi</td>
      <td>3.286</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>Pretoria</td>
      <td>1.221</td>
    </tr>
  </tbody>
</table>
</div>



## Filter


```python
brics["area"]
```




    BR     8.516
    RU    17.100
    IN     3.286
    CH     9.597
    SA     1.221
    Name: area, dtype: float64




```python
brics["area"]>8
```




    BR     True
    RU     True
    IN    False
    CH     True
    SA    False
    Name: area, dtype: bool




```python
is_huge = brics["area"]>8
brics[is_huge]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.4</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.5</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
```


```python
condition = np.logical_and(brics["area"]>8,brics["area"]<10)
brics[condition]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.4</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.0</td>
    </tr>
  </tbody>
</table>
</div>



## Loops


```python
for i in brics:
    print(i)
```

    country
    capital
    area
    population



```python
for m,n in brics.iterrows():
    print(m)
    print(n)
```

    BR
    country         Brazil
    capital       Brasilia
    area             8.516
    population       200.4
    Name: BR, dtype: object
    RU
    country       Russia
    capital       Moscow
    area            17.1
    population     143.5
    Name: RU, dtype: object
    IN
    country           India
    capital       New Delhi
    area              3.286
    population         1252
    Name: IN, dtype: object
    CH
    country         China
    capital       Beijing
    area            9.597
    population       1357
    Name: CH, dtype: object
    SA
    country       South Africa
    capital           Pretoria
    area                 1.221
    population           52.98
    Name: SA, dtype: object


**selective print**


```python
for m,n in brics.iterrows():
    print(m+":"+n["capital"])
```

    BR:Brasilia
    RU:Moscow
    IN:New Delhi
    CH:Beijing
    SA:Pretoria


**Add column**


```python
for m,n in brics.iterrows():
    brics.loc[m,"name_length"]=len(n["capital"])
print(brics)
```

             country    capital    area  population  name_length
    BR        Brazil   Brasilia   8.516      200.40          8.0
    RU        Russia     Moscow  17.100      143.50          6.0
    IN         India  New Delhi   3.286     1252.00          9.0
    CH         China    Beijing   9.597     1357.00          7.0
    SA  South Africa   Pretoria   1.221       52.98          8.0


**Apply function**


```python
brics = pd.read_csv("brics.csv",index_col=0)
```


```python
brics["name_length"]=brics["capital"].apply(len)
```


```python
brics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>capital</th>
      <th>area</th>
      <th>population</th>
      <th>name_length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BR</th>
      <td>Brazil</td>
      <td>Brasilia</td>
      <td>8.516</td>
      <td>200.40</td>
      <td>8</td>
    </tr>
    <tr>
      <th>RU</th>
      <td>Russia</td>
      <td>Moscow</td>
      <td>17.100</td>
      <td>143.50</td>
      <td>6</td>
    </tr>
    <tr>
      <th>IN</th>
      <td>India</td>
      <td>New Delhi</td>
      <td>3.286</td>
      <td>1252.00</td>
      <td>9</td>
    </tr>
    <tr>
      <th>CH</th>
      <td>China</td>
      <td>Beijing</td>
      <td>9.597</td>
      <td>1357.00</td>
      <td>7</td>
    </tr>
    <tr>
      <th>SA</th>
      <td>South Africa</td>
      <td>Pretoria</td>
      <td>1.221</td>
      <td>52.98</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>


