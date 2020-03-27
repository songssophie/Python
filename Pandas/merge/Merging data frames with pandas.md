

```python
import pandas as pd
```

# Reading multiple files

**read seperatelly**


```python
df0 = pd.read_csv('sales-jan-2015.csv')
print(df0.head())
df0.shape
#other forms: pd.read_excel(),pd.read_html(),pd.read_json()
```

                      Date    Company   Product  Units
    0  2015-01-21 19:13:21  Streeplex  Hardware     11
    1  2015-01-09 05:23:51  Streeplex   Service      8
    2  2015-01-06 17:19:34    Initech  Hardware     17
    3  2015-01-02 09:51:06      Hooli  Hardware     16
    4  2015-01-11 14:51:02      Hooli  Hardware     11





    (20, 4)




```python
df1 = pd.read_csv('sales-feb-2015.csv')
print(df1.head())
df1.shape
```

                      Date    Company   Product  Units
    0  2015-02-26 08:57:45  Streeplex   Service      4
    1  2015-02-16 12:09:19      Hooli  Software     10
    2  2015-02-03 14:14:18    Initech  Software     13
    3  2015-02-02 08:33:01      Hooli  Software      3
    4  2015-02-25 00:29:00    Initech   Service     10





    (20, 4)




```python
merge1 = pd.concat([df0,df1],axis=0)
merge1.head()
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
      <th>Date</th>
      <th>Company</th>
      <th>Product</th>
      <th>Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-21 19:13:21</td>
      <td>Streeplex</td>
      <td>Hardware</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-09 05:23:51</td>
      <td>Streeplex</td>
      <td>Service</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-06 17:19:34</td>
      <td>Initech</td>
      <td>Hardware</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-02 09:51:06</td>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-11 14:51:02</td>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
merge2 = pd.concat([df0,df1],axis=1,keys=['Jan','Feb'])
merge2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">Jan</th>
      <th colspan="4" halign="left">Feb</th>
    </tr>
    <tr>
      <th></th>
      <th>Date</th>
      <th>Company</th>
      <th>Product</th>
      <th>Units</th>
      <th>Date</th>
      <th>Company</th>
      <th>Product</th>
      <th>Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-21 19:13:21</td>
      <td>Streeplex</td>
      <td>Hardware</td>
      <td>11</td>
      <td>2015-02-26 08:57:45</td>
      <td>Streeplex</td>
      <td>Service</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-09 05:23:51</td>
      <td>Streeplex</td>
      <td>Service</td>
      <td>8</td>
      <td>2015-02-16 12:09:19</td>
      <td>Hooli</td>
      <td>Software</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-06 17:19:34</td>
      <td>Initech</td>
      <td>Hardware</td>
      <td>17</td>
      <td>2015-02-03 14:14:18</td>
      <td>Initech</td>
      <td>Software</td>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-02 09:51:06</td>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>16</td>
      <td>2015-02-02 08:33:01</td>
      <td>Hooli</td>
      <td>Software</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-11 14:51:02</td>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>11</td>
      <td>2015-02-25 00:29:00</td>
      <td>Initech</td>
      <td>Service</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



**read using loops**


```python
filenames = ['sales-jan-2015.csv','sales-feb-2015.csv']
dataframe = []
```


```python
for file in filenames:
    dataframe.append(pd.read_csv(file,index_col='Date',parse_dates=True))
```


```python
salesT = pd.concat(dataframe,axis='rows')
salesT.head()
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
      <th>Company</th>
      <th>Product</th>
      <th>Units</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-01-21 19:13:21</th>
      <td>Streeplex</td>
      <td>Hardware</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2015-01-09 05:23:51</th>
      <td>Streeplex</td>
      <td>Service</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2015-01-06 17:19:34</th>
      <td>Initech</td>
      <td>Hardware</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2015-01-02 09:51:06</th>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2015-01-11 14:51:02</th>
      <td>Hooli</td>
      <td>Hardware</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



**using comprehension**


```python
filenames = ['sales-jan-2015.csv','sales-feb-2015.csv']
dataframe = [pd.read_csv(f) for f in filenames]
```

**using glob**


