from langchain_text_splitters import TextSplitter,RecursiveCharacterTextSplitter

from hr_assistant import config

def split_into_chunks(documents):
    """
        split docs into small overlapping chunks
    """
    text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=config.CHUNK_SIZE,
    chunk_overlap=config.CHUNK_OVERLAP,
    )
    return text_splitter.split_documents(documents)