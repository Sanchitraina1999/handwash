import time
from plyer import notification

while True:
    notification.notify(
        title = 'Reminder to wash hands',
        message = 'Hey There!, Wash your Hands.',
        app_icon = '/home/sanchit199/Desktop/handwash/icon.ico',
        timeout = 10
    )