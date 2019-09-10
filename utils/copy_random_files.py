import os
import random
from shutil import copyfile

folder_input = '/home/marcosmarques/Documents/datasets/dataset_not_divided_documents_classifier/_rg/'
folder_output = '/home/marcosmarques/Documents/datasets/dataset_not_divided_documents_classifier/rg/'
num_files_of_copy = 200

# Obtém o caminho de todos os arquivos em um diretório
images = [os.path.join(folder_input, f) for f in os.listdir(folder_input) if os.path.isfile(os.path.join(folder_input, f))]


image_paths = random.sample(images, k=num_files_of_copy)

for path in image_paths:
    new_path = folder_output + path.split('/')[-1]
    copyfile(path, new_path)
