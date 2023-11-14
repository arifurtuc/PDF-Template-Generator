# Import required libraries
from fpdf import FPDF
import pandas as pd

# Create a new PDF instance with A4 size and portrait orientation
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from a CSV file
df = pd.read_csv("files/topics.csv")

# Iterate through each row in the DataFrame and add topics to the PDF
for index, row in df.iterrows():
    # Add a new page for each topic
    pdf.add_page()

    # Set font and styles for the topic text
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)

    # Add the topic text to the PDF with a line separator
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add additional pages to the PDF based on the number of pages required for a topic
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer for additional pages
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Save the PDF document as output.pdf
pdf.output("output.pdf")