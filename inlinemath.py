
sliptime= 0.1
# Cut selected content
keyboard.send_keys("<ctrl>+x")
time.sleep(sliptime)

keyboard.send_keys("/inline math")
time.sleep(sliptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(sliptime+0.1)

# Paste the previously cut content
keyboard.send_keys("<ctrl>+v")
time.sleep(sliptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(sliptime)