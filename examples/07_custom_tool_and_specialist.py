from vyxm.protocol.registry import Registry
from vyxm.protocol.tools import Tool

@Tool(Name="SayHello", Description="Says hello", Inputs={"Name": "str"}, Category="Test")
def SayHello(Name):
    return f"Hello, {Name}!"

registry = Registry()
print(registry.Tools.GetTool("SayHello")["Func"]("Alice"))