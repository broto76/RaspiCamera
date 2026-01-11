import time
from picamera2 import Picamera2, Preview

# 1. Initialize the camera
picam2 = Picamera2()

# 2. Configure the camera for previewing
# This sets up internal streams for the display
config = picam2.create_preview_configuration()
picam2.configure(config)

# 3. Open the preview window
# Preview.QTGL is recommended for best performance on Raspberry Pi
picam2.start_preview(Preview.QTGL)

# 4. Start the actual camera stream
picam2.start()

# Let the preview run for 5 seconds
print("Preview started. Closing in 600 seconds...")
time.sleep(600)

# 5. Clean up
picam2.stop_preview()
picam2.stop()

