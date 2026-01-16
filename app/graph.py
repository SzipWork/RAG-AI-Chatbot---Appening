from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional, List
from app.vectorstore import get_vectorstore
from app.llm import get_llm


vectorstore = get_vectorstore()
llm = get_llm()


#state
class ChatState(TypedDict):
    question: str
    context: Optional[str]
    answer: Optional[str]
    route: Optional[str]



def route_query(state: ChatState):
    q = state["question"].lower().strip()

    greetings = [
        "hi", "hello", "hii", "hey",
        "good morning", "good afternoon",
        "good evening", "good night"
    ]

    if q in greetings:
        return {"route": "greeting"}

    if "summarize" in q or "summary" in q:
        return {"route": "summarize"}

    return {"route": "rag"}



def retrieve_context(state: ChatState):
    
    docs = vectorstore.similarity_search(
        state["question"],
        k=15 
    )

    if not docs:
        return {"context": None}

    
    context = "\n\n".join(
        f"[Page {doc.metadata.get('page', 'N/A')}]\n{doc.page_content}"
        for doc in docs
    )

    return {"context": context}


#answer generator
def generate_answer(state: ChatState):

    
    if state["route"] == "greeting":
        return {
            "answer": "Hey.. I can answer detailed questions and summarize content from the Agentic AI Ebook."
        }

    
    if state["route"] == "summarize" and state["context"]:
        prompt = f"""
You are an expert technical summarizer.

Summarize the following ebook content clearly, accurately, and concisely.
Preserve key concepts, steps, and terminology.
Use ONLY the provided content.

Content:
{state["context"]}
"""
        res = llm.invoke(prompt)
        return {"answer": res.content}

   
    if state["context"]:
        prompt = f"""
You are an expert AI assistant answering STRICTLY from the Agentic AI Ebook.

INSTRUCTIONS:
- Use ONLY the provided context.
- Combine information from multiple sections if needed.
- Answer in detail with clear explanations.
- If the answer is not explicitly present, respond exactly with:
  "Sorry, this question is not covered in the Agentic AI Ebook."

Context:
{state["context"]}

Question:
{state["question"]}
"""
        res = llm.invoke(prompt)
        return {"answer": res.content}

    
    return {
        "answer": "Sorry, this question is not covered in the Agentic AI Ebook."
    }


#graph
graph = StateGraph(ChatState)

graph.add_node("route", route_query)
graph.add_node("retrieve", retrieve_context)
graph.add_node("generate", generate_answer)

graph.set_entry_point("route")

graph.add_edge("route", "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

chat_graph = graph.compile()
