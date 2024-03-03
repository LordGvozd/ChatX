from fastapi import APIRouter, Response

from src.chat.chat import *
from src.data.repository import AbstractChatRepo
from src.service_layer.servicies import ChatService
import src.service_layer.exception as service_layer_exception

class WebChat:
    def __init__(self, *, router: APIRouter, repo: AbstractChatRepo):

        self.__chat_service = ChatService(repo)

        self.__router = router

    def create_chat_endpoints(self) -> None:
        """ Create chat endpoint """
        @self.__router.post("/send_message")
        async def send_message(message: Message, response: Response):
            try:
                self.__chat_service.send_message(message)
            except service_layer_exception.ChatNotFound:
                response.status_code = 404
            except service_layer_exception.UserNotInChatError:
                response.status_code = 403
            else:
                response.status_code = 201

        @self.__router.post("/new_chat")
        async def new_chat(message: Message, response: Response):
            ...

        @self.__router.get("get_messages")
        async def get_messages(chat_id: int):
            ...




