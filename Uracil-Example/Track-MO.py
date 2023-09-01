import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
import sys

########################
# This part of the script is input
# for your specific system

active_space_start = 24
active_space_end = 32
cosine_similarity_threshold = 0.5

# End of input part
########################

# Defines number of MOs in active space
# based on start and end MO

cas_size = active_space_end - active_space_start + 1

# Read in two input file names and store them in tuple

filename1 = sys.argv[1]
filename2 = sys.argv[2]

filenames = (filename1, filename2)

def extract_data(filename, mo_number):
    with open(filename, 'r') as file:
        lines = file.readlines()

    start_pattern = re.compile(fr"\* ORBITAL\s+1\s+{mo_number}\b")
    end_pattern = re.compile(r"\* ORBITAL\b")
    
    start_index = -1
    end_index = -1
    data_lines = []

    for i, line in enumerate(lines):
        if start_pattern.match(line) and start_index == -1:
            start_index = i + 1
        elif end_pattern.match(line) and start_index != -1 and end_index == -1:
            end_index = i
            break
        elif start_index != -1 and end_index == -1:
            data_lines.append(line.strip())

    data_values = []
    for line in data_lines:
        values = [float(val) for val in line.split()]
        data_values.extend(values)

    data_array = np.array(data_values)
    return data_array

data_arrays = {}  # Dictionary to store data arrays

for filename in filenames:
    data_arrays_for_file = {}
    
    for mo_number in range(active_space_start, active_space_end + 1):
        data_array_name = f"data_array_{mo_number}"
        data_array = extract_data(filename, mo_number)
        if data_array is not None:
            data_arrays_for_file[data_array_name] = data_array
    
    data_arrays[filename] = data_arrays_for_file

# Calculate cosine similarity for each pair of vectors

cosine_similarity_count = 0  # Counter for cosine similarities equal to 1

for mo_number_1st in range(active_space_start, active_space_end + 1):
    for mo_number_2nd in range(active_space_start, active_space_end + 1):
        data_array_1 = data_arrays[filenames[0]][f"data_array_{mo_number_1st}"]
        data_array_2 = data_arrays[filenames[1]][f"data_array_{mo_number_2nd}"]
        
        data_array_1 = data_array_1.reshape(1, -1)
        data_array_2 = data_array_2.reshape(1, -1)
        
        similarity_matrix = cosine_similarity(data_array_1, data_array_2)
        cosine_similarity_value = similarity_matrix[0, 0]
        
# Uncomment for debug
#        print(f"Cosine Similarity for MO {mo_number_1st} {mo_number_2nd}: {cosine_similarity_value}")

# Count how many MOs are identical

        if cosine_similarity_value > cosine_similarity_threshold:
            cosine_similarity_count += 1

# Uncomment for debug
#print(f"Number of cosine similarity values equal to 1: {cosine_similarity_count}")

# Check if active space is stable

if cosine_similarity_count < cas_size:
    print('Warning: potential change in active space!')
else:
    print('Consistent with previous step')
