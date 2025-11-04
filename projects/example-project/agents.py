from crewai import Agent


def create_researcher():
    """Create a researcher agent."""
    return Agent(
        role='Research Analyst',
        goal='Conduct thorough research on given topics and provide detailed insights',
        backstory="""You are an experienced research analyst with a keen eye for detail.
        You excel at gathering information from various sources and synthesizing it into
        clear, actionable insights. Your research is always thorough and well-documented.""",
        verbose=True,
        allow_delegation=False
    )


def create_writer():
    """Create a writer agent."""
    return Agent(
        role='Content Writer',
        goal='Create engaging and informative content based on research findings',
        backstory="""You are a skilled content writer with years of experience in
        creating compelling narratives. You have a talent for taking complex information
        and making it accessible and interesting to a wide audience.""",
        verbose=True,
        allow_delegation=False
    )
