from __future__ import print_function, division
import torch.nn.functional as F


import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

def dice_loss(prediction, target):
    """Calculating the dice loss
    Args:
        prediction = predicted image
        target = Targeted image
    Output:
        dice_loss"""

    smooth = 1.0

    i_flat = prediction.view(-1)
    t_flat = target.view(-1)

    intersection = (i_flat * t_flat).sum()

    return 1 - ((2. * intersection + smooth) / (i_flat.sum() + t_flat.sum() + smooth))


def calc_loss(prediction, target, bce_weight=0.5, margin=2):
    """Calculating the loss and metrics
    Args:
        prediction = predicted image
        target = Targeted image
        metrics = Metrics printed
        bce_weight = 0.5 (default)
    Output:
        # loss : dice loss of the epoch """
    bce = F.binary_cross_entropy_with_logits(prediction, target)

    # criterion = nn.BCELoss()
    # bce = criterion(prediction, target)
    # bce = F.binary_cross_entropy(prediction, target)
    # bce = torch.sum((1-target)*torch.pow(prediction,2 ) + \
    #                                    target * torch.pow(torch.clamp(margin - prediction, min=0.0),2))
    prediction = F.sigmoid(prediction)
    dice = dice_loss(prediction, target)

    loss = bce * bce_weight + dice * (1 - bce_weight)

    return bce

class FocalLoss2d(torch.nn.Module):
    def __init__(self, weight=None, size_average=True, ignore_index=255):
        super(FocalLoss2d, self).__init__()
        self.gamma = 2
        self.nll_loss = torch.nn.NLLLoss2d(weight, size_average)

    def forward(self, inputs, targets):
        return self.nll_loss((1 - F.sigmoid(inputs, 1)) ** self.gamma * F.logsigmoid(inputs, 1), targets)
def sigmoid_focalloss(input, target, gamma):
    return F.nll_loss((1 - F.sigmoid(input)) ** gamma * F.logsigmoid(input), target)



