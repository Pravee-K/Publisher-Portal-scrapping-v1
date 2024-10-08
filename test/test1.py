import os

# Given file path
file_path = r"C:\Users\Admin\Documents\Work\XtraCut_Works\Publisher-Portal-scrapping-v1\TabExractions\TabSupport\data\InputData\Top100Clgs.txt"

# Step 1: Get the directory containing the file
directory_path = os.path.dirname(file_path)

# Step 2: Navigate to the parent directory using '..'
parent_directory = os.path.abspath(os.path.join(directory_path, '..', '..'))

# Step 3: Create the 'Output' directory in the parent directory
output_directory = os.path.join(parent_directory, 'Output')
os.makedirs(output_directory, exist_ok=True)

# Step 4: Generate a new path inside the 'Output' directory for the file
new_file_name = "NewGeneratedFile.txt"
new_file_path = os.path.join(output_directory, new_file_name)

# Print the paths for verification
print("Original file path:", file_path)
print("Parent directory path:", parent_directory)
print("Output directory path:", output_directory)
print("New file path inside Output directory:", new_file_path)
