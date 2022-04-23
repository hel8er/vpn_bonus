from .webhook import Webhook, Command
from bot import crud
from .schemas import Update
from .models import TgUser

bot = Webhook('5312535973:AAHvB7vKhcfs31vbuZ_sgA4lwqi_1taYe_A')


class StartCmd(Command):
    text = '/start'

    def run(self, update: Update):
        res = ""
        user, created = crud.get_or_create_user(update.message.chat)

        if update.message.text.find(' ') >= 0:
            ref_code = int(update.message.text.split(' ')[1])

            if user.id != ref_code:
                if user.joined_by is None:

                    parent = TgUser.objects.get(id=ref_code)
                    if parent:
                        crud.add_parent_ref(update.message.chat.id, ref_code)
                        bot.send_message(update.message.chat.id, "Регистрация прошла успешно!\n"
                                                                       "Задать вопрос \\ Заказать VPN 👇\n"
                                                                       "https://t.me/vpn_rabotaet")

                        res = 'connected'
                    else:

                        res = 'wrong code'

                else:
                    bot.send_message(update.message.chat.id, "Вы уже подключены")
            else:
                bot.send_message(update.message.chat.id, "Вы не можете подключиться по своей же ссылке, "
                                                               "это сслыка для приглашения друзей")

                res = "already connected"

        bot.send_message(update.message.chat.id, "Реферальная ссылка для твоих друзей:")
        bot.send_message(update.message.chat.id, "👇")
        bot.send_message(update.message.chat.id, 'https://t.me/vpnbonusbot?start=' + str(user.id))
        return res


class MyRefs(Command):
    text = '/myrefs'

    def run(self, update: Update):
        refs = crud.get_refs(update.message.chat.id)
        if refs:
            text = [f"{ref['first_name']} {ref['last_name']} @{ref['username']}" for ref in refs]
            bot.send_message(update.message.chat.id,
                                   "\n".join(text))
        else:
            bot.send_message(update.message.chat.id,
                                   "У вас еще нет подключеных рефералов")

        return True


class Contact(Command):
    text = '/contact'

    def run(self, update: Update):
        return bot.send_message(update.message.chat.id, "Задать вопрос \\ Заказать VPN 👇\n"
                                                       "Telegram : https://t.me/vpn_rabotaet")


commands = {cmd.text: cmd for cmd in Command.__subclasses__()}
cmd_list = Command.__subclasses__()
