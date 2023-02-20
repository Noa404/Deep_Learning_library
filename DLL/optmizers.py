"""
We use an optmizer to adjust the parameters
of out network based on the gradients computed during back propagation

"""
from nn import NeuralNet

class Optimizer:
    def step(self, net: nn) -> None:
        raise NotImplementedError

class SGD(Optimizer):
    def __init__(self, lr: float = 0.01) -> None:
        self.lr = lr

    def step(self, net: NeuralNet) -> None:
        for param,grad in net.params_and_grads():
            param -= self.lr * grad