```python
from glob import glob
filenames=glob('sales*.csv')
dataframe=[pd.read_csv(f) for f in filenames]
```

# Reindexing DataFrames


```python
#read file
mydf = pd.read_csv('pittsburgh2013.csv')

#transfer Date to datetime, errors='coerce' can avoid following errors
mydf['Date'] = pd.to_datetime(mydf['Date'],errors='coerce')

#extract month from Date
mydf['month']=mydf['Date'].dt.month

#write to files
w_mean = mydf.loc[:,['month','Mean TemperatureF']]
w_mean.to_csv('w_mean.csv',index=False)

w_max = mydf.loc[:,['month','Max TemperatureF']]
w_max.to_csv('w_max.csv',index=False)
```


```python
import numpy as np
df2 = pd.read_csv('w_mean.csv',index_col='month')
df3 = df2.groupby('month').agg(np.mean)
df3
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53.100000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>62.612903</td>
    </tr>
    <tr>
      <th>6</th>
      <td>70.133333</td>
    </tr>
    <tr>
      <th>7</th>
      <td>72.870968</td>
    </tr>
    <tr>
      <th>8</th>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>63.766667</td>
    </tr>
    <tr>
      <th>10</th>
      <td>55.451613</td>
    </tr>
    <tr>
      <th>11</th>
      <td>39.800000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>34.935484</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = pd.read_csv('w_max.csv',index_col='month')
df5 = df4.groupby('month').max()
df5
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
      <th>Max TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>88</td>
    </tr>
    <tr>
      <th>6</th>
      <td>89</td>
    </tr>
    <tr>
      <th>7</th>
      <td>91</td>
    </tr>
    <tr>
      <th>8</th>
      <td>86</td>
    </tr>
    <tr>
      <th>9</th>
      <td>90</td>
    </tr>
    <tr>
      <th>10</th>
      <td>84</td>
    </tr>
    <tr>
      <th>11</th>
      <td>72</td>
    </tr>
    <tr>
      <th>12</th>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df3.index)
print(df5.index)
```

    Int64Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype='int64', name='month')
    Int64Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype='int64', name='month')


**reindex**


```python
ordered=[2,4,1,3,5,6,7,8,9,10,11,12]
df3.reindex(ordered)
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53.100000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>62.612903</td>
    </tr>
    <tr>
      <th>6</th>
      <td>70.133333</td>
    </tr>
    <tr>
      <th>7</th>
      <td>72.870968</td>
    </tr>
    <tr>
      <th>8</th>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>63.766667</td>
    </tr>
    <tr>
      <th>10</th>
      <td>55.451613</td>
    </tr>
    <tr>
      <th>11</th>
      <td>39.800000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>34.935484</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5.reindex(df3.index)
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
      <th>Max TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>88</td>
    </tr>
    <tr>
      <th>6</th>
      <td>89</td>
    </tr>
    <tr>
      <th>7</th>
      <td>91</td>
    </tr>
    <tr>
      <th>8</th>
      <td>86</td>
    </tr>
    <tr>
      <th>9</th>
      <td>90</td>
    </tr>
    <tr>
      <th>10</th>
      <td>84</td>
    </tr>
    <tr>
      <th>11</th>
      <td>72</td>
    </tr>
    <tr>
      <th>12</th>
      <td>68</td>
    </tr>
  </tbody>
</table>
</div>




```python
order1 = [1,2,13]
df6=df3.reindex(order1)
df6
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df7 = df6.dropna()
df7
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
  </tbody>
</table>
</div>




