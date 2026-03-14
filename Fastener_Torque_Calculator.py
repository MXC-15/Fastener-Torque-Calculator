import math
def calculate_torque():
    print("Mechainical Bolt Torque Calculator")
    d_mm = float(input("Enter the bolt diameter (mm): "))
    proof_stress = float(input("Enter the proof stress (MPa): "))
    k_factor = float(input("Enter the K factor (friction coefficient): "))

    d_meters = d_mm / 1000
    area = math.pi * (d_meters / 2) ** 2
    preload = 0.75 * area * proof_stress * 1e6
    
    torque = preload * k_factor * d_meters
    print(f"Preload force: {preload:.2f} N")
    print(f"The required torque is: {torque:.2f} N·m")
calculate_torque() 