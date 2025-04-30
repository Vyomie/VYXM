# RegistryVisualizer.py
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class RegistryVisualizer:
    def __init__(self, registry):
        self.Registry = registry
        self.Graph = nx.DiGraph()
        self.NodeTypes = {
            'Specialist': {'Color': '#FFD700', 'Shape': 's'},
            'Tool': {'Color': '#ADD8E6', 'Shape': 'd'},
            'Planner': {'Color': '#90EE90', 'Shape': 'h'},
            'Distributor': {'Color': '#FFA07A', 'Shape': 'v'}
        }

    def BuildGraph(self):
        # Add Planner Node
        if self.Registry.PlannerModel:
            self.Graph.add_node(
                "Planner",
                Type='Planner',
                Label=f"Planner\n{self.Registry.PlannerModel['Name']}"
            )

        # Add Distributor Node
        self.Graph.add_node(
            "Distributor",
            Type='Distributor',
            Label="Distributor\n(Zero-shot Router)"
        )

        # Add Specialists
        for specialist in self.Registry.Specialists:
            self.Graph.add_node(
                specialist['Name'],
                Type='Specialist',
                Label=f"{specialist['Name']}\n[{specialist['Tag']}]"
            )
            self.Graph.add_edge(
                "Distributor",
                specialist['Name'],
                Label=f"Routes\n{specialist['Tag']}"
            )

        # Add Tools
        for toolName, toolData in self.Registry.Tools.GetAllTools().items():
            self.Graph.add_node(
                toolName,
                Type='Tool',
                Label=f"{toolName}\n({toolData['Category']})"
            )

        # Connect Specialists to Tools
        for specialist in self.Registry.Specialists:
            for toolName in self.Registry.Tools.GetAllTools():
                if (specialist['Tag'].lower() in toolName.lower() or 
                    specialist['Name'].lower() in toolName.lower()):
                    self.Graph.add_edge(
                        specialist['Name'],
                        toolName,
                        Style='dashed',
                        Label="Uses"
                    )

    def DrawNodes(self, positions, axis):
        for node in self.Graph.nodes():
            nodeType = self.Graph.nodes[node]['Type']
            config = self.NodeTypes[nodeType]
            
            nx.draw_networkx_nodes(
                self.Graph,
                positions,
                nodelist=[node],
                node_shape=config['Shape'],
                node_size=3000,
                node_color=config['Color'],
                alpha=0.9,
                ax=axis
            )
            
            plt.text(
                positions[node][0],
                positions[node][1],
                self.Graph.nodes[node]['Label'],
                ha='center',
                va='center',
                fontsize=8,
                bbox=dict(facecolor='white', alpha=0.7)
            )

    def DrawEdges(self, positions, axis):
        for source, target, data in self.Graph.edges(data=True):
            nx.draw_networkx_edges(
                self.Graph,
                positions,
                edgelist=[(source, target)],
                width=2,
                alpha=0.6,
                edge_color='gray',
                style=data.get('Style', 'solid'),
                ax=axis
            )
            
            if 'Label' in data:
                plt.text(
                    positions[source][0]*0.6 + positions[target][0]*0.4,
                    positions[source][1]*0.6 + positions[target][1]*0.4,
                    data['Label'],
                    fontsize=7,
                    bbox=dict(facecolor='white', alpha=0.7)
                )

    def Visualize(self):
        plt.figure(figsize=(14, 10))
        axis = plt.gca()
        
        self.BuildGraph()
        positions = nx.spring_layout(self.Graph, k=1.5, seed=42)
        
        self.DrawNodes(positions, axis)
        self.DrawEdges(positions, axis)
        
        # Create Legend
        legendElements = [
            plt.Line2D([0], [0], marker='s', color='w', label='Specialist',
                      markerfacecolor='#FFD700', markersize=15),
            plt.Line2D([0], [0], marker='d', color='w', label='Tool',
                      markerfacecolor='#ADD8E6', markersize=15),
            plt.Line2D([0], [0], marker='h', color='w', label='Planner',
                      markerfacecolor='#90EE90', markersize=15),
            plt.Line2D([0], [0], marker='v', color='w', label='Distributor',
                      markerfacecolor='#FFA07A', markersize=15)
        ]
        
        axis.legend(handles=legendElements, loc='upper right')
        plt.title("VyxM Protocol Registry Visualization", fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

# Example Usage
if __name__ == "__main__":
    from vyxm.protocol import Registry
    registry = Registry()
    visualizer = RegistryVisualizer(registry)
    visualizer.Visualize()