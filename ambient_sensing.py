import schedule
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class AmbientSensing:
    def __init__(self):
        self.temperature_history = []
        self.pressure_history = []
        self.co2_levels = []
        self.particulate_levels = []

    def update_temperature(self, temperature):
        self.temperature_history.append(temperature)

    def update_pressure(self, pressure):
        self.pressure_history.append(pressure)

    def update_co2_levels(self, co2_level):
        self.co2_levels.append(co2_level)

    def update_particulate_levels(self, particulate_level):
        self.particulate_levels.append(particulate_level)

    def generate_report(self):
        filename = "ambient_sensing_report.pdf"
        with canvas.Canvas(filename, pagesize=letter) as pdf:
            pdf.drawString(100, 750, "Ambient Sensing Report")
            pdf.drawString(100, 730, f"Timestamp: {time.ctime()}")
            # Adicione informações específicas do relatório

def job():
    ambient_sensing = AmbientSensing()
    ambient_sensing.update_temperature(25)
    ambient_sensing.update_co2_levels(400)
    ambient_sensing.generate_report()

schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
