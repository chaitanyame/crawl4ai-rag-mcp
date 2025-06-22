# Crawl4AI RAG MCP Server

This README provides instructions for adding the local codebase to the [crawl4ai-rag-mcp GitHub repository](https://github.com/chaitanyame/crawl4ai-rag-mcp).

## Instructions to Push the Code

You can push the code directly from this directory by adding the GitHub repository as a remote. Here's how:

1. Make sure you're authenticated with GitHub on your local machine:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. If this directory isn't already a Git repository, initialize it:
   ```
   git init
   ```

3. Make sure .env is in your .gitignore file to avoid pushing sensitive information:
   ```
   echo ".env" >> .gitignore
   ```

4. Add the GitHub repository as a remote:
   ```
   git remote add origin https://github.com/chaitanyame/crawl4ai-rag-mcp.git
   ```

5. Add all files to Git:
   ```
   git add .
   ```

6. Commit the changes:
   ```
   git commit -m "Add crawl4ai-rag MCP server with Neo4j knowledge graph for hallucination detection"
   ```

7. Push the changes to GitHub:
   ```
   git push -u origin main
   ```
   
   If the repository already has content and Git rejects the push, you may need to pull first or use force push (use with caution):
   ```
   # Pull first if needed
   git pull origin main --allow-unrelated-histories
   
   # Or force push (if you're sure you want to override the remote content)
   git push -u origin main --force
   ```

## Overview of the Codebase

This codebase implements an MCP (Model Context Protocol) server integrated with Crawl4AI and Supabase for web crawling and RAG capabilities. The server includes:

1. Web crawling functionality (automatic detection of URL types)
2. Content storage in Supabase
3. RAG (Retrieval Augmented Generation) capabilities
4. Neo4j knowledge graph for hallucination detection

## Features

- Smart URL detection
- Recursive crawling
- Parallel processing
- Vector search with source filtering
- Neo4j knowledge graph for repository parsing and code validation

## Configuration

The system can be configured via environment variables in a `.env` file. See `.env.example` for a template.

## Running the Server

Using Docker:
```bash
docker run --env-file .env -p 8051:8051 mcp/crawl4ai-rag
```

Using Python:
```bash
uv run src/crawl4ai_mcp.py
```
