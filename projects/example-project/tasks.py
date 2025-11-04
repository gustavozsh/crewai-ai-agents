from crewai import Task


def create_research_task(agent, topic):
    """Create a research task for the given topic."""
    return Task(
        description=f"""Conduct comprehensive research on the topic: {topic}
        
        Your research should include:
        1. Key concepts and definitions
        2. Current trends and developments
        3. Notable examples or case studies
        4. Future implications
        
        Provide a detailed report with your findings.""",
        agent=agent,
        expected_output="A detailed research report with key findings and insights"
    )


def create_writing_task(agent, topic):
    """Create a writing task based on research."""
    return Task(
        description=f"""Using the research provided, write an engaging article about: {topic}
        
        The article should:
        1. Have a compelling introduction
        2. Present information in a clear, logical structure
        3. Include relevant examples
        4. Conclude with key takeaways
        
        Write in an accessible style suitable for a general audience.""",
        agent=agent,
        expected_output="A well-written article that engages readers and clearly communicates the topic"
    )
