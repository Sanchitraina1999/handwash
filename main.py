import time
from plyer import notification

if __name__ == '__main__':
        notification.notify(
            title = 'Reminder to wash hands',
            message = 'Hey There!, Wash your Hands.',
            app_icon = '/home/sanchit199/Desktop/handwash/icon.ico',
            timeout = 10
        )