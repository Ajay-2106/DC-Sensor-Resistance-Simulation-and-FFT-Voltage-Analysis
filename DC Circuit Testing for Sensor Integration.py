import time
import random
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

data_log = []

Vcc = 5.0          # Supply voltage in Volts
R1 = 10000         # Fixed resistor in Ohms (10k)

def simulate_sensor_resistance():
    ideal_R = 10000  # 10k Ohms typical
    noise = random.uniform(-500, 500)  # Simulated variation
    noise = round(noise, 3)
    return ideal_R + noise

def calc_voltage(Rs):
    return Vcc * Rs / (R1 + Rs)

# Create filename
def given_file_name(base_name="DC_test_log", extension="csv"):
    i = 1
    while True:
        file_name = f"{base_name}_{i}.{extension}"
        file_path = f"A:/Python/Projects/Demo results/{file_name}"
        if not os.path.exists(file_path):
            return file_name
        i += 1

try:
    print("Starting DC circuit sensor simulation. Press Ctrl+C to stop.")
    while True:
        Rs = simulate_sensor_resistance()
        Vout = round(calc_voltage(Rs), 3)
        time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{time_stamp} | Sensor R = {int(Rs)} ohm | Vout = {Vout} V")
        data_log.append([time_stamp, Rs, Vout])
        time.sleep(.2)

except KeyboardInterrupt:
    print("\nAcquisition stopped.")

    file_name = given_file_name()
    with open(f"A:Python/Projects/Demo results/{file_name}", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Sensor Resistance (ohm)", "Output Voltage (V)"])
        writer.writerows(data_log)
    
    print(f"Data saved as {file_name}")
    print("Running FFT analysis.")

    value = [row[2] for row in data_log]
    N = len(value)
    Fs = 1

    fft_value = np.fft.fft(value)
    fft_frq = np.fft.fftfreq(N, d=1/Fs)

    half_N = N // 2
    plt.figure(figsize=(10, 5))
    plt.plot(fft_frq[:half_N], np.abs(fft_value[:half_N]))
    plt.title("Simulated DC Output Voltage Over Time")
    plt.xlabel("Frq (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("Sample plotted and displayed.")