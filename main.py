import os
from dotenv import load_dotenv

from agents.input_parser import InputParser
from agents.state_manager import StateManager
from agents.task_executor import TaskExecutor
from agents.output_formatter import OutputFormatter
from utils.llm_connector import LLMConnector

def agent_pipeline(user_input, state_manager, llm_connector):
    """
    Orchestrates the 4-step AI agent pipeline.
    """
    # Step 1: Input Understanding
    input_parser = InputParser(llm_connector)
    parsed_input = input_parser.parse(user_input, state_manager.get_history()) # Pass history for context
    
    intent = parsed_input.get("intent")
    entities = parsed_input.get("entities", [])

    # Update state with user's input immediately after parsing
    # This ensures the user's current query is part of the history for the *next* turn
    state_manager.update_state(intent=None, entities=[], user_query=user_input) 
    
    current_state = state_manager.get_current_state()

    # Step 3: Plan and Execute Task
    task_executor = TaskExecutor(llm_connector)
    task_result = task_executor.execute_task(intent if intent is not None else "", entities, current_state)

    # Step 4: Generate Output
    output_formatter = OutputFormatter()
    final_output = output_formatter.format_response(task_result)
    
    # Update state with agent's response
    state_manager.update_state(intent=intent, entities=entities, assistant_response=final_output)

    return final_output

if __name__ == "__main__":
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in .env file. Please set it.")

    llm_connector = LLMConnector(api_key=groq_api_key)
    state_manager = StateManager()

    print("Welcome to EssayGenie! Your AI essay brainstorming assistant.")
    print("Type 'exit' or 'quit' to end the session.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("EssayGenie: Goodbye!")
            break
        
        response = agent_pipeline(user_input, state_manager, llm_connector)
        print(f"EssayGenie: {response}")