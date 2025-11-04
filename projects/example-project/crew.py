from crewai import Crew, Process
from agents import create_researcher, create_writer
from tasks import create_research_task, create_writing_task


def create_crew(topic):
    """Create and configure the crew with agents and tasks."""
    
    # Create agents
    researcher = create_researcher()
    writer = create_writer()
    
    # Create tasks
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer, topic)
    
    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew
