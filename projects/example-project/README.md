# Example CrewAI Project

This is a template project demonstrating the basic structure of a CrewAI application.

## Overview

This example project shows how to:
- Define AI agents with specific roles and goals
- Create tasks for agents to complete
- Orchestrate agents in a crew to accomplish complex objectives

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

3. Run the project:
```bash
python main.py
```

## Project Structure

- `agents.py` - Agent definitions with roles, goals, and backstories
- `tasks.py` - Task definitions that agents will complete
- `crew.py` - Crew configuration that orchestrates agents and tasks
- `main.py` - Entry point to run the crew
- `requirements.txt` - Project dependencies
- `.env.example` - Example environment variables

## Customization

Modify the agents, tasks, and crew configuration to suit your specific use case.
