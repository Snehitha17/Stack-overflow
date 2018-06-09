import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
from plotly.offline import iplot
import warnings
warnings.filterwarnings("ignore")
import cufflinks as cf
cf.go_offline()

stack_data = pd.read_csv('F:sneha files/python/stack overflow/survey_results_public.csv')
schema = pd.read_csv('F:sneha files/python/stack overflow/survey_results_schema.csv')

stack_data.head()
schema.head()

stack_data.describe()

stack_data.info()

total = stack_data.isnull().sum().sort_values(ascending = False)
percent = (stack_data.isnull().sum()/stack_data.isnull().count()*100).sort_values(ascending = False)
missing_stack  = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_stack

