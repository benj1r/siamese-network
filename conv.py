import torch
import torch.nn as nn

class ConvolutionBlock(nn.Module):
    def __init__(self,in_channels, num_classes, size):
        super(ConvolutionBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=8, kernel_size=(3,3), stride=(1,1), padding=(1,1))
        self.pool = nn.MaxPool2d(kernel_size=(2,2) stride=(2,2))
        self.conv2 = nn.Conv2d(in_channels = 8, out_channels=16, kernel_size(3,3), stride=(1,1), padding=(1,1))
        self.fc1 = nn.Linear(16*(size/4)*(size/4))

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.pool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
        return x


