import torch

a = torch.randn(100, 200)
b = torch.randn(200, 300)
c = torch.mm(a, b)
