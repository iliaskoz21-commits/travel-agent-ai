import pytest
import os
from app.graph import app_workflow
from app.utils import export_to_pdf

def test_workflow_structure():
    """
    Test to verify if the LangGraph is correctly initialized 
    with all the required nodes.
    """
    # Retrieve the names of the nodes in the graph
    nodes = app_workflow.nodes
    assert "flights" in nodes
    assert "stays" in nodes
    assert "presenter" in nodes
    print("\n✅ Graph structure is correct!")

def test_pdf_generation():
    """
    Test to verify if the PDF export utility correctly 
    generates a file on disk.
    """
    test_text = "This is a test itinerary from Athens to London."
    path = export_to_pdf(test_text)
    
    # Check if file exists and has the correct name
    assert os.path.exists(path)
    assert path == "itinerary.pdf"
    
    # Cleanup: remove the test file after assertion
    if os.path.exists(path):
        os.remove(path)
    print("✅ PDF Utils working correctly!")

def test_database_connection():
    """
    Test to verify if the SqliteSaver (checkpoint) 
    initializes without errors.
    """
    from app.database import get_sqlite_memory
    saver = get_sqlite_memory()
    assert saver is not None
    print("✅ SqliteSaver initialized successfully!")