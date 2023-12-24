import schedule
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class AssetsSensing:
    def __init__(self):
        self.assets_location = {}
        self.supply_routes_checklist = []
        self.standard_operation_time = 0

    def update_assets_location(self, asset_id, location):
        self.assets_location[asset_id] = location

    def add_supply_route_checklist(self, route):
        self.supply_routes_checklist.append(route)

    def set_standard_operation_time(self, time):
        self.standard_operation_time = time

    def generate_report(self):
        filename = "assets_sensing_report.pdf"
        with canvas.Canvas(filename, pagesize=letter) as pdf:
            pdf.drawString(100, 750, "Assets Sensing Report")
            pdf.drawString(100, 730, f"Timestamp: {time.ctime()}")
            # Adicione informações específicas do relatório

def job():
    assets_sensing = AssetsSensing()
    assets_sensing.update_assets_location('asset1', 'location1')
    assets_sensing.add_supply_route_checklist('route1')
    assets_sensing.set_standard_operation_time(10)
    assets_sensing.generate_report()

schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
