from groq import Groq

class LLMConnector:
    def __init__(self, api_key: str, model: str = "llama3-70b-8192"):
        self.client = Groq(api_key=api_key)
        self.model = model

    def get_chat_completion(self, messages: list, temperature: float = 0.7, json_mode: bool = False) -> str: # Added json_mode parameter
        """
        Sends messages to the LLM and returns the completion.
        If json_mode is True, it instructs the LLM to return valid JSON.
        """
        try:
            if json_mode:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    response_format={"type": "json_object"} # <--- JSON Mode Activation
                )
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature
                )
            return response.choices[0].message.content or ""
        except Exception as e:
            print(f"Error communicating with LLM: {e}")
            return "I'm sorry, I'm having trouble connecting to my knowledge base right now. Please try again later."