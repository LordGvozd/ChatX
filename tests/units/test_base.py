import pytest

from src.chat.chat import *
from src.data.repository import InMemoryRepo


def test_save_message():
    repo = InMemoryRepo()

    chat = Chat(
        id=1,
        members=[User(id=1, name="User1")],
        messages=[]
    )

    chat.add_message(Message(
        from_user=1,
        chat_id=1,
        text="TEST1"
    ))

    repo.save_chat_state(chat)

    assert repo.get_chats(amount=1)[0].messages[0].text == "TEST1"


def test_user_not_in_chat_cant_write():

    chat = Chat(
        id=1,
        members=[User(id=1, name="User1")],
        messages=[]
    )

    with pytest.raises(UserNotInChatError):
        chat.add_message(Message(
                from_user=2,
                chat_id=1,
                text="TEST1"
            ))


