from mcp.server.fastmcp import FastMCP
# Import your existing RAG function
from my_rag_logic import query_rag

# Initialize the MCP server
mcp = FastMCP("MyRAGServer")

@mcp.tool()
def search_knowledge_base(query: str) -> str:
    """Use this to search the RAG knowledge base for information."""
    # Call your existing RAG function
    return query_rag(query)

if __name__ == "__main__":
    mcp.run()