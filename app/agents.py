import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from tavily import TavilyClient

# Φόρτωση των ρυθμίσεων από το αρχείο .env
load_dotenv()

# Αρχικοποίηση Clients
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(api_key=tavily_api_key)
llm = ChatOllama(model="mistral", temperature=0)

def web_search(query: str):
    """
    Εκτελεί αναζήτηση μέσω Tavily AI. 
    Το Tavily είναι βελτιστοποιημένο για LLMs και επιστρέφει καθαρό περιεχόμενο.
    """
    print(f"--- API CALL: Searching Tavily for: {query} ---")
    try:
        # Αναζήτηση με Tavily
        response = tavily.search(query=query, max_results=3)
        context = "\n".join([f"Source: {r['url']}\nContent: {r['content']}" for r in response['results']])
        return context if context else "No real-time data found."
    except Exception as e:
        print(f"!!! Tavily Error: {e}")
        return "Search service unavailable. Using internal AI knowledge."

# --- Nodes ---

def flight_node(state):
    print("--- AGENT: Finding Flights ---")
    query = f"cheapest flights from {state['origin']} to {state['destination']} 2026 prices"
    raw_data = web_search(query)
    
    prompt = f"You are a flight specialist. Based on this data: {raw_data}\nSummarize flight options for {state['origin']} to {state['destination']}."
    response = llm.invoke(prompt)
    return {"flight_info": response.content}

def stay_node(state):
    print("--- AGENT: Finding Stays ---")
    query = f"best rated hotels and airbnbs in {state['destination']} 2026"
    raw_data = web_search(query)
    
    prompt = f"You are an accommodation expert. Based on this data: {raw_data}\nRecommend 3 stays in {state['destination']}."
    response = llm.invoke(prompt)
    return {"accommodation_info": response.content}

def presenter_node(state):
    print("--- AGENT: Generating Professional Markdown Report ---")
    
    prompt = f"""
    You are a Senior Travel Consultant. Your goal is to present the travel options for {state['destination']} in a high-end, structured format.
    
    DATA SOURCES:
    - FLIGHT DATA: {state['flight_info']}
    - ACCOMMODATION DATA: {state['accommodation_info']}
    
    REPORT STRUCTURE:
    1. Introduction: A welcoming sentence about the trip from {state['origin']} to {state['destination']}.
    
    2. Flights Summary Table: Create a Markdown table with columns: [Airline/Provider | Estimated Price | Key Notes].
    
    3. Stays Summary Table: Create a Markdown table with columns: [Accommodation Name | Price per Night | Highlights].
    
    4. Final Advice: A short paragraph with a "pro-tip" for the traveler.
    
    FORMATTING RULES:
    - Use professional English.
    - Use Bold text for prices.
    - Use Emojis to make it visually appealing.
    - Ensure the tables are properly aligned in Markdown.
    """
    
    response = llm.invoke(prompt)
    return {"final_itinerary": response.content}