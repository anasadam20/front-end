import pandas as pd

# User input: Enter the dates
dates = [
    '01-Apr', '05-03-2024', '5/15/2024', '05-01-2024', '05-01-2024', '5/15/2024', '05-10-2024', '05-10-2024',
    '5/20/2024', '5/17/2024', '4/26/2024', '5/17/2024', '5/28/2024', '5/16/2024', '5/28/2024', '5/15/2024',
    '5/28/2024', '5/15/2024', '5/15/2024', '5/15/2024', '5/15/2024', '5/15/2024', '5/15/2024', '5/15/2024',
    '5/15/2024', '5/15/2024', '5/15/2024', '5/15/2024', '5/24/2024', '5/15/2024', '5/15/2024', '5/15/2024',
    '5/15/2024', '5/15/2024', '5/28/2024', '5/28/2024', '04-10-2024', '04-10-2024', '04-10-2024', '04-12-2024',
    '04-12-2024', '4/15/2024', '4/15/2024', '4/15/2024', '4/18/2024', '4/19/2024', '4/19/2024', '4/19/2024',
    '4/26/2024', '4/30/2024', '4/30/2024', '4/30/2024', '4/30/2024', '4/30/2024', '4/30/2024', '05-01-2024',
    '05-01-2024', '05-01-2024', '05-01-2024', '05-03-2024', '05-03-2024', '05-03-2024', '05-04-2024', '05-08-2024',
    '5/27/2024', '5/27/2024', '4/30/2024'
]

# Convert 'Expiration Date' column to date-month-year format, handling 'NIL' values
formatted_dates = []
for date in dates:
    try:
        formatted_date = pd.to_datetime(date, errors='coerce').strftime('%d/%m/%Y')
        formatted_dates.append(formatted_date)
    except:
        formatted_dates.append('Invalid Date')

# Create DataFrame
df = pd.DataFrame({'Expiration Date': formatted_dates})

# Specify a valid directory path for your desktop
desktop_path = r'C:\Users\mohamed.sahulhameed\Desktop'  # Replace 'your_actual_username' with your actual username
csv_file_path = f'{desktop_path}\\converted_dates.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")
