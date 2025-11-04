# Project Structure Guide

## Recommended Structure

A typical CrewAI project should follow this structure:

```
project-name/
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── main.py               # Entry point
├── agents.py             # Agent definitions
├── tasks.py              # Task definitions
├── crew.py               # Crew configuration
├── tools/                # Custom tools (optional)
│   └── custom_tool.py
└── config/               # Configuration files (optional)
    └── agents.yaml
```

## File Descriptions

### main.py
The entry point of your application. This file:
- Loads environment variables
- Initializes the crew
- Runs the crew and handles results

### agents.py
Contains agent definitions. Each agent should have:
- **role**: The agent's function or position
- **goal**: What the agent aims to achieve
- **backstory**: Context that shapes the agent's behavior
- **tools**: Optional list of tools the agent can use

### tasks.py
Defines tasks for agents to complete. Each task includes:
- **description**: What needs to be done
- **agent**: Which agent is responsible
- **expected_output**: What the result should look like

### crew.py
Orchestrates agents and tasks:
- Assembles agents and tasks into a crew
- Defines the process (sequential or hierarchical)
- Configures crew-level settings

## Modular Approach

For larger projects, consider organizing by feature:

```
project-name/
├── features/
│   ├── research/
│   │   ├── agents.py
│   │   └── tasks.py
│   └── writing/
│       ├── agents.py
│       └── tasks.py
├── shared/
│   └── tools.py
└── main.py
```

## Configuration Files

For complex projects, use YAML configuration:

```yaml
# config/agents.yaml
researcher:
  role: "Research Analyst"
  goal: "Conduct thorough research"
  backstory: "Experienced analyst..."
```

Then load in your code:

```python
import yaml

with open('config/agents.yaml', 'r') as f:
    config = yaml.safe_load(f)
```

## Best Practices

1. **Separation of Concerns**: Keep agents, tasks, and crew logic separate
2. **Reusability**: Create functions that return agents and tasks for flexibility
3. **Documentation**: Document each agent's role and each task's purpose
4. **Environment Variables**: Never hardcode API keys or sensitive data
5. **Version Control**: Include `.env.example` but exclude `.env` from git
