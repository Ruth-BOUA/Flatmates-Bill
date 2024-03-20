import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="p", unit="pt", format="a4")
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Insert the period
        pdf.set_font(family="times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of flatmates
        pdf.set_font(family="times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        pdf.output(f'reports/{self.filename}')
        webbrowser.open('file://' + '/Users/ruthboua/Downloads/files-master/App-2-Flatmates-Bill/reports/' + self.filename)
