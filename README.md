# CrewAI AI Agents

Repository to store my projects created in Crew AI, which are AI-related.

## About

This repository contains various AI agent projects built using [CrewAI](https://www.crewai.com/), a cutting-edge framework for orchestrating role-playing, autonomous AI agents. CrewAI enables the creation of sophisticated multi-agent systems where agents collaborate to accomplish complex tasks.

## Repository Structure

```
crewai-ai-agents/
├── projects/           # Individual CrewAI projects
│   └── example-project/
│       ├── agents.py       # Agent definitions
│       ├── tasks.py        # Task definitions
│       ├── crew.py         # Crew configuration
│       ├── main.py         # Entry point
│       └── requirements.txt
├── shared/            # Shared utilities and configurations
├── docs/              # Documentation
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or poetry for package management

### Installation

1. Clone this repository:
```bash
git clone https://github.com/gustavozsh/crewai-ai-agents.git
cd crewai-ai-agents
```

2. Install CrewAI and dependencies:
```bash
pip install crewai crewai-tools
```

3. Navigate to a specific project and install its requirements:
```bash
cd projects/example-project
pip install -r requirements.txt
```

### Running a Project

Each project contains its own README with specific instructions. Generally:

```bash
cd projects/<project-name>
python main.py
```

## Projects

Projects in this repository demonstrate different use cases and capabilities of CrewAI:

- More projects coming soon...

## Contributing

This is a personal learning repository, but suggestions and improvements are welcome through issues.

## Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [CrewAI Examples](https://github.com/joaomdmoura/crewAI-examples)

## License

See [LICENSE](LICENSE) file for details.