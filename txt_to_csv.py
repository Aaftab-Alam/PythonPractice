import pandas as pd

read_file = pd.read_csv (r'Path where the Text file is stored\File name.txt')
read_file.to_csv (r'Path where the CSV will be saved\File name.csv', index=None)