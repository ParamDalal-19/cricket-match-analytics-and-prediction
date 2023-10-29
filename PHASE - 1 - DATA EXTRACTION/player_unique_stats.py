import pandas as pd

data = pd.read_excel("player_stats.xlsx")
dct = {} # { [ total match played 0, total innings played 1, total not outs 2, total run 3, highest score 4, total balls faced 5, strike rate 6, hundred 7, fifty 8, four 9, six 10] }

for idx, val in data.iterrows():
    try:
        if dct[val[1]]:
            ls = [0,1,2,3,5,7,8,9,10]
            plc = [2,3,4,5,7,9,10,11,12]
            for j in range(0, len(ls)):
                if val[plc[j]] != "teju":
                    if dct[val[1]][ls[j]] != "teju":
                        dct[val[1]][ls[j]] += float(val[plc[j]])
                    else:
                        dct[val[1]][ls[j]] = float(val[plc[j]])

            if val[6] != "teju":

                nm = float((val[6])[:-1]) if str(val[6])[-1] == "*" else float(val[6])

                if dct[val[1]][4] != "teju":
                    if nm > float(dct[val[1]][4]):
                        dct[val[1]][4] = nm
                else:
                    dct[val[1]][4] = nm

            if dct[val[1]][6] == "teju":
                if val[8] != "teju":
                    dct[val[1]][6] = float(val[8])
    except KeyError:
        plc1 = [2,3,4,5,6,7,8,9,10,11,12]
        dct[val[1]] = [float((val[6][:-1])) if str(val[6])[-1] == "*" and str(val[6]) != "teju" else (float(val[p]) if val[p] != "teju" else val[p]) if p == 6 else (float(val[p]) if val[p] != "teju" else val[p]) for p in plc1]


# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(dct, orient='index',
                            columns=['Total Matches', 'Total Innings', 'Total Not Outs', 'Total Runs',
                                     'Highest Score', 'Total Balls Faced', 'Strike Rate', 'Hundreds', 'Fifties', 'Fours', 'Sixes'])

# Add a new column 'Player Name'
df['Player Name'] = df.index

# Reorder the columns
column_order = ['Player Name', 'Total Matches', 'Total Innings', 'Total Not Outs', 'Total Runs',
                'Highest Score', 'Total Balls Faced', 'Strike Rate', 'Hundreds', 'Fifties', 'Fours', 'Sixes']
df = df[column_order]

# Create an Excel writer
excel_writer = pd.ExcelWriter('unique_player_data.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel sheet
df.to_excel(excel_writer, sheet_name='Player Stats', index=False)

# Save the Excel file
excel_writer.save()

