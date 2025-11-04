# Shared Utilities

This directory contains shared utilities, tools, and configurations that can be used across multiple CrewAI projects.

## Contents

- Custom tools that can be reused in different projects
- Common agent configurations
- Shared utility functions
- Reusable prompt templates

## Usage

Import shared utilities in your projects:

```python
# Example: Using a shared custom tool
import sys
sys.path.append('../../shared')

from tools.custom_search import CustomSearchTool

# Use the tool in your agent
agent = Agent(
    role='Researcher',
    tools=[CustomSearchTool()],
    ...
)
```

## Adding Shared Utilities

When creating utilities that might be useful across multiple projects:

1. Add them to this directory
2. Document their usage
3. Include examples
4. Consider writing tests

## Best Practices

- Keep utilities generic and reusable
- Document parameters and return values
- Version shared code appropriately
- Test thoroughly before using in production
