import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.onnx
import model as mdl
 
input = torch.rand(3, 224, 224)
target = torch.rand(100, 6)
num_classes = 80
topk = 100
model = mdl.CenterNet(num_classes=num_classes, topk=topk)
output = model(input, target)
onnx_path = "CenterNet.onnx"
torch.onnx.export(model, input, onnx_path)

