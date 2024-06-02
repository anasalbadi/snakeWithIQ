# Let us jump to building the feed-forward neural network
#####################################################
# import the packages we need for this project
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

#####################################################
# Building the Neural Network 
class Linear_QNet(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)