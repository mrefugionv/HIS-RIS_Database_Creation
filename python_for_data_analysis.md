# PYTHON FOR DATA ANALYSIS
**Python for data analysis integrates data manipulation (pandas), visualization (seaborn), statistics (scipy), and machine learning (sklearn) into a complete workflow, from raw data to evaluated models.**
[[_LOC_]]


## LIBRARIES

### DATA ANALYSIS AND MANIPULATION
* Pandas for dataframe management: It provides high-level data structures and tools designed to make working with structured (tabular) and time-series data fast, flexible, and expressive.
* Numpy for arrays and numeric operations:  It provides high-performance multidimensional array objects and tools that are up to 50x faster than traditional Python lists for processing large datasets.
* Datetime for date data management.

```
import pandas as pd   
import numpy as np   
import datetime        
```


### VISUALIZATION

* Matplotlib for basic graphic creation: Matplotlib is the foundational library for data visualization in Python, used extensively in data analysis to create static, animated, and interactive plots. 
* Seaborn for advanced visualization: Boxplots, heatmaps.

```
from matplotlib import pyplot as plt    
import seaborn as sns                  
```

### STATISTICS 
* Scipy for statistics tests : t-test, ...
* Math for math functions : square (sqr), log...

```
from scipy import stats as st            
import math as mt                      
```

### MACHINE LEARNING
```
from sklearn.preprocessing import StandardScaler    # Dta Standarization
from sklearn.model_selection import train_test_split # Train/test data split
from sklearn.linear_model import LogisticRegression # Linear Classification
from sklearn.ensemble import RandomForestClassifier # Tree based model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score # Classificación parameters
from sklearn.cluster import KMeans #  kmeans method for clustering
from scipy.cluster.hierarchy import dendrogram, linkage # Dendogram graphic
```
