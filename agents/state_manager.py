from typing import Optional

class StateManager:
    def __init__(self):
        self._state = {
            "last_intent": None,
            "last_entities": [],
            "history": [] # Stores {"role": "user/assistant", "content": "message"}
        }

    def update_state(self, intent: str, entities: list, user_query: Optional[str] = None, assistant_response: Optional[str] = None):
        """
        Updates the current state with the latest intent, entities, and conversation turn.
        """
        self._state["last_intent"] = intent
        self._state["last_entities"] = entities
        
        if user_query:
            self._state["history"].append({"role": "user", "content": user_query})
        if assistant_response:
            self._state["history"].append({"role": "assistant", "content": assistant_response})
        
        # Keep history manageable (e.g., last N turns) to avoid excessively long prompts
        # For simplicity, we'll keep all for now, but for real applications, truncate.
        # self._state["history"] = self._state["history"][-5:] # Keep last 5 turns

    def get_current_state(self) -> dict:
        """
        Returns the current state of the conversation.
        """
        return self._state.copy()

    def get_history(self) -> list:
        """
        Returns the conversation history.
        """
        return self._state["history"]