```python
df8 = df6.ffill()
df8
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.714286</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.sort_index()
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
      <th>Mean TemperatureF</th>
    </tr>
    <tr>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>32.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.714286</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53.100000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>62.612903</td>
    </tr>
    <tr>
      <th>6</th>
      <td>70.133333</td>
    </tr>
    <tr>
      <th>7</th>
      <td>72.870968</td>
    </tr>
    <tr>
      <th>8</th>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>63.766667</td>
    </tr>
    <tr>
      <th>10</th>
      <td>55.451613</td>
    </tr>
    <tr>
      <th>11</th>
      <td>39.800000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>34.935484</td>
    </tr>
  </tbody>
</table>
</div>



# Arithmetic with Series & DataFrames


```python
weather = pd.read_csv('pittsburgh2013.csv',index_col='Date',parse_dates=True)
weather.head()
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
      <th>Max TemperatureF</th>
      <th>Mean TemperatureF</th>
      <th>Min TemperatureF</th>
      <th>Max Dew PointF</th>
      <th>MeanDew PointF</th>
      <th>Min DewpointF</th>
      <th>Max Humidity</th>
      <th>Mean Humidity</th>
      <th>Min Humidity</th>
      <th>Max Sea Level PressureIn</th>
      <th>...</th>
      <th>Max VisibilityMiles</th>
      <th>Mean VisibilityMiles</th>
      <th>Min VisibilityMiles</th>
      <th>Max Wind SpeedMPH</th>
      <th>Mean Wind SpeedMPH</th>
      <th>Max Gust SpeedMPH</th>
      <th>PrecipitationIn</th>
      <th>CloudCover</th>
      <th>Events</th>
      <th>WindDirDegrees</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>32</td>
      <td>28</td>
      <td>21</td>
      <td>30</td>
      <td>27</td>
      <td>16</td>
      <td>100</td>
      <td>89</td>
      <td>77</td>
      <td>30.10</td>
      <td>...</td>
      <td>10</td>
      <td>6</td>
      <td>2</td>
      <td>10</td>
      <td>8</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>8</td>
      <td>Snow</td>
      <td>277</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>25</td>
      <td>21</td>
      <td>17</td>
      <td>14</td>
      <td>12</td>
      <td>10</td>
      <td>77</td>
      <td>67</td>
      <td>55</td>
      <td>30.27</td>
      <td>...</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>14</td>
      <td>5</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>4</td>
      <td>NaN</td>
      <td>272</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>32</td>
      <td>24</td>
      <td>16</td>
      <td>19</td>
      <td>15</td>
      <td>9</td>
      <td>77</td>
      <td>67</td>
      <td>56</td>
      <td>30.25</td>
      <td>...</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>17</td>
      <td>8</td>
      <td>26.0</td>
      <td>0.00</td>
      <td>3</td>
      <td>NaN</td>
      <td>229</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>30</td>
      <td>28</td>
      <td>27</td>
      <td>21</td>
      <td>19</td>
      <td>17</td>
      <td>75</td>
      <td>68</td>
      <td>59</td>
      <td>30.28</td>
      <td>...</td>
      <td>10</td>
      <td>10</td>
      <td>6</td>
      <td>23</td>
      <td>16</td>
      <td>32.0</td>
      <td>0.00</td>
      <td>4</td>
      <td>NaN</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>34</td>
      <td>30</td>
      <td>25</td>
      <td>23</td>
      <td>20</td>
      <td>16</td>
      <td>75</td>
      <td>68</td>
      <td>61</td>
      <td>30.42</td>
      <td>...</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>16</td>
      <td>10</td>
      <td>23.0</td>
      <td>0.21</td>
      <td>5</td>
      <td>NaN</td>
      <td>221</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>




```python
weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn']
```




    Date
    2013-07-01    0.18
    2013-07-02    0.14
    2013-07-03    0.00
    2013-07-04    0.25
    2013-07-05    0.02
    2013-07-06    0.06
    2013-07-07    0.10
    Name: PrecipitationIn, dtype: float64



**scalar multiplication**


```python
weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn']*2.5
```




    Date
    2013-07-01    0.450
    2013-07-02    0.350
    2013-07-03    0.000
    2013-07-04    0.625
    2013-07-05    0.050
    2013-07-06    0.150
    2013-07-07    0.250
    Name: PrecipitationIn, dtype: float64



**Relative temperature range**


