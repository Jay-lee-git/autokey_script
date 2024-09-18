
keyboard.send_keys("<ctrl>+b")
time.sleep(0.5)

# Press Enter
keyboard.send_keys("<ctrl>+<shift>+h")
time.sleep(sleeptime)

# Paste the previously cut content
keyboard.send_keys("<ctrl>+v")
time.sleep(sleeptime)

# Press Enter
keyboard.send_keys("<enter>")