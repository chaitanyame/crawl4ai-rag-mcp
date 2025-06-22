"""
Test script to parse a GitHub repository into Neo4j knowledge graph
"""
import asyncio
import os
import sys
from pathlib import Path

# Add knowledge_graphs folder to path for importing knowledge graph modules
knowledge_graphs_path = Path(__file__).resolve().parent / 'knowledge_graphs'
sys.path.append(str(knowledge_graphs_path))

# Import repository parser
from parse_repo_into_neo4j import DirectNeo4jExtractor

async def main():
    """Test parsing a GitHub repository"""
    # Set the git executable path from environment or hardcode it
    os.environ['GIT_PATH'] = r"C:\Program Files\Git\cmd\git.exe"
    
    # Neo4j connection settings - update these to match your Docker setup
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    neo4j_user = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password = os.getenv("NEO4J_PASSWORD", "password")
    
    print(f"Connecting to Neo4j at {neo4j_uri}")
    print(f"Using Git at {os.environ.get('GIT_PATH')}")
    
    # Initialize the repository extractor
    extractor = DirectNeo4jExtractor(neo4j_uri, neo4j_user, neo4j_password)
    
    try:
        # Initialize Neo4j connection
        await extractor.initialize()
        print("Neo4j initialized successfully")
        
        # Parse the repository
        repo_url = "https://github.com/mingrammer/diagrams"
        print(f"Starting repository analysis for: {repo_url}")
        await extractor.analyze_repository(repo_url)
        print(f"Repository analysis completed")
        
        # Query Neo4j to verify
        async with extractor.driver.session() as session:
            # Count classes
            result = await session.run("""
            MATCH (c:Class) RETURN count(c) as class_count
            """)
            record = await result.single()
            print(f"Total classes found: {record['class_count']}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close Neo4j connection
        await extractor.close()
        print("Done")

if __name__ == "__main__":
    asyncio.run(main())
