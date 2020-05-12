import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'Reminder to wash hands',
            message = 'Hey There!, Wash your Hands.',
            app_icon = 'icon.ico',
            timeout = 10
        )
    time.sleep(1*60)