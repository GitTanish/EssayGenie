class OutputFormatter:
    def format_response(self, task_output: str) -> str:
        """
        Formats the output from the task executor into a user-friendly response.
        """
        # For a simple agent, this might just return the task_output directly.
        # In a more complex agent, you might add intros, outros, or
        # rephrase based on the perceived sentiment or conversation flow.
        return f"Here's what I found:\n\n{task_output}"