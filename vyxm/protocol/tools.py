# tools.py

class ToolRegistry:
    def __init__(self):
        self.Tools = {}

    def RegisterTool(self, Name, Func, Description="", Inputs=None, Category=None):
        self.Tools[Name] = {
            "Func": Func,
            "Description": Description,
            "Inputs": Inputs or {},
            "Category": Category or "General"
        }

    def GetTool(self, Name):
        return self.Tools.get(Name)

    def GetAllTools(self):
        return self.Tools

    def ListTools(self, Category=None):
        if Category:
            return {K: V for K, V in self.Tools.items() if V["Category"] == Category}
        return self.Tools


def CallTool(Name, Args, Registry):
    Tool = Registry.GetTool(Name)
    if not Tool:
        return f"Tool '{Name}' not found."
    return Tool["Func"](**Args)


ToolRegistryInstance = ToolRegistry()

def Tool(Name, Description="", Inputs=None, Category=None):
    def Wrapper(Func):
        ToolRegistryInstance.RegisterTool(Name, Func, Description, Inputs, Category)
        return Func
    return Wrapper
