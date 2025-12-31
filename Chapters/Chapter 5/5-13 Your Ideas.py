# Mini Game Logic
walkspeed = 10
items = ["speed_boots"]
if "speed_ring" in items:
    walkspeed += 10
if "speed_boots" in items:
    walkspeed += 10

print(walkspeed)