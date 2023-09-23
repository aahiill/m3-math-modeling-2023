import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read in the data
data = {'Year': [2018, 2019, 2021, 2022],
    	'E-Bikes Sold': [369, 423, 750, 928]}
df = pd.DataFrame(data)

# Create the linear regression model with exponential moving average
ema_model = LinearRegression()
weights = pd.Series(0.05, index=range(len(df)))
# Weight of 0.3 to 2021
weights[df[df['Year'] == 2021].index[0]] = 0.1
# Weight of 0.5 to 2022
weights[df[df['Year'] == 2022].index[0]] = 0.5
X = df[['Year']]
y = df['E-Bikes Sold']
ema_model.fit(X, y, sample_weight=weights)

# Predict the number of e-bikes sold in 2 and 5 years

two_years = ema_model.predict([[2025]])
five_years = ema_model.predict([[2028]])

print(f"Predicted e-bikes sold in 2 years: {two_years[0]}")
print(f"Predicted e-bikes sold in 5 years: {five_years[0]}")

# Create a plot of the historical data and predicted values
x_values = list(range(2018, 2028))
y_values = ema_model.predict(pd.DataFrame(x_values, columns=['Year']))
plt.plot(x_values, y_values, label='Predicted Values')
plt.scatter(df['Year'], df['E-Bikes Sold'], color='red', label='Historical Data')
plt.legend()
plt.xlabel('Year')
plt.ylabel('E-Bikes Sold')
plt.title('Predicted E-Bike Sales Growth with EMA')
plt.show()
