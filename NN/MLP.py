#Reference: https://github.com/amir-jafari/Deep-Learning
import torch
import torch.nn as nn

#define class for MLP
class Net(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes, activation):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.relu1 = activation
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.relu2 = activation
        self.fc3 = nn.Linear(hidden_size2, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        if self.activation == "sigmoid":
           sigmoid = nn.Sigmoid()
           out = sigmoid(out)
        elif self.activation == "relu":
           relu = nn.ReLU()
           out = relu(out)
        elif self.activation == "tanh":
           tanh = nn.Tanh()
           out = tanh(out)
        elif self.activation == "softmax":
           soft_max = nn.Softmax()
           out = soft_max(out)
        else:
           pass
        out = self.fc2(out)
        if self.activation == "sigmoid":
           sigmoid = nn.Sigmoid()
           out = sigmoid(out)
        elif self.activation == "relu":
           relu = nn.ReLU()
           out = relu(out)
        elif self.activation == "tanh":
           tanh = nn.Tanh()
           out = tanh(out)
        elif self.activation == "softmax":
           soft_max = nn.Softmax()
           out = soft_max(out)
        else:
           pass
        out = self.fc3(out)
        return out
