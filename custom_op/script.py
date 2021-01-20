#!/usr/bin/env python3
import torch
torch.ops.load_library("build/libtest_op.so")


class MyCell(torch.nn.Module):
    def __init__(self):
        super(MyCell, self).__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x, h):
        new_h = torch.tanh(torch.ops.my_ops.test_op(self.linear(x), h))
        return new_h, new_h


my_cell = MyCell()
x = torch.rand(3, 4)
h = torch.rand(3, 4)
traced_cell = torch.jit.trace(my_cell, (x, h))
print(traced_cell.code)
print(traced_cell(x, h))
traced_cell.save("cell.zip")
print("Saved successfully")
