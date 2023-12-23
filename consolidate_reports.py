from PyPDF2 import PdfFileMerger

def consolidate_reports():
    merger = PdfFileMerger()

    reports = ["assets_sensing_report.pdf", "ambient_sensing_report.pdf", "data_sensing_report.pdf",
               "first_mes_report.pdf", "equipment_sensing_report.pdf", "process_sensing_report.pdf"]

    for report in reports:
        merger.append(report)

    merger.write("consolidated_reports.pdf")
    merger.close()

if __name__ == "__main__":
    consolidate_reports()
