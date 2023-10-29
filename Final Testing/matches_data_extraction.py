import os
import json
import pandas as pd

folder_path = "./ipl_data"  # Replace this with the path to your folder containing JSON files
json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

# List to store extracted information from each JSON file
data_list = []
count = 0
# Loop through each JSON file in the folder
for file_name in json_files:
    count += 1
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(file_name)
    # column data
    id = count
    season = data["info"]["dates"][0].split("-")[0]

    try:
        city = data["info"]["city"]
    except:
        if data["info"]["venue"] == "Dubai International Cricket Stadium":
            city = "Dubai"
        elif data["info"]["venue"] == "Sharjah Cricket Stadium":
            city = "UAE"
        else:
            print("city error here :- ", file_name)

    date = data["info"]["dates"][0]
    team1 = data["info"]["teams"][0]
    team2 = data["info"]["teams"][1]
    toss_winner = data["info"]["toss"]["winner"]
    toss_decision = data["info"]["toss"]["decision"]

    try:
        winner = data["info"]["outcome"]["winner"]
    except:
        winner = data["info"]["outcome"]["result"]

    try:
        win_by_runs = data["info"]["outcome"]["by"]["runs"]
    except KeyError:
        win_by_runs = 0

    try:
        win_by_wickets = data["info"]["outcome"]["by"]["wickets"]
    except KeyError:
        win_by_wickets = 0
    try:
        player_of_match = data["info"]["player_of_match"][0]
    except:
        player_of_match = "no_one"

    venue = data["info"]["venue"]


    # Extract essential information from the current JSON file
    essential_info = {
        "id": id,
        "season": season,
        "city": city,
        "date": date,
        "team1": team1,
        "team2": team2,
        "toss_winner": toss_winner,
        "toss_decision": toss_decision,
        "winner": winner,
        "win_by_runs": win_by_runs,
        "win_by_wickets": win_by_wickets,
        "player_of_match": player_of_match,
        "venue": venue,
    }

    # Append the extracted information to the list
    data_list.append(essential_info)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Display the DataFrame
print(df)

excel_file_path = 'matches.xlsx'  # Specify the path for the Excel file
df.to_excel(excel_file_path, index=False)  # Set index=False to exclude row numbers in Excel

