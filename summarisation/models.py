from transformers import BartForConditionalGeneration, BartConfig
import torch import nn
import torch

#Function to load model depending on whether or not it is pretrained
def load_hf_model(config, pretrained=False, path=None, device=device):
    if pretrained:
        if path:
            model = BartForConditionalGeneration.from_pretrained(
                "bart-large-cnn",
                state_dict=torch.load(path, map_location=torch.device('cuda')),
                config=config
            )
        else:
            model = BartForConditionalGeneration.from_pretrained("bart-large-cnn", config=config)
    else:
        model = BartForConditionalGeneration()

    return model.to(device)

#Parametrize BART into its different layer groups
def bart_splitter(model):
    return [
        params(model.bart.model.encoder),
        params(model.bart.model.decoder.embed_tokens),
        params(model.bart.model.decoder.embed_positions),
        params(model.bart.model.decoder.layers),
        params(model.bart.model.decoder.layernorm_embedding)]
        
#Defines pretrained model
class FastaiWrapper(nn.Module):
    def __init__(self):
        self.config = BartConfig(vocab_size=50264, output_past=True)
        self.bart = load_hf_model(config=self.config, pretrained=True)

    def forward(self, x):
        output = self.bart(x)[0]
        return output
