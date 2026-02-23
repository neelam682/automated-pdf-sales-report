import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Load data
df = pd.read_csv("sales_data.csv")

total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
best_month = df.groupby("Month")["Revenue"].sum().idxmax()

# Create PDF
pdf = SimpleDocTemplate("sales_report.pdf")
elements = []

styles = getSampleStyleSheet()
elements.append(Paragraph("<b>Sales Report</b>", styles["Title"]))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph(f"Total Revenue: ${total_revenue}", styles["Normal"]))
elements.append(Paragraph(f"Average Revenue: ${average_revenue:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Top Product: {top_product}", styles["Normal"]))
elements.append(Paragraph(f"Best Month: {best_month}", styles["Normal"]))

pdf.build(elements)

print("PDF report generated: sales_report.pdf")