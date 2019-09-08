import split_folders

input_folder = 'dataset_not_divided'
output = 'dataset'

split_folders.ratio(input_folder, output=output, seed=1337, ratio=(.8, .1, .1))