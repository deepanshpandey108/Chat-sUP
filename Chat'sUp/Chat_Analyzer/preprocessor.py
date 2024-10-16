import re
import pandas as pd


def preprocess(data):
    pattern = r'\d{2}/\d{2}/\d{2,4}, \d{1,2}:\d{2}\u202f[apAP][mM]\s-\s'

    messages = re.split(pattern, data)
    dates = re.findall(pattern, data)

    print(f"Number of messages split: {len(messages)}")
    print(f"Number of dates found: {len(dates)}")

    # Ensure there is at least one message to process
    if not messages or not dates:
        print("Error: No messages or dates found.")
        return pd.DataFrame()  # Return an empty DataFrame

    # Check for mismatched lengths
    if len(messages) - 1 != len(dates):
        print(f"Warning: {len(messages) - 1} messages found, but {len(dates)} dates found.")
        # Append an empty string to messages to match the length
        messages.append("")  # Ensure lengths match

    # Create a DataFrame
    df = pd.DataFrame({'user_message': messages[:-1], 'message_date': dates})

    # Clean the 'message_date' column
    df['message_date'] = df['message_date'].str.replace('\u202f', ' ').str.strip(' -')

    # Convert 'message_date' to datetime with the correct format
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p', errors='coerce')

    # Rename column for consistency
    df.rename(columns={'message_date': 'date'}, inplace=True)

    user = []
    message_text = []

    # Iterate over the 'user_message' column
    for msg in df['user_message']:
        entry = re.split('([\w\W]+?):\s', msg)

        if len(entry) > 2:  # Valid split
            user.append(entry[1])
            message_text.append(entry[2])
        else:  # Malformed message
            user.append('group_notification')
            message_text.append(entry[0] if entry else "")

    # Add the extracted 'user' and 'message' columns to the DataFrame
    df['user'] = user
    df['message'] = message_text

    # Drop the original 'user_message' column
    df.drop(columns=['user_message'], inplace=True)

    # Extract year, month, day, hour, minute
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df  # Return the DataFrame for further processing
