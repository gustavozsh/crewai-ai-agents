# Getting Started with CrewAI

## What is CrewAI?

CrewAI is a framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Step 1: Set up your environment

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install CrewAI

```bash
pip install crewai crewai-tools
```

## API Keys

CrewAI typically uses LLM providers like OpenAI. You'll need to set up API keys:

1. Get an API key from [OpenAI](https://platform.openai.com/api-keys)
2. Create a `.env` file in your project:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Your First Crew

A crew consists of:
- **Agents**: AI entities with specific roles and goals
- **Tasks**: Assignments that agents need to complete
- **Process**: How tasks are executed (sequential or hierarchical)

### Basic Example

```python
from crewai import Agent, Task, Crew, Process

# Define an agent
researcher = Agent(
    role='Researcher',
    goal='Find information on a given topic',
    backstory='You are a skilled researcher',
    verbose=True
)

# Define a task
research_task = Task(
    description='Research the topic of AI agents',
    agent=researcher,
    expected_output='A comprehensive research report'
)

# Create a crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential
)

# Run the crew
result = crew.kickoff()
print(result)
```

## Next Steps

1. Explore the example project in `projects/example-project/`
2. Read about [Project Structure](PROJECT_STRUCTURE.md)
3. Learn [Best Practices](BEST_PRACTICES.md)
4. Create your own project!
