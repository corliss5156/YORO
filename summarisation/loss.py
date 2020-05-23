from torch import nn
from torch.nn import F

#Defines summarisation loss function
class SummarisationLoss(nn.Module):
    def __init__(self):
        #defines loss function to be used, which is cross entropy
        self.criterion = torch.nn.CrossEntropyLoss()

    def forward(self, output, target):
        #output is a 3D tensor of dimension batch_size x sequence length x 1024(fixed vector output size)
        #target is also of the same shape: batch_size x sequence length x 1024(fixed vector output size)
        #x is of the same dimension as the output as softmax is applied to the second dimension(along sequence length)
        x = F.log_softmax(output, dim=-1)
        #norm calculates the sum of values in the target not equal to 1, i.e. not empty since 1 is used for padding
        norm = (target != 1).data.sum()
        #first reshape x into a 2D tensor of size (batch_size*sequence length) x 1024(last dimension)
        #contiguous ensures that the ordering of the values in x remains intact
        #then reshape the target likewise
        return self.criterion(x.contiguous().view(-1, x.size(-1)), target.contiguous().view(-1)) / norm
