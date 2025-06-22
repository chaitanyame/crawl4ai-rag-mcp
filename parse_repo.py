import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from knowledge_graphs.parse_repo_into_neo4j import DirectNeo4jExtractor

# Load environment variables
load_dotenv()

# Set the Git path explicitly
os.environ["GIT_PATH"] = r"C:\Program Files\Git\cmd\git.exe"

async def main():
    # Get Neo4j connection details from environment variables
    neo4j_uri = os.environ.get('NEO4J_URI', 'bolt://localhost:7687')
    neo4j_user = os.environ.get('NEO4J_USER', 'neo4j')
    neo4j_password = os.environ.get('NEO4J_PASSWORD', 'password')
    
    print(f"Using Neo4j URI: {neo4j_uri}")
    print(f"Using Git path: {os.environ.get('GIT_PATH')}")
    
    # Initialize the repo extractor
    extractor = DirectNeo4jExtractor(neo4j_uri, neo4j_user, neo4j_password)
    
    try:
        # Initialize Neo4j connection and constraints
        await extractor.initialize()
        
        # Parse the repository
        repo_url = "https://github.com/mingrammer/diagrams.git"
        print(f"Parsing repository: {repo_url}")
        await extractor.analyze_repository(repo_url)
        print("Repository parsed successfully!")
        
    finally:
        # Close the Neo4j connection
        await extractor.close()

if __name__ == "__main__":
    asyncio.run(main())
