# How to organise code 

There should be 3 .py scripts at most: utils.py, models.py and loss.py 
utils.py contains the additional utilities and preprocessing functions or classes needed 
models.py contains the functions or classes to load pretrained models, add custom nn modules or any wrappers for defining the architecture 
loss.py contains the custom loss function(if any) if necessary 

### The main script is located here in this [colab notebook] (https://colab.research.google.com/drive/1x5zWe8yoyvuYcAAiss2zpLEqG7wp-5ez?usp=sharing). 
### All the above mentioned packages have to be imported beforehand for the notebook to run successfully. 
