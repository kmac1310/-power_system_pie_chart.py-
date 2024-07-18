import pandas as pd
import plotly.express as px

# Data for the 1440 Power System on a Weekday
activities = {
    'Sleep': 420,
    'Work': 540,
    'Gym': 60,
    'Study AI': 180,
    'Dinner': 60,
    'New Activity': 60
}

# Calculate remaining time
total_minutes_in_a_day = 1440
remaining_minutes = total_minutes_in_a_day - sum(activities.values())
activities['Remaining Time'] = remaining_minutes

# Creating DataFrame
data = pd.DataFrame({
    'Activity': activities.keys(),
    'Minutes': activities.values()
})

# Plotting Weekday Pie Chart
fig = px.pie(data, names='Activity', values='Minutes', title='1440 Power System: Weekday Activities')

# Save the plot as an HTML file
fig.write_html("power_system_pie_chart.html")

# Optionally, save as an image file
fig.write_image("power_system_pie_chart.png")

print("Pie chart has been saved as 'power_system_pie_chart.html' and 'power_system_pie_chart.png'")
