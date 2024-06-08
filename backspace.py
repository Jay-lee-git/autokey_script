# Enter script code
from datetime import datetime 
now_ = datetime.now().strftime('%Y%m%d_%H%M%S_1')
keyboard.send_keys("<ctrl>+<shift>+s")
time.sleep(0.5)
keyboard.send_keys(now_)
time.sleep(0.5)
keyboard.send_keys("<enter>")
time.sleep(0.5)
keyboard.send_keys("<enter>")
time.sleep(0.5)
keyboard.send_keys("<ctrl>+z")
keyboard.send_keys("<ctrl>+z")