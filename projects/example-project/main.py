#!/usr/bin/env python
"""
Example CrewAI Project - Main Entry Point

This script demonstrates how to create and run a crew of AI agents
to research and write about a given topic.
"""

import os
from dotenv import load_dotenv
from crew import create_crew


def main():
    """Main function to run the CrewAI example."""
    
    # Load environment variables
    load_dotenv()
    
    # Check for required API keys
    if not os.getenv('OPENAI_API_KEY'):
        print("Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or as an environment variable.")
        return
    
    # Define the topic
    topic = "The impact of AI agents on modern software development"
    
    print(f"\n{'='*60}")
    print(f"Starting CrewAI Example Project")
    print(f"Topic: {topic}")
    print(f"{'='*60}\n")
    
    # Create and run the crew
    try:
        crew = create_crew(topic)
        result = crew.kickoff()
        
        print(f"\n{'='*60}")
        print("Crew Execution Completed!")
        print(f"{'='*60}\n")
        print("Result:")
        print(result)
    except Exception as e:
        print(f"\n{'='*60}")
        print("Error during crew execution!")
        print(f"{'='*60}\n")
        print(f"Error: {str(e)}")
        print("\nPlease check:")
        print("1. Your API key is valid and has sufficient credits")
        print("2. Your internet connection is stable")
        print("3. The CrewAI library is properly installed")
        return
    

if __name__ == "__main__":
    main()
