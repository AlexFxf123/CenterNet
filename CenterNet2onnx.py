import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.onnx
from model import CenterNet
 
num_classes = 80
topk = 100
model = CenterNet(num_classes=num_classes, topk=topk)
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"可训练参数量: {trainable_params}")
model.eval()
onnx_path = "CenterNet.onnx"

# 假设你的输入数据形状，生成对应的随机张量
dummy_input = torch.rand(1, 3, 512, 512)
dummy_target = torch.rand(1, 16384, 85)  # 或者 torch.zeros(target_shape) 等
output = model(dummy_input, dummy_target)
# 将多个输入以元组形式传递给 export 函数
torch.onnx.export(
    model, 
    (dummy_input, dummy_target),        # 关键：以元组形式提供所有参数
    onnx_path,
    input_names=['input', 'target'],  # 为每个输入指定名称，便于识别
    output_names=['output'],
    # 可以继续添加其他参数，如 dynamic_axes
)


