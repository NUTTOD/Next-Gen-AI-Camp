import torch
import torch.nn as nn
import torch.nn.functional as Function

class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, kernel_size=5)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
        self.conv3 = nn.Conv2d(16, 32, kernel_size=5)
        self.fc1 = nn.Linear(32*56*56, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 4)

    def forward(self, x):
        x = Function.relu(self.conv1(x))
        x = Function.relu(self.conv2(x))
        x = Function.relu(self.conv3(x))
        x = x.view(-1, 32*56*56)
        x = Function.relu(self.fc1(x))
        x = Function.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
model = CNNModel()
print(model)