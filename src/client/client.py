from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.management.manager import GameManager

from threading import Thread
from queue import Queue
from typing import Any
import socket as sock
import pickle

from src.common.constants import ADDRESS

class Client:
    def __init__(self, manager: GameManager) -> None:
        self.manager = manager
        self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.socket.connect(ADDRESS)

        self.quit_queue = Queue(maxsize=1)
        self.data_queue = Queue()
        self.receive_thread = Thread(target=self.forever_receive)
        self.receive_thread.start()

    def send(self, message: Any) -> None:
        print(f"Sending data: {message}")
        pickled = pickle.dumps(message)
        self.socket.send(pickled)

    def receive(self) -> None:
        try:
            pickled = self.socket.recv(1024)
        except ConnectionAbortedError:
            self.quit_queue.put(True)
            print("Connection closed.")
        else:
            message = pickle.loads(pickled)
            self.data_queue.put(message)
            print(f"Data received: {message}")

    def forever_receive(self) -> None:
        print("Started receive thread.")
        while self.quit_queue.empty():
            self.receive()
        print("Receive thread ended.")

    @property
    def has_data(self) -> bool:
        return not self.data_queue.empty()

    def get_data(self) -> Any:
        return self.data_queue.get()

    def disconnect(self) -> None:
        print("Closing socket...")
        self.socket.close()