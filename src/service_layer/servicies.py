from typing import Optional

from src.chat.chat import Message, Chat, User
from src.data.repository import AbstractChatRepo

from src.service_layer.exception import *


class ChatService:
    def __init__(self, repo: AbstractChatRepo):
        self.__repo = repo

    def send_message(self, message: Message) -> None:
        """ Send message, or raise exceptions """
        chat_to_send = self.__repo.load_chat(message.chat_id)

        # If chat not exist
        if not chat_to_send:
            raise ChatNotFound(f"Chat with id {message.chat_id} not found!")

        chat_to_send.add_message(message)

        self.__repo.save_chat_state(chat_to_send)

    def create_new_chat(self) -> Chat:
        """ Create new chat """
        last_chat_id = len(self.__repo.get_chats())

        new_chat = Chat(
            id=last_chat_id+1,
            members=[],
            messages=[]
        )

        self.__repo.save_chat_state(new_chat)

        return new_chat

    def get_messages(self, chat_id: int) -> list[Message]:
        """ Get messages from chat with chat_id """
        chat_to_get = self.__repo.load_chat(chat_id)

        # If chat not exist
        if not chat_to_get:
            raise ChatNotFound

        return chat_to_get.messages

    def add_member_to_chat(self, chat_id, user: User):
        chat_to_add = self.__repo.load_chat(chat_id)

        if not chat_to_add:
            raise ChatNotFound

        chat_to_add.add_member(user)
        self.__repo.save_chat_state(chat_to_add)


