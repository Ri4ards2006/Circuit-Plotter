from flask import Blueprint, render_template, request
from circuits.resistor import Resistor
from circuits.capacitor import Capacitor
from circuits.inductor import Inductor
from simulations.dc_analysis import calculate_series_voltage
from plots.plot_voltage import generate_plot
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None

    if request.method == 'POST':
        r = float(request.form.get('resistor', 100))
        c = float(request.form.get('capacitor', 1e-6))
        l = float(request.form.get('inductor', 0.01))
        i = float(request.form.get('current', 0.02))

        r1 = Resistor(r)
        c1 = Capacitor(c)
        l1 = Inductor(l)

        spannung = calculate_series_voltage([r1, c1, l1], i)
        result = f"{spannung.real:.2f} V"

        # Plot & save
        times = [0, 1, 2, 3, 4]
        voltages = [spannung.real * t / 4 for t in times]
        plot_url = generate_plot(voltages, times)

    return render_template('index.html', result=result, plot_url=plot_url)
