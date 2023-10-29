import os
import json
import pandas as pd

folder_path = "./ipl_data"  # Replace this with the path to your folder containing JSON files
json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

# List to store extracted information from each JSON file
data_list = []

# Loop through each JSON file in the folder
for file_name in json_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(file_name)
    # Extract essential information from the current JSON file
    essential_info = {
        "Date": data["info"]["dates"][0],
        "Venue": data["info"]["venue"],
        "Toss Winner": data["info"]["toss"]["winner"],
        "Toss Decision": data["info"]["toss"]["decision"],
        "Team 1": data["info"]["teams"][0],
        "Team 2": data["info"]["teams"][1]
    }

    # Append the extracted information to the list
    data_list.append(essential_info)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Display the DataFrame
print(df)
