import random

import pytest

from src.chat.chat import *
from src.data.repository import InMemoryRepo
from src.service_layer.servicies import ChatService
from src.service_layer.exception import *


def get_base_chat():
    return Chat(id=1,
                members=[User(id=u, name=f"User-{u}") for u in range(10)],
                messages=[])


def test_send_normal_message():
    repo = InMemoryRepo()

    chat = get_base_chat()
    repo.save_chat_state(chat)

    chat_service = ChatService(repo)
    chat_service.send_message(Message(from_user=1, chat_id=1, text="Test"))

    chat = repo.load_chat(1)

    assert chat.messages[0].text == "Test"


def test_send_message_chat_not_found():
    repo = InMemoryRepo()
    chat = get_base_chat()
    repo.save_chat_state(chat)

    chat_service = ChatService(repo)

    with pytest.raises(ChatNotFound):
        chat_service.send_message(Message(from_user=1, chat_id=100, text="Test"))


def test_send_message_user_not_in_chat():
    repo = InMemoryRepo()
    chat = get_base_chat()
    repo.save_chat_state(chat)

    chat_service = ChatService(repo)

    with pytest.raises(UserNotInChatError):
        chat_service.send_message(Message(from_user=100, chat_id=1, text="Test"))


def test_create_new_chat():
    repo = InMemoryRepo()
    chat_service = ChatService(repo)

    chat_service.create_new_chat()
    chat_service.create_new_chat()
    chat_service.create_new_chat()

    assert (repo.get_chats()[0].id == 1 and repo.get_chats()[1].id == 2 and repo.get_chats()[2].id == 3)


def test_get_messages():
    repo = InMemoryRepo()
    chat = get_base_chat()
    repo.save_chat_state(chat)

    chat_service = ChatService(repo)

    [chat.add_message(Message(from_user=random.randint(0, 9), chat_id=1, text=f"{i}")) for i in range(30)]
    repo.save_chat_state(chat)

    assert len(chat_service.get_messages(1)) == 30

    for i in range(30):
        assert chat_service.get_messages(1)[i].text == str(i)
