import pandas as pd
import json

def excel_to_json(excel_file):
    # Read Excel file into a DataFrame
    with open(excel_file, 'rb') as file:
        df = pd.read_excel(file)
    
    # Convert DataFrame to JSON
    json_data = []
    for index, row in df.iterrows():
        input_value = row["input"] if pd.notna(row["input"]) else ""  # Check if input value is not NaN
        item = {
            "instruction": row["instruction"],
            "input": input_value,
            "output": row["output"]
        }
        json_data.append(item)
    
    return json_data

# Example usage:
excel_file = "data/khmer_alpaca_data.xlsx"  # Specify the Excel file name
json_data = excel_to_json(excel_file)

# Export JSON data to file
with open('data/khmer_alpaca_data.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print("Conversion successful. JSON data saved as: khmer_alpaca_data.json")
