# Let us jump to building the feed-forward neural network
#####################################################
# import the packages we need for this project
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

#####################################################
# Building the Neural Network - Look at readme for more info
class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        # First linear layer with input size and hidden size outputs
        self.linear1 = nn.Linear(input_size, hidden_size)
        # Second linear layer with hidden size and output size outputs
        self.linear2 = nn.Linear(hidden_size, output_size)

    # applies first linear layer to the input 'x' and then applies ReLU
    def forward(self, x): # This is a feed-forward neural net
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    
    def save(self, file_name='model.pth') : # Saving the model
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)

# Training & Optimizing the network: 
# Using the simplified deep Q-learning equations
class QTrainer:
    def __init__(self, model, lr, gamma): # initializing
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr) # optimizer
        self.criterion = nn.MSELoss() # loss function

    def train_step(self, state, action, reward, next_state, done): # trainer
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)

        if len(state.shape) == 1: # if there 1 dimension
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done,)
        pred = self.model(state) # using the q-model predict equation above

        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))
            target[idx][torch.argmax(action[idx]).item()] = Q_new
        
        self.optimizer.zero_grad() # calculating loss function
        loss = self.criterion(target, pred)
        loss.backward()
        self.optimizer.step()


