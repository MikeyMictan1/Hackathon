import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Step 1: Read the CSV file
df = pd.read_csv('stockMarket.csv')
names = {"Brown's Bakery": ["Brown's Bakery"],
         'Capital One': ['Capital One'],
         'Chip NFT': ['Chip NFT'],
         'Chipdo': ["Chipdo"],
       }
dfExtra = pd.DataFrame(names)
df = pd.concat([dfExtra, df], ignore_index = True)
df.reset_index()
df.rename(index={0:'Stock', 1: 'Price', 2:'Stability', 3:'Stocks Owned', 4:'Change'}, inplace=True)
df = df.transpose()
df.drop('Unnamed: 0',axis=0,inplace=True)

for index, row in df.iterrows():
    if row['Stability'] == 'True':
        row['Stability'] = 'Safe'
    if row['Stability'] == 'False':
        row['Stability'] = 'Unstable'

    if row['Change'] == 'True':
        row['Change'] = '↑'
    if row['Change'] == 'False':
        row['Change'] = '↓'
    if row['Change'] == 'none':
        row['Change'] = '-'


# Step 2: Create a table using matplotlib
fig, ax = plt.subplots(figsize=(10, len(df)*0.4 + 1))  # Adjust the size accordingly
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Adjust the font size and cell dimensions if needed
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)  # You can adjust the scaling factor
# Customize the background colors
# Set background color for header row
header_color = '#769974'  # Light gray for the header
for i, col in enumerate(df.columns):
     table[0, i].set_facecolor(header_color)

# Set background color for all cells
cell_color = '#a7cca5'  # Light background for cells
for row in range(1, len(df) + 1):
    for col in range(len(df.columns)):
        table[row, col].set_facecolor(cell_color)
# Save the table as an image
plt.savefig('stockMarket.png', bbox_inches='tight', dpi=300)

# Open the saved image and display it
img = Image.open('stockMarket.png')
img.show()
