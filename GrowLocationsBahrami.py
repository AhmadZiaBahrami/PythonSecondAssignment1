
# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import matplotlib.image as mpimg  # Add this line to import mpimg

# Load the Grow dataset
dataset_path = r'E:\Dundee_2023\First_Semester\ProgrammingLanguageForDataEngineering\Python\07-Assignment\SecondAssignment\Growlocations.csv'
df = pd.read_csv(dataset_path)

# Data Cleaning
# Assuming Latitude and Longitude columns are swapped, so correcting them
df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude']

# Filter out rows with bad values
df_cleaned = df[
    (df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985) &
    (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)
]

# Load the UK map image
map_image_path = r'E:\Dundee_2023\First_Semester\ProgrammingLanguageForDataEngineering\Python\07-Assignment\SecondAssignment\Demo1\map7.png'
uk_map = Image.open(map_image_path)

# Create an ImageDraw object to draw on the image
draw = ImageDraw.Draw(uk_map)

# Plot sensor locations on the map
for index, row in df_cleaned.iterrows():
    # Convert Latitude and Longitude to pixel coordinates (adjusted to keep within map boundaries)
    x = int((row['Longitude'] - (-10.592)) / (1.6848 - (-10.592)) * uk_map.width)
    y = int((row['Latitude'] - 50.681) / (57.985 - 50.681) * uk_map.height)

    # Ensure the points are within the image boundaries
    x = max(0, min(uk_map.width - 1, x))
    y = max(0, min(uk_map.height - 1, y))

    # Draw a point on the image
    draw.ellipse((x - 5, y - 5, x + 5, y + 5))

# Display the modified map image with sensor locations
# Create a subplot
fig, ax = plt.subplots()

# Load the map image
map_img = mpimg.imread(map_image_path)

# Plot the map image
ax.imshow(map_img, extent=[-10.592, 1.6848, 50.681, 57.985])

# Plot grow sensor locations
ax.scatter(df_cleaned['Longitude'], df_cleaned['Latitude'], marker='o', color='blue')

# Set labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Bahrami: Grow Sensor Locations on UK Map')
ax.legend()
ax.grid(True)

plt.show()
