class TaskExecutor:
    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    def _perform_search(self, entities: list) -> str:
        """Simulates a search operation for essay topics."""
        query = ", ".join(entities)
        prompt = (
            f"You are an AI assistant helping students brainstorm. "
            f"Provide a brief overview and 3-5 potential essay angles/questions related to '{query}'. "
            f"Focus on historical, social, or thematic perspectives if applicable."
        )
        messages = [{"role": "user", "content": prompt}]
        return self.llm_connector.get_chat_completion(messages, temperature=0.7)

    def _summarize_topic(self, entities: list) -> str:
        """Summarizes a given topic."""
        topic = ", ".join(entities)
        prompt = (
            f"You are an academic summarizer for college students. "
            f"Briefly explain '{topic}' in 2-3 sentences, highlighting its core concept."
        )
        messages = [{"role": "user", "content": prompt}]
        return self.llm_connector.get_chat_completion(messages, temperature=0.4)

    def _elaborate_topic(self, entities: list) -> str:
        """
        Elaborates on a given concept, providing more detail, examples,
        or potential sub-arguments for an essay.
        """
        concept = ", ".join(entities)
        prompt = (
            f"You are an expert academic tutor. Elaborate on the concept of '{concept}'. "
            f"Provide 2-3 key aspects, relevant examples, or potential areas for deeper analysis in an essay. "
            f"Assume the student needs detailed insights for their paper."
        )
        messages = [{"role": "user", "content": prompt}]
        return self.llm_connector.get_chat_completion(messages, temperature=0.6)

    def _general_brainstorm(self, entities: list) -> str:
        """Provides general brainstorming ideas based on broad input."""
        topic = ", ".join(entities) if entities else "a general essay topic"
        prompt = (
            f"You are a creative essay brainstorming assistant. "
            f"Suggest 3-5 broad essay ideas or approaches for a student working on '{topic}'. "
            f"Think about different disciplines or angles."
        )
        messages = [{"role": "user", "content": prompt}]
        return self.llm_connector.get_chat_completion(messages, temperature=0.8)

    def execute_task(self, intent: str, entities: list, current_state: dict) -> str:
        """
        Dispatches to the appropriate task function based on the detected intent.
        """
        if intent == "search":
            return self._perform_search(entities)
        elif intent == "summarize":
            return self._summarize_topic(entities)
        elif intent == "elaborate":
            return self._elaborate_topic(entities)
        elif intent == "general_brainstorm": # <--- ADD THIS ELIF BLOCK
            return self._general_brainstorm(entities)
        else:
            return "I'm not sure how to help with that specific request. Can you rephrase or ask for something like 'search', 'summarize', or 'elaborate', or 'general brainstorm'?"