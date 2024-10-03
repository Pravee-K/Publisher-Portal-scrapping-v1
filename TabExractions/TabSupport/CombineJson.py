import json
from pathlib import Path
import os


def find_all_json_files(directory):
    json_files = dict()
    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a .json extension
            if file.endswith(".json"):
                json_files[os.path.basename(file)] = os.path.join(root, file)
    return json_files


def combine_json_files(file_paths: dict, output_file):
    combined_data = {}

    for key, val in file_paths.items():
        with open(val, 'r') as file:
            data = json.load(file)
            combined_data[key] = data

    with open(output_file, 'w') as output_json:
        json.dump(combined_data, output_json, indent=4)

    print(f"Combined JSON data has been saved to {output_file}")

current_file_path = os.path.dirname(os.path.abspath(__file__))

print(current_file_path)

json_files = find_all_json_files(os.path.join(current_file_path, 'data'))
print(json_files)

# json_files = {
#     'college info': os.path.join(current_file_path, 'data', 'file1.json'),
#     'Fees': os.path.join(current_file_path, 'data', 'file2.json'),
#     'Scholarship': os.path.join(current_file_path, 'data', 'file3.json')
# }
# print(json_files)

output_file = os.path.join(current_file_path, 'combined_output.json')

combine_json_files(json_files, output_file)



# Find and print all JSON files
print(f"Found JSON files: {json_files}")
