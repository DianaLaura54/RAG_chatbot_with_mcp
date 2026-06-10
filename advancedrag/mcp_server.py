from mcp.server.fastmcp import FastMCP
from rag import retrieve_context

mcp = FastMCP("MyRAGServer")

@mcp.tool()
def search_knowledge_base(query: str) -> str:
    return retrieve_context(query)

if __name__ == "__main__":
    mcp.run()