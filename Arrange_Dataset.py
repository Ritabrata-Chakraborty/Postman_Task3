import os
import shutil
import random
import csv

# Create new folders for Rock, Paper, and Scissor
rock_folder = 'Rock'
paper_folder = 'Paper'
scissor_folder = 'Scissor'

# List of CSV file names
foldernames = ['train', 'test', 'valid']  

for foldername in foldernames:
    
    if not os.path.exists('Dataset/' + foldername + '/' + rock_folder):
        os.makedirs('Dataset/' + foldername + '/' + rock_folder)
        
    if not os.path.exists('Dataset/' + foldername + '/' + paper_folder):
        os.makedirs('Dataset/' + foldername + '/' + paper_folder)
        
    if not os.path.exists('Dataset/' + foldername + '/' + scissor_folder):
        os.makedirs('Dataset/' + foldername + '/' + scissor_folder)
    
    if not os.path.exists('Dataset/' + foldername + '/None'):
        os.makedirs('Dataset/' + foldername + '/None')

    with open('Dataset/' + foldername + '/_classes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            filename = row['filename']
            rock_value = int(row[' Rock'])
            paper_value = int(row[' Paper'])
            scissor_value = int(row[' Scissors'])

            if rock_value == 1:
                shutil.copy(('Dataset/' + foldername + '/' + filename), os.path.join('Dataset/' + foldername + '/' + rock_folder, os.path.basename(filename)))

            if paper_value == 1:
                shutil.copy(('Dataset/' + foldername + '/' + filename), os.path.join('Dataset/' + foldername + '/' + paper_folder, os.path.basename(filename)))

            if scissor_value == 1:
                shutil.copy(('Dataset/' + foldername + '/' + filename), os.path.join('Dataset/' + foldername + '/' + scissor_folder, os.path.basename(filename)))

            if scissor_value == 0 and paper_value == 0 and rock_value == 0:
                shutil.copy(('Dataset/' + foldername + '/' + filename), os.path.join('Dataset/' + foldername + '/None', os.path.basename(filename)))
            
            os.remove('Dataset/' + foldername + '/' + filename)
        
    none_files = [f for f in os.listdir('Dataset/' + foldername + '/None') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    files_to_delete = int(len(none_files) * 0.8)
    
    # Randomly select files to delete
    files_to_delete_indices = random.sample(range(len(none_files)), files_to_delete)
    
    # Delete the selected files
    for index in sorted(files_to_delete_indices, reverse=True):
        file_to_delete = os.path.join('Dataset/' + foldername + '/None', none_files[index])
        os.remove(file_to_delete)
        print(f"Deleted: {file_to_delete}")
        
    os.remove('Dataset/' + foldername + '/_classes.csv')

    print(f"Images from {foldername} have been copied and moved to the respective folders.")

print("All CSV files have been processed.")