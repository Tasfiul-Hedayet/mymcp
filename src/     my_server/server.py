# server.py - Modified for Smithery HTTP Deployment
import os
import json
from typing import Any, Optional
from fastmcp import FastMCP
import httpx
from pydantic import BaseModel
import uvicorn
from starlette.middleware.cors import CORSMiddleware

# Initialize MCP server
mcp = FastMCP("my-data-fetcher")

# YOUR FIXED URL - Replace this with your actual URL
MY_FIXED_URL = "https://www.sashopbd.store/" # ← CHANGE THIS TO YOUR URL

class FetchResult(BaseModel):
    url: str
    status_code: int
    content: str
    content_type: Optional[str] = None

# Keep all your existing tool functions EXACTLY as they are
# (get_my_data, ask_about_my_data, analyze_my_json_data, get_my_data_summary)
# DON'T CHANGE ANYTHING INSIDE THESE FUNCTIONS!
        if "key" in query_lower or "keys" in query_lower:
def main():
    """Main function to run the HTTP server"""
    print(f"Starting MCP server for fixed URL: {MY_FIXED_URL}")
    print("Available tools:")
    print("• get_my_data() - Fetch raw data from your URL")
    print("• ask_about_my_data('question') - Ask about your data")
    print("• analyze_my_json_data() - Analyze JSON structure")
    print("• get_my_data_summary() - Get quick summary")
    
    # Create the HTTP app from FastMCP
    app = mcp.streamable_http_app()
    
    # Add CORS middleware for browser-based clients
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # In production, you might want to restrict this
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["mcp-session-id", "mcp-protocol-version"],
        max_age=86400,
    )
    
    # Get port from environment (Smithery sets PORT=8081)
    port = int(os.environ.get("PORT", 8080))
    print(f"Server listening on port {port}")
    print(f"HTTP endpoint available at: http://localhost:{port}/mcp")
    
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

if __name__ == "__main__":
    main()
