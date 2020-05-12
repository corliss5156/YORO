# Reading-Aid-App-

### Data Instructions 
Sample data for evaluation has already been uploaded under the data folder. To use the data:
1) Git clone this repository in colab by running the following bash command:
  ```
  !git clone https://github.com/Benjamintdk/Reading-Aid-App-.git
  ```
2) Copy the relevant data files to the current working directory:
  ```
  !cp Reading-Aid-App-/data/* .
  ```
3) The files are named accordingly with the following format: file_1 is from wikipedia, file_2 is from a biography, file_3 is from a non-fiction e-book. The files are in JSON(JavaScript Object Notation) format, which is the equivalent of a dictionary in python. To read from JSON files, use the following code:
  ```
  import json 
  
  with open([FILE_NAME.json], encoding='ISO-8859-1') as f:
    data = json.load(f)
  ```
the variable data is then a dictionary, with each key being every paragraph's first sentence and the corresponding value is whatever's left of each paragraph. 
