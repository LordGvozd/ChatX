from abc import abstractmethod, ABC
from typing import Optional

from src.chat.chat import Chat


class DataError(Exception):
    ...


class ChatNotFoundError(DataError):
    ...


class AbstractChatRepo(ABC):
    @abstractmethod
    def save_chat_state(self, chat: Chat) -> None:
        """ Save chat state to storage """
        ...

    @abstractmethod
    def load_chat(self, id: int) -> Chat | None:
        """ Return chat, if exist, else return None """
        ...

    @abstractmethod
    def get_chats(self, *, amount: Optional[int] = None) -> list[Chat]:
        """ Get all chats from storage """
        ...


class AbstractAsyncChatRepo(AbstractChatRepo, ABC):

    async def save_chat_state(self, chat: Chat) -> None:
        raise NotImplementedError

    async def load_chat(self, id: int) -> Chat | None:
        raise NotImplementedError

    async def get_chats(self, *, amount: int = None) -> list[Chat]:
        raise NotImplementedError


class InMemoryRepo(AbstractChatRepo):
    def __init__(self):
        self.__chats: list[Chat] = []

    def save_chat_state(self, chat: Chat) -> None:
        self.__chats.append(chat)

    def load_chat(self, id: int) -> Chat:
        for c in self.__chats:
            if c.id == id:
                return c

    def get_chats(self, *, amount: Optional[int] = None) -> list[Chat]:
        if amount:
            return self.__chats[:amount]
        return self.__chats
