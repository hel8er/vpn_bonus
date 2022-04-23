from .models import TgUser
from .schemas import Update, Chat


def get_or_create_user(chat: Chat):
    try:
        user = TgUser.objects.get(id=chat.id)
        return user, False
    except TgUser.DoesNotExist:
        user = TgUser.objects.create(**chat.dict())
        user.save()
        return user, False


def get_refs(id):
    user = TgUser.objects.get(pk=id)
    return user.refs


def add_parent_ref(id, ref):
    user = TgUser.objects.get(id=id)
    user.joined_by = ref
    user.save()
    return user