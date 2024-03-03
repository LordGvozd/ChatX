from dataclasses import dataclass
from pydantic import BaseModel


class ChatError(Exception):
    ...


class UserNotInChatError(ChatError):
    ...


class User(BaseModel):
    id: int
    name: str


class Message(BaseModel):
    from_user: int
    chat_id: int
    text: str


class Chat:
    def __init__(self, *, id: int, members: list[User], messages: list[Message]):
        self.__id: int = id
        self.__members: list[User] = members
        self.__messages: list[Message] = messages

    def add_message(self, message: Message):
        members_ids = [u.id for u in self.__members]

        if message.from_user not in members_ids:
            raise UserNotInChatError

        self.__messages.append(message)

    def add_member(self, user: User):
        self.__members.append(user)

    @property
    def members(self) -> list[User]:
        return self.__members

    @property
    def messages(self) -> list[Message]:
        return self.__messages

    @property
    def id(self) -> int:
        return self.__id
