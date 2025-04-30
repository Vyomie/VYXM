# agent_specialists.py

class RestaurantFinder:
    def Run(self, InputData):
        Task = InputData["Task"]
        ToolRegistry = InputData["ToolRegistry"]
        MapsUrl = ToolRegistry.GetTool("GoogleMaps")["Func"]("sushi in NYC")

        return (
            f"Found sushi place: {MapsUrl}",
            "Text",
            {
                "ToolCalls": [],
                "NextSpecialist": "EmailSender",
                "NextTask": f"Email this restaurant link: {MapsUrl}",
            },
        )

class EmailSender:
    def Run(self, InputData):
        Task = InputData["Task"]
        return (
            f"Sent email: {Task}",
            "Text",
            {
                "ToolCalls": [
                    {
                        "Tool": "SendEmail",
                        "Args": {
                            "To": "you@example.com",
                            "Subject": "Restaurant",
                            "Body": Task
                        }
                    }
                ],
                "NextSpecialist": None,
            },
        )
