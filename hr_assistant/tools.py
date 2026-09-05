from langchain.tools import tool

def create_search_tool(retriever):
    """
        Returns tool that searches HR policy doc
    """
    @tool 
    def search_hr_policy(question:str)->str:
        """Searches the HR policy document for information relevant to the question."""
        matching_chunks=retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)
    return search_hr_policy