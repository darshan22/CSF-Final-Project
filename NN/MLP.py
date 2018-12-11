import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.l1 = nn.Linear(1 * 28 * 28, 20)
        self.t1 = nn.Tanh()
        self.l2 = nn.Linear(20, 10)
        self.t2 = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = x.view(-1, 1 * 28 * 28)
        x = self.t1(self.l1(x))
        x = self.t2(self.l2(x))
return x
