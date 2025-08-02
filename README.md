# DC Sensor Resistance Simulation and FFT Voltage Analysis

This Python project simulates a DC voltage divider circuit using a variable resistor as the sensor. It mimics real-time sensor fluctuations by introducing noise in the resistance value and calculates the output voltage accordingly. The data is timestamped, logged into a CSV file, and followed by a frequency spectrum analysis using FFT.

## 🔧 Circuit Model

- **Voltage Source (Vcc)**: 5.0 V
- **Fixed Resistor (R1)**: 10 kΩ
- **Sensor Resistor (Rs)**: Varies between ~9500 Ω and ~10500 Ω (with added noise)
- **Output Voltage (Vout)** is calculated using: Vout = Vcc × Rs / (R1 + Rs)

## 📌 Features

- Real-time simulation of sensor resistance variation
- Output voltage calculation based on the DC voltage divider principle
- Timestamped data logging into uniquely named CSV files
- Frequency spectrum analysis using Fast Fourier Transform (FFT)
- Live plot of frequency components using matplotlib

## 📁 Output

- **CSV File Structure**: Timestamp, Sensor Resistance (ohm), Output Voltage (V)

- **FFT Plot**:
Shows the frequency components of the voltage signal

## 💻 Requirements

- Python 3.x
- NumPy
- Matplotlib
