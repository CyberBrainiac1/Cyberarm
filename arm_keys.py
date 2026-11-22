from adafruit_servokit import ServoKit

hat = ServoKit(channels=16)
angles = [90, 90, 90, 90]
keys = ["ad", "ws", "jl", "ik"]  # Base, shoulder, elbow, wrist on channels 0–3.

print("A/D base, W/S shoulder, J/L elbow, I/K wrist. Q quits.")

while True:
    key = input("> ").strip().lower()
    if key == "q":
        break

    for joint, pair in enumerate(keys):
        if key == pair[0]:
            angles[joint] -= 5
        elif key == pair[1]:
            angles[joint] += 5
        else:
            continue

        angles[joint] = max(60, min(120, angles[joint]))
        hat.servo[joint].angle = angles[joint]
