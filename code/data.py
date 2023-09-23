import pandas as pd
import matplotlib.pyplot as plt
# Define the data as a dictionary
data = {'Year': [2018, 2019, 2020, 2021, 2022],
    	'E-Bikes sold in United States (1000s of units)': [369, 423, 416, 750, 928]}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the Year column as the index
df = df.set_index('Year')

# Create a list of years to use as the x-axis
years = range(df.index.min(), df.index.max()+1)

# Plot the data as a line graph
df.plot(kind='line', marker='o', xticks=years)

# Add title and labels to the graph
plt.title('E-Bikes sold in United States (1000s of units)')
plt.xlabel('Year')
plt.ylabel('Number of E-Bikes sold (1000s)')

# Display the graph
plt.show()