```python
week1_range = weather.loc['2013-7-1':'2013-7-7',['Min TemperatureF','Max TemperatureF']]
week1_range
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
      <th>Min TemperatureF</th>
      <th>Max TemperatureF</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-07-01</th>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>2013-07-02</th>
      <td>66</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2013-07-03</th>
      <td>71</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-04</th>
      <td>70</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-05</th>
      <td>69</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-06</th>
      <td>70</td>
      <td>89</td>
    </tr>
    <tr>
      <th>2013-07-07</th>
      <td>70</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>




```python
#replace F in columns' name to Fa
week1_range.columns = week1_range.columns.str.replace('F','Fa')
week1_range
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
      <th>Min TemperatureFa</th>
      <th>Max TemperatureFa</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-07-01</th>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>2013-07-02</th>
      <td>66</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2013-07-03</th>
      <td>71</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-04</th>
      <td>70</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-05</th>
      <td>69</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2013-07-06</th>
      <td>70</td>
      <td>89</td>
    </tr>
    <tr>
      <th>2013-07-07</th>
      <td>70</td>
      <td>77</td>
    </tr>
  </tbody>
</table>
</div>




```python
week1_mean = weather.loc['2013-7-1':'2013-7-7','Mean TemperatureF']
week1_mean
```




    Date
    2013-07-01    72
    2013-07-02    74
    2013-07-03    78
    2013-07-04    77
    2013-07-05    76
    2013-07-06    78
    2013-07-07    72
    Name: Mean TemperatureF, dtype: int64




```python
#if we want to obtian week1_range/week1_mean, we cannot calculate directly
week1_range/week1_mean
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
      <th>2013-07-01 00:00:00</th>
      <th>2013-07-02 00:00:00</th>
      <th>2013-07-03 00:00:00</th>
      <th>2013-07-04 00:00:00</th>
      <th>2013-07-05 00:00:00</th>
      <th>2013-07-06 00:00:00</th>
      <th>2013-07-07 00:00:00</th>
      <th>Max TemperatureF</th>
      <th>Min TemperatureF</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-07-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-07-07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
week1_range.divide(week1_mean,axis='rows')
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
      <th>Min TemperatureF</th>
      <th>Max TemperatureF</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-07-01</th>
      <td>0.916667</td>
      <td>1.097222</td>
    </tr>
    <tr>
      <th>2013-07-02</th>
      <td>0.891892</td>
      <td>1.135135</td>
    </tr>
    <tr>
      <th>2013-07-03</th>
      <td>0.910256</td>
      <td>1.102564</td>
    </tr>
    <tr>
      <th>2013-07-04</th>
      <td>0.909091</td>
      <td>1.116883</td>
    </tr>
    <tr>
      <th>2013-07-05</th>
      <td>0.907895</td>
      <td>1.131579</td>
    </tr>
    <tr>
      <th>2013-07-06</th>
      <td>0.897436</td>
      <td>1.141026</td>
    </tr>
    <tr>
      <th>2013-07-07</th>
      <td>0.972222</td>
      <td>1.069444</td>
    </tr>
  </tbody>
</table>
</div>



**Percentage changes**


```python
week1_mean.pct_change()*100
```




    Date
    2013-07-01         NaN
    2013-07-02    2.777778
    2013-07-03    5.405405
    2013-07-04   -1.282051
    2013-07-05   -1.298701
    2013-07-06    2.631579
    2013-07-07   -7.692308
    Name: Mean TemperatureF, dtype: float64



## Adding


```python
gold = pd.read_csv('gold_top5.csv',index_col=0)
silver = pd.read_csv('silver_top5.csv',index_col=0)
bronze = pd.read_csv('bronze_top5.csv',index_col=0)
```


```python
gold+silver
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
      <th>Total</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>854.0</td>
    </tr>
    <tr>
      <th>Soviet Union</th>
      <td>1465.0</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>1089.0</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>3283.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
gold.add(silver,fill_value=0)
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
      <th>Total</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>461.0</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>407.0</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>854.0</td>
    </tr>
    <tr>
      <th>Soviet Union</th>
      <td>1465.0</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>1089.0</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>3283.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
gold+silver+bronze
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
      <th>Total</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Soviet Union</th>
      <td>2049.0</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>1594.0</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>4335.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
gold.add(silver,fill_value=0).add(bronze,fill_value=0)
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
      <th>Total</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>936.0</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>861.0</td>
    </tr>
    <tr>
      <th>Italy</th>
      <td>854.0</td>
    </tr>
    <tr>
      <th>Soviet Union</th>
      <td>2049.0</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>1594.0</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>4335.0</td>
    </tr>
  </tbody>
</table>
</div>


