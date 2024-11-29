import pandas as pd
from IPython.display import display
  # create a simple dataset of people
data = {'Name': ["Gala", "Lily", "Nicole", "Linda"],
          'Location' : ["New York", "New York", "Mexico", "London"],
          'Age' : [7, 7, 15, 33]
}
data_pandas = pd.DataFrame(data)
# IPython.display allows "pretty printing" of dataframes # in the Jupyter notebook
display(data_pandas)
#Looks prettier in Jupiter
display(data_pandas[data_pandas.Age > 30])
#this only displays all ages greater than 30, keeps indices the same