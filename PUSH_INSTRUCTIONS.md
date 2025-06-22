# Crawl4AI RAG MCP Server

This README provides instructions for adding the local codebase to the [crawl4ai-rag-mcp GitHub repository](https://github.com/chaitanyame/crawl4ai-rag-mcp).

## Instructions to Push the Code

It looks like this directory is already a Git repository pointing to `coleam00/mcp-crawl4ai-rag.git`. Since you want to push to your own repository `chaitanyame/crawl4ai-rag-mcp.git`, follow these steps:

1. Check your current remote settings:
   ```
   git remote -v
   ```

2. If the origin is pointing to coleam00's repository, remove it and add your own:
   ```
   git remote remove origin
   git remote add origin https://github.com/chaitanyame/crawl4ai-rag-mcp.git
   ```

   Or if you want to keep the original remote but add yours as well:
   ```
   git remote add my-repo https://github.com/chaitanyame/crawl4ai-rag-mcp.git
   ```

3. Make sure .env is in your .gitignore file to avoid pushing sensitive information:
   ```
   echo ".env" >> .gitignore
   ```

4. If you have uncommitted changes, add and commit them:
   ```
   git add .
   git commit -m "Add crawl4ai-rag MCP server with Neo4j knowledge graph for hallucination detection"
   ```

5. Push the changes to your GitHub repository:
   ```
   # If you renamed the original origin
   git push -u origin main
   
   # Or if you added a new remote named 'my-repo'
   git push -u my-repo main
   ```
   
6. If the repository already has content and Git rejects the push, you may need to pull first or use force push:
   ```
   # Pull first if needed (use this if you renamed 'origin')
   git pull origin main --allow-unrelated-histories
   
   # Or force push (use with caution)
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
