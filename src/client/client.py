from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.management.manager import GameManager

from threading import Thread
from enum import Enum, auto
from queue import Queue
import socket as sock
import pickle

from src.common.constants import ADDRESS

class Client:
    def __init__(self, manager: GameManager) -> None:
        self.manager = manager
        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.socket.connect(ADDRESS)

        self.quit_queue = Queue(maxsize=1)
        self.message_queue = Queue()
        self.receive_thread = Thread(target=self.forever_receive)
        self.receive_thread.start()

    def send(self, message: dict) -> None:
        print(f"[Sending data] Type '{message['type']}': {message['message']}")
        pickled = pickle.dumps(message)
        self.socket.send(pickled)

    def receive(self) -> None:
        try:
            pickled_data = self.socket.recv(1024)
        except ConnectionAbortedError:
            self.quit_queue.put(True)
            print("Connection closed.")
        except ConnectionResetError:
            self.quit_queue.put(True)
            print("Connection closed due to the other player disconnecting.")
        else:
            message = pickle.loads(pickled_data)
            self.message_queue.put(message)
            print(f"[Data received] Type '{message['type']}': {message['message']}")

    def forever_receive(self) -> None:
        print("Started receive thread.")
        while self.quit_queue.empty():
            self.receive()
        print("Receive thread ended.")

    @property
    def alive(self) -> bool:
        return self.quit_queue.empty()

    @property
    def has_messages(self) -> bool:
        return not self.message_queue.empty()

    def get_message(self) -> dict:
        return self.message_queue.get()

    def disconnect(self) -> None:
        print("Closing socket...")
        self.socket.close()

class MessageType(Enum):
    PLACE = auto()
    REPLENISH = auto()