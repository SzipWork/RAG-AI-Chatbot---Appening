from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.vectorstore import get_vectorstore


def ingest_pdf(pdf_path: str):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages from PDF")


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,        
        chunk_overlap=250,      
        separators=[
            "\n\n",             
            "\n",              
            ". ",               
            " ",                
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} text chunks")


    for chunk in chunks:
        if "page" not in chunk.metadata:
            chunk.metadata["page"] = "unknown"

#vector db storing
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    vectorstore.persist()

    print("Ebook fully ingested into vector database")


if __name__ == "__main__":
    ingest_pdf("Ebook.pdf")
