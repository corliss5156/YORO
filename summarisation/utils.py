from transformers import PreTrainedTokenizer, BartTokenizer
import pandas as pd
import json

#converts json files to dataframes
def json_to_df(file_name):
  with open(file_name, encoding='ISO-8859-1') as file:
    data = json.load(file)
  summaries = list(data.keys())
  text = list(data.values())
  df = {'summary':summaries, 'text':text}
  return pd.DataFrame(df)
