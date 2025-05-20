from dotenv import load_dotenv
from typing import Literal, Annotated, List, Union
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Load API key
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model_name="gpt-4o")

# Define classifier schema
class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response."
    )

# Define state schema
class State(TypedDict):
    messages: Annotated[List[Union[dict, HumanMessage, AIMessage]], add_messages]
    message_type: Union[str, None]

def get_message_content(message):
    """Helper function to get content from either dict or message object"""
    if isinstance(message, dict):
        return message["content"]
    return message.content

# Define classifier function
def classify_message(state: State):
    last_message = state["messages"][-1]
    content = get_message_content(last_message)

    parser = PydanticOutputParser(pydantic_object=MessageClassifier)

    messages = [
        {
            "role": "system",
            "content": f"""Classify the user message as either 'emotional' or 'logical'. 
            Return a JSON object that matches this schema: {parser.get_format_instructions()}
            
            Examples:
            User: "I'm feeling really sad today"
            {{"message_type": "emotional"}}
            
            User: "What's the capital of France?"
            {{"message_type": "logical"}}"""
        },
        {"role": "user", "content": content} 
    ]

    output = llm.invoke(messages)
    result = parser.parse(output.content)
    return {"message_type": result.message_type}

# Define therapist agent
def therapist_agent(state: State):
    last_message = state["messages"][-1]
    content = get_message_content(last_message)

    messages = [
        {"role": "system",
         "content": """You are a compassionate therapist. Focus on the emotional aspects.
                        Show empathy, validate feelings, and help process emotions.
                        Ask thoughtful questions to explore feelings more deeply.
                        Avoid giving logical solutions unless explicitly asked."""},
        {"role": "user", "content": content}
    ]

    reply = llm.invoke(messages)
    return {
        "messages": state["messages"] + [{"role": "assistant", "content": reply.content}]
    }

# Define logical agent
def logical_agent(state: State):
    last_message = state["messages"][-1]
    content = get_message_content(last_message)

    messages = [
        {"role": "system",
         "content": """You are a purely logical assistant. Focus only on facts.
            Provide clear, concise answers based on logic and evidence.
            Do not address emotions or provide emotional support."""},
        {"role": "user", "content": content}
    ]

    reply = llm.invoke(messages)
    return {
        "messages": state["messages"] + [{"role": "assistant", "content": reply.content}]
    }

# Build the LangGraph
graph_builder = StateGraph(State)

graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

graph_builder.add_edge(START, "classifier")

graph_builder.add_conditional_edges(
    "classifier",
    lambda state: "therapist" if state["message_type"] == "emotional" else "logical",
    {"therapist": "therapist", "logical": "logical"}
)

graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

graph = graph_builder.compile()

# Run the chatbot
def run_chatbot():
    state: State = {"messages": [], "message_type": None}

    print("Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Assistant: Take care! 👋")
            break

        # Add user message as a dictionary
        state["messages"].append({"role": "user", "content": user_input})

        # Invoke the graph
        state = graph.invoke(state)

        # Print the assistant's response
        if state["messages"]:
            last_msg = state["messages"][-1]
            content = get_message_content(last_msg)
            print(f"Assistant: {content}\n")

if __name__ == "__main__":
    run_chatbot()