#!/usr/bin/env python3
import torch
import platform
import sys
if sys.platform == "linux":
    torch.ops.load_library("_pvcnn_backend.so")
elif sys.platform == "win32":
    torch.ops.load_library("_pvcnn_backend.pyd")

class MyCell(torch.nn.Module):
    def __init__(self):
        super(MyCell, self).__init__()

    def forward(self, x, h):
        return torch.ops._pvcnn_backend.ball_query(x, h, 0.1, 2)


my_cell = MyCell()
centers_coords = torch.rand(3, 2, 2).cuda()
points_coords = torch.rand(3, 2, 2).cuda()
traced_cell = torch.jit.trace(my_cell, (centers_coords, points_coords))
print(traced_cell.code)
print(traced_cell(centers_coords, points_coords))
traced_cell.save("cell.zip")
print("Saved successfully")
