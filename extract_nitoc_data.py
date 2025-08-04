import os
import json
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

path_to_data = os.getenv('PATH_TO_DATA')

# # Check if the path to the data exists
# if not os.path.exists(path_to_data):
#     print(f"Path to data does not exist: {path_to_data}")
# else:
#     # Print the contents of the path to the data
#     print(os.listdir(path_to_data))


# Create a list to store the NITOC tournaments
nitoc_tournaments = []
event_list = []

# For each file in the current directory
for file in os.listdir(path_to_data):
    if file.endswith('.json'):
        with open(os.path.join(path_to_data, file), 'r') as f:
            data = json.load(f)

            # For each tournament in the data
            for tournament in data:
                if 'National Invitational Tournament of Champions' in tournament['name']:
                    print("NITOC found: ", tournament['name'])
                    dict = {'name': tournament['name'], 'url': tournament['url'], 'state': tournament['state'], 'date': tournament['date']}
                    
                    for event in tournament['events']:
                        print("Event found: ", event['name'], "Population: ", event['population'])

                        if event['name'] not in event_list:
                            event_list.append(event['name'])

                        dict.update({event['name']: event['population']})

                    nitoc_tournaments.append(dict)





# Write the NITOC tournaments to a csv file, noting the year, and each event's population.
# If there is an event not offered in certain years, list it as 0.
# Columns: Year, State, and then columns for each event, with event name as the column name and population as the value.
# Write the csv to the current directory.

# Create a dataframe from the NITOC tournaments
nitoc_df = pd.DataFrame(nitoc_tournaments)

# Create a year column from date.
nitoc_df['year'] = nitoc_df['date'].str.split('-').str[0]
nitoc_df = nitoc_df.drop(columns=['date'])
nitoc_df = nitoc_df.sort_values(by='year')

# Create a dataframe from the events

# Write the dataframe to a csv file
nitoc_df.to_csv('nitoc_tournaments.csv', index=False)


