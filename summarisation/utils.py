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

#Transforms the data
#Inherits from the Transform
class DataTransform(Transform):
    def __init__(self, tokenizer:PreTrainedTokenizer, column:str, max_length):
        self.tokenizer = tokenizer
        self.column = column
        self.max_length = max_length
    #batch_encode_plus encodes the input text into
    def encodes(self, inp):
        tokenized = self.tokenizer.batch_encode_plus(
            [list(inp[self.column])],
            max_length=self.max_length,
            pad_to_max_length=True,
            return_tensors='pt'
        )
        return TensorText(tokenized['input_ids']).squeeze()

    def decodes(self, encoded):
        decoded = [
            self.tokenizer.decode(o, skip_special_tokens=True,
                                  clean_up_tokenization_spaces=False) for o in encoded]
        return decoded
