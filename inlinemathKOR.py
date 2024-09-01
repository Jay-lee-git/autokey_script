
sliptime= 0.1
# Cut selected content
keyboard.send_keys("<ctrl>+x")
time.sleep(sliptime)

keyboard.send_keys("/dlsfkdls tngkr")
time.sleep(sliptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(0.4)

# Paste the previously cut content
keyboard.send_keys("<ctrl>+v")
time.sleep(sliptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(sliptime)