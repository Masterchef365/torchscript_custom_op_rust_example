#!/usr/bin/env python3
import torch
torch.ops.load_library("test_op.so")
print(torch.ops.my_ops.test_op(torch.ones(1, 1), torch.ones(1, 1)))
