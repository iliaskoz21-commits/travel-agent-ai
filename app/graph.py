from typing import TypedDict
from langgraph.graph import StateGraph, END
from .agents import flight_node, stay_node, presenter_node
from .database import get_sqlite_memory

class AgentState(TypedDict):
    origin: str
    destination: str
    flight_info: str
    accommodation_info: str
    final_itinerary: str

# Define the state machine (Graph)
workflow = StateGraph(AgentState)

workflow.add_node("flights", flight_node)
workflow.add_node("stays", stay_node)
workflow.add_node("presenter", presenter_node)

workflow.set_entry_point("flights")
workflow.add_edge("flights", "stays")
workflow.add_edge("stays", "presenter")
workflow.add_edge("presenter", END)

# Compile with SQLite Memory
app_workflow = workflow.compile(checkpointer=get_sqlite_memory())