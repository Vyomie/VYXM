from vyxm.protocol.registry import Registry
from vyxm.protocol.RegistryVisualizer import RegistryVisualizer

registry = Registry()
visualizer = RegistryVisualizer(registry)
visualizer.Visualize()