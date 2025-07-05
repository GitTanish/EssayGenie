# EssayGenie 🧠✍️

An AI-powered essay brainstorming assistant built using the 4-step AI agent architecture. EssayGenie helps students generate ideas, understand complex topics, and explore different angles for their academic essays.

## 🎯 Project Overview

**Use Case**: AI Agent to help college students with essay brainstorming and topic exploration

**Target User**: College students working on essays who need help with:
- Finding research angles for topics
- Understanding complex concepts
- Generating creative essay ideas
- Exploring different perspectives on subjects

**Core Value**: Transforms vague academic interests into structured, actionable essay ideas and insights.

## 🏗️ Architecture

EssayGenie follows the 4-step AI agent design pattern:

```
User Input → Input Understanding → State Management → Task Execution → Output Formatting → Response
```

### 1. **Input Understanding** (`input_parser.py`)
- **Purpose**: Parses user queries to extract intent and relevant entities
- **Intents Supported**: `search`, `summarize`, `elaborate`, `general_brainstorm`, `unclear`
- **Technology**: Uses JSON-mode LLM calls for structured output
- **Context Awareness**: Considers conversation history for better understanding

### 2. **State Management** (`state_manager.py`)
- **Purpose**: Maintains conversation context and user interaction history
- **Memory**: Stores last intent, entities, and full conversation history
- **Persistence**: Keeps track of user queries and assistant responses across turns

### 3. **Task Execution** (`task_executor.py`)
- **Purpose**: Routes to appropriate functions based on detected intent
- **Capabilities**:
  - `search`: Provides essay angles and perspectives on topics
  - `summarize`: Gives concise explanations of concepts
  - `elaborate`: Offers detailed analysis and examples
  - `general_brainstorm`: Suggests broad essay ideas and approaches

### 4. **Output Formatting** (`output_formatter.py`)
- **Purpose**: Formats task outputs into user-friendly responses
- **Features**: Consistent formatting with clear structure

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key (for LLM access)
- Required packages: `groq`, `python-dotenv`

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd essaygenie
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the application**
```bash
python main.py
```

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test.py
```

**Test Cases Include:**
- Normal inputs (search, summarize, elaborate)
- Vague inputs ("Give me something academic to think about")
- Edge cases (empty input)
- Ambiguous requests
- Compound queries

## 💡 Example Interactions

### Search Intent
```
You: Search for causes of World War II
EssayGenie: Here's what I found:

Looking at the causes of World War II, here are several potential essay angles:

1. **Economic Factors**: How the Great Depression and economic instability contributed to political extremism
2. **Treaty of Versailles**: Analyzing whether the harsh terms created conditions for future conflict
3. **Rise of Totalitarianism**: Examining how fascist and communist ideologies gained power
4. **Failure of Appeasement**: Evaluating the diplomatic strategies that failed to prevent war
5. **Colonial and Imperial Tensions**: How competition for resources and territory escalated conflicts
```

### Elaborate Intent
```
You: Elaborate on the Industrial Revolution
EssayGenie: Here's what I found:

The Industrial Revolution represents a fundamental transformation in human production and social organization. Here are key aspects for deeper analysis:

1. **Technological Innovation**: Steam power, mechanization, and factory systems revolutionized production methods, shifting from manual labor to machine-based manufacturing.

2. **Social Transformation**: Created new class structures with industrial capitalists and urban workers, fundamentally changing family structures and community relationships.

3. **Economic Impact**: Introduced concepts of wage labor, mass production, and capital accumulation that form the basis of modern economic systems.

For your essay, consider examining how these changes affected different social groups, regional variations in industrialization, or long-term environmental consequences.
```

## 📁 Project Structure

```
essaygenie/
├── agents/
│   ├── __init__.py
│   ├── input_parser.py      # Intent and entity extraction
│   ├── state_manager.py     # Conversation state management
│   ├── task_executor.py     # Task routing and execution
│   └── output_formatter.py  # Response formatting
├── utils/
│   ├── __init__.py
│   └── llm_connector.py     # Groq LLM integration
├── main.py                  # Main application entry point
├── test.py                  # Test suite
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (create this)
```

## 🔧 Technical Implementation

### LLM Integration
- **Provider**: Groq (fast inference)
- **Model**: llama3-70b-8192
- **JSON Mode**: Ensures structured responses for parsing
- **Temperature Control**: Varies by task (0.2 for parsing, 0.8 for creative brainstorming)

### Error Handling
- JSON parsing fallbacks
- LLM connection error recovery
- Graceful degradation for unclear intents

### State Management
- Conversation history tracking
- Intent and entity persistence
- Context-aware parsing

## 🎨 Design Decisions

### Why This Architecture?
1. **Modularity**: Each component has a single responsibility
2. **Extensibility**: Easy to add new intents and capabilities
3. **Testability**: Each layer can be tested independently
4. **Maintainability**: Clear separation of concerns

### Intent Classification
- **search**: When users want to explore topics or find angles
- **summarize**: When users need concise explanations
- **elaborate**: When users want detailed analysis
- **general_brainstorm**: When users have broad, unfocused needs

## 🚧 Known Limitations

1. **Memory Management**: Conversation history grows indefinitely
2. **Context Window**: No truncation strategy for long conversations
3. **Multi-turn Planning**: Limited ability to handle complex, multi-step requests
4. **Personalization**: No user-specific preferences or learning

## 🔮 Future Enhancements

- **Web Search Integration**: Real-time research capabilities
- **Citation Management**: Automatic source tracking and formatting
- **Essay Structure Planning**: Outline generation and organization
- **Collaborative Features**: Peer review and feedback integration
- **Export Capabilities**: Save conversations and ideas to various formats

## 🏆 Assignment Alignment

This project demonstrates:
- ✅ **4-Step Architecture**: Complete implementation of all layers
- ✅ **Problem-Solving**: Addresses real student needs
- ✅ **LLM Integration**: Effective use of AI capabilities
- ✅ **Iterative Development**: Multiple test cases and refinements
- ✅ **Documentation**: Clear code structure and comments

## 📖 Learning Outcomes

Through building EssayGenie, key insights include:
- **Prompt Engineering**: Crafting effective system prompts for different tasks
- **State Management**: Balancing context retention with performance
- **Intent Classification**: Designing clear, actionable intent categories
- **Error Handling**: Building resilient AI applications
- **User Experience**: Creating natural, helpful AI interactions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Update documentation
5. Submit a pull request

## 📄 License

MIT License

Copyright (c) 2025 EssayGenie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**Built with curiosity, iteration, and a commitment to helping students succeed in their academic journey.** 🎓
