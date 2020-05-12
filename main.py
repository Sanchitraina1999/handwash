import time
from plyer import notification

while True:
    notification.notify(
        title = 'Reminder to wash hands',
        message = 'Hey There!, Wash your Hands.',
        app_icon = 'icon.ico',
        timeout = 10
    )
    time.sleep(30*60)