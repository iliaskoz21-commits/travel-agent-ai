import gradio as gr
from app.graph import app_workflow
from app.utils import export_to_pdf

def run_app(origin, destination, user_id):
    config = {"configurable": {"thread_id": user_id}}
    inputs = {"origin": origin, "destination": destination}
    
    # Run LangGraph
    result = app_workflow.invoke(inputs, config)
    plan = result["final_itinerary"]
    pdf_path = export_to_pdf(plan)
    
    return plan, pdf_path

# Gradio Interface
demo = gr.Interface(
    fn=run_app,
    inputs=["text", "text", gr.Textbox(label="User ID", value="traveler_01")],
    outputs=["markdown", "file"],
    title="Multi-Agent Local Travel Planner",
    description="Powered by Mistral & LangGraph"
)

if __name__ == "__main__":
    demo.launch()