import torch
from torch.nn import Sequential as Seq, Linear as Lin, ReLU
from torch_geometric.nn import GINConv


def test_gin_conv():
    in_channels, out_channels = (16, 32)
    edge_index = torch.tensor([[0, 0, 0, 1, 2, 3], [1, 2, 3, 0, 0, 0]])
    num_nodes = edge_index.max().item() + 1
    x = torch.randn((num_nodes, in_channels))

    nn = Seq(Lin(in_channels, 32), ReLU(), Lin(32, out_channels))
    conv = GINConv(nn, train_eps=True)
    assert conv.__repr__() == (
        'GINConv(nn=Sequential(\n'
        '  (0): Linear(in_features=16, out_features=32, bias=True)\n'
        '  (1): ReLU()\n'
        '  (2): Linear(in_features=32, out_features=32, bias=True)\n'
        '))')
    assert conv(x, edge_index).size() == (num_nodes, out_channels)
    conv = GINConv(nn, train_eps=False)
    assert conv(x, edge_index).size() == (num_nodes, out_channels)
