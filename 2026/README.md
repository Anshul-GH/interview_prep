Day 1 (02/16/26, Mon, 4h) – PyTorch/ML basics
Focus: tensors, autograd, DataLoaders, fast.ai lesson 1–2, simple vision model

Overall structure for the 4 hours
[DONE] - Hour 1: PyTorch tensors basics
[DONE] - Hour 2: Autograd (automatic differentiation)
- Hour 3: DataLoaders and datasets
- Hour 4: Simple vision model + fast.ai Lesson 1–2 connections

Hour 1 – Tensors
Goals:
- Understand what a tensor is and how it differs from NumPy arrays.
- Practice basic tensor operations.

Tasks:
- Read the “Tensors” section in the official PyTorch documentation.
- In a Python script or notebook:
  - Create tensors with torch.tensor, torch.zeros, torch.ones, torch.randn.
  - Convert between NumPy arrays and tensors.
  - Practice reshaping and indexing (view, reshape, permute, slicing).
  - Move tensors to GPU if available using tensor.to(device).

Hour 2 – Autograd
Goals:
- Understand how PyTorch builds a computation graph and computes gradients.
- Be able to get gradients for simple functions.

Tasks:
- Read the “Autograd: Automatic Differentiation” tutorial in the PyTorch docs.
- In code:
  - Create a tensor x with requires_grad=True.
  - Define a simple function, e.g. y = (3 * x**2 + 2 * x).sum().
  - Call y.backward() and inspect x.grad.
  - Reset gradients and try a different function; confirm the derivative matches your hand calculation.

Hour 3 – DataLoaders and datasets
Goals:
- Learn how PyTorch handles data batching and shuffling.
- Be able to build a DataLoader for a simple dataset.

Tasks:
- Read the “Data loading and processing” tutorial in the PyTorch docs.
- In code:
  - Use a built-in dataset (e.g. MNIST or CIFAR10 via torchvision.datasets).
  - Wrap it in a DataLoader with batch_size=64 and shuffle=True.
  - Iterate over the DataLoader in a loop and print batch shapes.
  - Optionally define a small custom Dataset class that reads from an image folder structure.

Hour 4 – Simple vision model + fast.ai Lesson 1–2
Goals:
- Tie tensors, autograd, and DataLoaders into a full training loop.
- See how fast.ai’s high-level API relates to raw PyTorch.

Tasks:
- From fast.ai’s “Practical Deep Learning for Coders” course, watch or skim Lesson 1 and Lesson 2.
- In raw PyTorch (not fast.ai), implement:
  - A simple CNN (or a small torchvision model).
  - A loss function (e.g. cross-entropy) and optimizer (e.g. Adam).
  - A minimal training loop:
    - For each batch: forward pass, compute loss, loss.backward(), optimizer.step().
    - Train for 1–2 epochs on a small subset of data.
- Compare with fast.ai:
  - Note how fast.ai’s Learner and fit functions encapsulate your manual training steps.
  - Write 3–5 bullet points mapping each manual step to the equivalent fast.ai abstraction.

Quick cheat sheet (keep open while working)
- Tensors:
  - torch.tensor, torch.randn, .view, .reshape, .permute
- Autograd:
  - x.requires_grad_(True), y = f(x), y.backward(), x.grad
- Data:
  - class MyDataset(Dataset): ...
  - DataLoader(dataset, batch_size=64, shuffle=True)
- Training loop:
  - for xb, yb in loader:
  - optimizer.zero_grad(), loss.backward(), optimizer.step()
