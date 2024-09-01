sleeptime=1-0.5
# Cut selected content
keyboard.send_keys("<ctrl>+x")
time.sleep(sleeptime)

keyboard.send_keys("/dlsfkdlstngkr")
time.sleep(sleeptime)

# Press Enter
keyboard.send_keys("<enter>")
time.sleep(sleeptime)

# Paste the previously cut content
keyboard.send_keys("<ctrl>+v")
time.sleep(sleeptime)

# Press Enter
keyboard.send_keys("<enter>")
