from fpdf import FPDF

def export_to_pdf(text):
    """Helper to generate a PDF file from the itinerary."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Encode to handle special characters for basic FPDF
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, clean_text)
    path = "itinerary.pdf"
    pdf.output(path)
    return path