# ⚡ eCircuits – Simple Circuits, Powerful Learning 🚀

**eCircuits** is a personal learning project that combines:
- 🔌 Basic electrical circuit theory (DC & AC)
- 🐍 Python programming skills
- 📊 Plotting and visualization using `matplotlib`

The app simulates simple electrical components like **Resistors**, **Capacitors**, and **Inductors**, and calculates their behavior in series circuits. It also visualizes voltage changes over time or frequency.

---

## 🎯 Learning Goals

| Area             | Goal                                                                 |
|------------------|----------------------------------------------------------------------|
| 💡 Electronics   | Understand impedance, voltage-current relations, DC/AC behavior     |
| 🧠 Python        | Practice object-oriented design, modular code, and using PyCharm    |
| 📈 Plotting      | Learn how to plot with `matplotlib` and visualize data effectively  |

---

## 🛠️ What does it do?

| Module             | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `Resistor`         | Represents a resistor in Ohms                                            |
| `Capacitor`        | Represents a capacitor in Farads, reacts differently in DC/AC           |
| `Inductor`         | Represents an inductor in Henrys, creates reactance in AC               |
| `dc_analysis.py`   | Calculates total voltage from component impedances and current          |
| `plot_voltage.py`  | Plots voltage over time or other quantities using `matplotlib`          |

---

## 🧪 Example Simulation

```python
r1 = Resistor(100)          # 100 Ohm
c1 = Capacitor(1e-6)        # 1 µF
l1 = Inductor(0.01)         # 10 mH
current = 0.02              # 20 mA

voltage = calculate_series_voltage([r1, c1, l1], current)

times = [0, 1, 2, 3, 4]
voltages = [voltage.real * t / 4 for t in times]

plot_voltage_over_time(voltages, times)
