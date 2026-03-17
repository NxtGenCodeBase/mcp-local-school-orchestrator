from mcp.server.fastmcp import FastMCP
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3
import os

mcp = FastMCP("SchoolAdminServer")


@mcp.tool()
def get_student_info(name: str) -> str:
    """Fetch GPA and Grade for a specific student."""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    result = cursor.fetchone()
    conn.close()
    return f"Found: {result}" if result else "Student not found."


@mcp.tool()
def list_top_performers(min_gpa: float = 3.5) -> str:
    """List students with a GPA above a certain threshold."""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, gpa FROM students WHERE gpa >= ?", (min_gpa,))
    results = cursor.fetchall()
    conn.close()
    return str(results)


@mcp.tool()
def generate_pdf_report(filename: str = "School_Report.pdf") -> str:
    """Generates a PDF report of all student performance insights."""
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, gpa FROM students")
    data = cursor.fetchall()
    conn.close()

    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "🏫 School Performance Insights")
    y = 720
    for name, gpa in data:
        c.drawString(100, y, f"Student: {name} | GPA: {gpa}")
        y -= 20
    c.save()
    return f"✅ PDF Report created at: {os.path.abspath(filename)}"


if __name__ == "__main__":
    mcp.run(transport='stdio')
