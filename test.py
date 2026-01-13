# 测试是否找到gpu
import torch  as t 
print('test',t.cuda.is_available())
print(t.version.cuda)

# 查看模型参数和结构
# import torch
# model_params = torch.load('./checkpoints/centernet_10.pth')  # 加载模型参数
# print(model_params)         # 查看模型参数，可以看到参数，但看不到网络结构

# import matplotlib.pyplot as plt
# plt.figure(figsize=(12, 6))
# # plt.plot(range(1, opt.max_epoch + 1), loss_values, label='Training Loss',color='blue', marker='o')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.title('Training Loss')
# plt.legend()
# plt.show()