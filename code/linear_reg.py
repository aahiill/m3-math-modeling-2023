import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read in the data
# Code for LinearReg2 is the same; only 2020 and its corresponding data is omitted
data = {'Year': [2018, 2019, 2020, 2021, 2022],
    	'E-Bikes Sold': [369, 423, 416, 750, 928]}
df = pd.DataFrame(data)

# Create the linear regression model
lr_model = LinearRegression()
X = df[['Year']]
y = df['E-Bikes Sold']
lr_model.fit(X, y)

# Predict the number of e-bikes sold in 2 and 5 years
two_years = lr_model.predict([[2025]])
five_years = lr_model.predict([[2028]])
print(f"Predicted e-bikes sold in 2 years: {two_years[0]}")
print(f"Predicted e-bikes sold in 5 years: {five_years[0]}")

# Create a plot of the historical data and predicted values
x_values = list(range(2018, 2028))
y_values = lr_model.predict(pd.DataFrame(x_values, columns=['Year']))
plt.plot(x_values, y_values, label='Predicted Values')
plt.scatter(df['Year'], df['E-Bikes Sold'], color='red', label='Historical Data')
plt.legend()
plt.xlabel('Year')
plt.ylabel('E-Bikes Sold')
plt.title('Predicted E-Bike Sales Growth')
plt.show()
