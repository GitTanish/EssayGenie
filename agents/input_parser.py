import json

class InputParser:
    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    def parse(self, user_input: str, conversation_history: list) -> dict:
        """
        Parses the user query to extract intent and entities.
        Includes conversation history for contextual understanding.
        """
        history_str = "\n".join([f"{item['role']}: {item['content']}" for item in conversation_history])
        
        system_prompt = (
            "You are a highly accurate natural language parser for an AI essay brainstorming assistant. "
            "Your task is to identify the user's intent and any relevant entities from their query. "
            "Consider the past conversation history for context, but focus on the current user input for primary intent. "
            "Respond ONLY with a valid JSON object. " # <--- Keep this
            "The JSON object MUST contain 'intent' and 'entities' keys. " # Added clarity
            "Possible intents include: 'search', 'summarize', 'elaborate', 'general_brainstorm', 'unclear'. "
            "Entities should be a list of relevant keywords or topics."
            "\n\nExample Output JSON: {\"intent\": \"search\", \"entities\": [\"World War II\", \"causes\"]}" # <--- Added "JSON" to example
            "\nExample Output JSON: {\"intent\": \"elaborate\", \"entities\": [\"Keynesian economics\"]}"
            "\nExample Output JSON: {\"intent\": \"general_brainstorm\", \"entities\": [\"history essay\", \"American Revolution\"]}"
        )

        user_message_content = f"Current User Input: \"{user_input}\""
        if history_str:
            user_message_content = f"Conversation History:\n{history_str}\n\n" + user_message_content

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message_content}
        ]

        response_content = ""

        try:
            # Call with json_mode=True to ensure JSON output
            # The prompt itself must also contain "json" for Groq's validation
            response_content = self.llm_connector.get_chat_completion(messages, temperature=0.2, json_mode=True)
            return json.loads(response_content)
        except json.JSONDecodeError as e:
            print(f"CRITICAL ERROR: LLM failed to return valid JSON despite JSON Mode. Error: {e}. Raw response: {response_content}")
            return {"intent": "unclear", "entities": []}
        except Exception as e:
            print(f"Error during input understanding: {e}. Last known LLM response content: {response_content if response_content else 'N/A'}")
            return {"intent": "unclear", "entities": []}