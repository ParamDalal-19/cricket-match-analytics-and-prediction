import os
import json
import pandas as pd

folder_path = "./ipl_data"  # Replace this with the path to your folder containing JSON files
json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

# List to store ball-by-ball data from all innings in all JSON files
all_innings_data = []
count = 0
# Loop through each JSON file in the folder
for file_name in json_files:
    count += 1
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract ball-by-ball data for each inning in the current JSON file
    innings_data = data.get("innings", [])
    # print("innings_data :-", innings_data)
    inning_number = 0



    for inning_info in innings_data:
        batting_team = inning_info.get("team", None)
        team = [data["info"]["teams"][0], data["info"]["teams"][1]]
        team.remove(batting_team)

        bowling_team = team[0]

        innings_overs = inning_info.get("overs", [])
        inning_number += 1
        Total = 0
        # List to store ball-by-ball data for the current inning
        inning_ball_by_ball_list = []
        is_super_over = 1 if inning_info.get("super_over", None) else 0

        for over_data in innings_overs:
            Delivery = 0
            over_number = over_data.get("over", None)
            deliveries = over_data.get("deliveries", [])

            for delivery_data in deliveries:
                batter = delivery_data.get("batter", None)
                bowler = delivery_data.get("bowler", None)
                Delivery += 1
                non_striker = delivery_data.get("non_striker", None)
                runs = delivery_data["runs"].get("batter", None)
                extras = delivery_data["runs"].get("extras", None)
                total_runs = delivery_data["runs"].get("total", None)
                Total += total_runs

                wicket_info = delivery_data.get("wickets", [])
                if wicket_info:
                    player_out = wicket_info[0].get("player_out", None)
                    wicket_kind = wicket_info[0].get("kind", None)
                    fielder_info = wicket_info[0].get("fielders", [])
                    fielder = fielder_info[0]["name"] if fielder_info else None
                else:
                    player_out, wicket_kind, fielder = None, None, None

                ball_info = {
                    "Match_id": count,
                    "Inning Number": inning_number,
                    "Batting_team": batting_team,
                    "Bowling_team": bowling_team,
                    "Over": over_number,
                    "Ball": Delivery,
                    "Batsman": batter,
                    "Non-Striker": non_striker,
                    "Bowler": bowler,
                    "is_super_over": is_super_over,
                    "player_dismissed": player_out,
                    "Total": total_runs,
                }

                inning_ball_by_ball_list.append(ball_info)

        all_innings_data.extend(inning_ball_by_ball_list)

# Create a DataFrame from the list of ball-by-ball data for all innings
ball_by_ball_df = pd.DataFrame.from_records(all_innings_data)

# Replace any missing values with "NaN"
ball_by_ball_df.fillna("NaN", inplace=True)

# # Display the DataFrame
print(ball_by_ball_df)

excel_file_path = 'deliveries.xlsx'  # Specify the path for the Excel file
ball_by_ball_df .to_excel(excel_file_path, index=False)  # Set index=False to exclude row numbers in Excel
