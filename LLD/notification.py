from abc import ABCMeta, abstractmethod
from enum import Enum


class NotificationType(Enum):
    SMS = 1
    EMAIL = 2
    WHATSAPP = 3


class MessageFormat(Enum):
    TEXT = 1
    QR = 2


class NotificationSender(metaclass=ABCMeta):
    @abstractmethod
    def send_notification(self):
        pass


class Notification:
    def __init__(self, notification_sender) -> None:
        self.notification_sender = notification_sender

    @abstractmethod
    def send_message(self):
        pass


class TextMessage(Notification):
    def __init__(self, notification_sender) -> None:
        super().__init__(notification_sender)
        print("This is a Text Message")

    def send_message(self):
        self.notification_sender.send_notification()


class QRMessage(Notification):
    def __init__(self, notification_sender) -> None:
        super().__init__(notification_sender)
        print("This is a QR Code")

    def send_message(self):
        self.notification_sender.send_notification()


class SMSNotification(NotificationSender):
    def send_notification(self):
        print("Sending SMS Notification")


class EMAILNotification(NotificationSender):
    def send_notification(self):
        print("Sending Email Notification")


if __name__ == "__main__":

    text = TextMessage(EMAILNotification())
    text.send_message()

    qr = QRMessage(EMAILNotification())
    text.send_message()
