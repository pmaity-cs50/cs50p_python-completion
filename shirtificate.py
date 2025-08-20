from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")
    pdf.ln(30)


    pdf.image("shirtificate.png", x=10, y=80, w=190)


    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.cell(0, 180, f"{name} took CS50", align="C")


    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
