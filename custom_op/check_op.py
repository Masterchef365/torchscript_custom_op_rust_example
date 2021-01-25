#!/usr/bin/env python3
import torch
torch.ops.load_library("test_op.pyd")
print(torch.ops.custom.test_op)