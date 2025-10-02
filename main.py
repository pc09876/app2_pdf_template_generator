from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format='A4') # Defining a pdf instance
pdf.set_auto_page_break(auto=False, margin=0) # Disabling the auto page break
df = pd.read_csv("topics.csv") # Defining the dataframe

for index, row in df.iterrows():

    # Setting up the front page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    """
    Defines the font for the front page. 
    heading Style B --> Bold
    """
    pdf.set_text_color(100, 100, 100)  # fonts color (0 to 254) --> dark grey
    pdf.cell(w=0, h=12, align='L', txt=row["Topic"], border=0, ln=1)
    """
    w --> cell width. 0: the cells expands through the entire width of the page.
    h --> height of the cell.
    align --> text alignment. L: aligned to the left of the cell.
    border --> cell border. 0 - nonvisible, 1 - visible. 
    ln --> breakline between cells. 0 - no breakline, 1 - single breakline
    """
    # Multiple lines generation
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)
    """
    x1, y1 --> coordinated for the starting point of the line (distance from the page's top and left sides).
    x2, y2 --> coordinated for the ending point of the line (distance from the page's top and left sides).
    """

    # Setting up the footer for the front page
    pdf.ln(265) # Add a break line at a certain distance from the top of the page (in mm)
    pdf.set_font('Arial', 'I', 8)  # Style I --> Italic
    pdf.set_text_color(180, 180, 180)
    # noinspection PyArgumentList
    pdf.cell(w=0, h=10, align='R', txt=row["Topic"], border=0)

    # Blank pages generation
    # noinspection PyTypeChecker
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Multiple lines generation
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

        # Setting up the footer for the blank pages
        pdf.ln(277)
        pdf.set_font('Arial', 'I', 8)  # Style I --> Italic
        pdf.set_text_color(180, 180, 180)
        # noinspection PyArgumentList
        pdf.cell(w=0, h=10, align='R', txt=row["Topic"], border=0)

# Generating the pdf file
pdf.output("output.pdf")