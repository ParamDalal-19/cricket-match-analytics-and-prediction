import os
import json
import pandas as pd

folder_path = "./ipl_data"  # Replace this with the path to your folder containing JSON files
json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

# List to store extracted information from each JSON file
data_list = []
all_player_year_data = []
# Loop through each JSON file in the folder
file_count = 0
for file_name in json_files:
    file_count += 1
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)

    info_data = data.get("info", [])
    team_data = info_data.get("players", [])
    player_year_list = []
    player_count = 0
    for team in team_data:
        player_data = team_data.get(team, [])
        for player in player_data:
            player_count += 1
            row_info = {
                "Match": file_name.replace(".json", ""),
                "Player short name": player,
                "Match full date": info_data.get("dates")[0],
                "Match year": info_data.get("dates")[0].split("-")[0],
                "Match month": info_data.get("dates")[0].split("-")[1],
                "Match day": info_data.get("dates")[0].split("-")[2]
            }
            player_year_list.append(row_info)
        all_player_year_data.extend(player_year_list)
    if player_count != 22:
        print(file_name.replace(".json", ""))
# Create a DataFrame from the list of dictionaries
# df = pd.DataFrame.from_records(all_player_year_data)

# Display the DataFrame
# print(df.head())

print(file_count)
# excel_file_path = 'player_year.xlsx'  # Specify the path for the Excel file
# df.to_excel(excel_file_path, index=False)  # Set index=False to exclude row numbers in Excel
