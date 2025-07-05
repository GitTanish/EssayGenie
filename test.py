from agents.input_parser import InputParser
from agents.state_manager import StateManager
from agents.task_executor import TaskExecutor
from agents.output_formatter import OutputFormatter
from utils.llm_connector import LLMConnector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Sanity check
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Initialize modules
llm = LLMConnector(api_key=api_key)
state = StateManager()
parser = InputParser(llm)
executor = TaskExecutor(llm)
formatter = OutputFormatter()

def run_test(user_input):
    print(f"\n🧪 Input: {user_input}")
    
    # Parse
    parsed = parser.parse(user_input, state.get_history())
    print(f"🔍 Parsed: {parsed}")
    
    intent = parsed.get("intent", "")
    entities = parsed.get("entities", [])
    
    # Update state with user input
    state.update_state(intent="", entities=[], user_query=user_input)
    
    # Execute task
    current_state = state.get_current_state()
    task_output = executor.execute_task(intent, entities, current_state)
    
    # Format output
    final_output = formatter.format_response(task_output)
    print(f"🧠 EssayGenie: {final_output}")
    
    # Update state with assistant response
    state.update_state(intent=intent, entities=entities, assistant_response=final_output)

if __name__ == "__main__":
    print("✅ Running AI Agent Test Suite")

    test_cases = [
        # Normal Inputs
        "Search for causes of World War II",
        "Summarize the idea of existentialism",
        "Elaborate on the Industrial Revolution",
        "I need help brainstorming a history essay",
        
        # Vague Input
        "Give me something academic to think about",
        
        # Edge Case: Empty
        "",

        # Ambiguous or unclear intent
        "Tell me more about stuff in the past",

        # Compound Input
        "Can you summarize Keynesian economics and then give me essay angles?",
    ]

    for case in test_cases:
        run_test(case)
