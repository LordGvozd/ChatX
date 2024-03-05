from fastapi import APIRouter, Response
from fastapi.exceptions import *

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
                raise HTTPException(status_code=404, detail="Chat not found")
            except service_layer_exception.UserNotInChatError:
                raise HTTPException(status_code=403, detail="User not in chat")
            else:
                response.status_code = 201

        @self.__router.post("/new_chat")
        async def new_chat(response: Response) -> int:
            new_chat = self.__chat_service.create_new_chat()
            response.status_code = 201

            return new_chat.id

        @self.__router.post("/add_member")
        async def add_member(chat_id: int, user: User, response: Response):
            try:
                self.__chat_service.add_member_to_chat(chat_id, user)
                response.status_code = 201
            except service_layer_exception.ChatNotFound:
                raise HTTPException(status_code=404, detail="Chat not found")

            except service_layer_exception.UserAlreadyInChat:
                raise HTTPException(status_code=409, detail="User already in chat")

        @self.__router.get("get_messages")
        async def get_messages(chat_id: int, response: Response):
            try:
                messages = self.__chat_service.get_messages(chat_id=chat_id)
                return messages
            except service_layer_exception.ChatNotFound:
                raise HTTPException(status_code=404, detail="Chat not found")





