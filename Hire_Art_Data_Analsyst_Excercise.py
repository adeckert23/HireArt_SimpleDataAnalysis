import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the data from excel into pandas dataframe
df = pd.read_excel('HireArt - Data Analyst Exercise 10.12.17.xlsx')

#checking the shape of the dataframe, 1001 rows x 3 columns
df.shape

#checking the head of the document to make sure it was imported correctly, especially the headers
df.head()

#checking to see the format of the columns.  Date of Contact is already formatted as a Datetime
df.info()

#Lets check the min and max to see how balanced this data set is
#I'd especially be concerned if the dataset is unbalanced and some months appear more often than others.
np.min(df['Date of Contact'])
#First date is 10/3/13
np.max(df['Date of Contact'])
#Last date is 9/29/17

#Graphing the data, to have an idea of the distribution.  I think a histogram will be a good visual for this.
plt.hist(x='Date of Contact', bins=48, data=df)
plt.ylabel('Count of Client Contacts')
plt.xlabel('Date of Contact by month')
plt.show()
#Conclusion after visualizing:
#After graphing, and knowing the dataset is balanced, the final numbers show
#October is our busiest month. October is close to double September, and close to triple most other months.
#There was no single October outlier that accounted for the outsized gains.

#This gets me the total visitors by month, regardless of year
#October has 213, September 121, and the rest between 52-80
df['Date of Contact'].dt.month.value_counts()

#This groups by year and month.  This would have been good if I didn't have the visual.
df['Date of Contact'].groupby(df['Date of Contact'].dt.to_period('M')).agg('count')
