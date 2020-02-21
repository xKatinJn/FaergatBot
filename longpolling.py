import random

from scripts.data_scripts import csv_writer
from faergatbot import vk, longpoll
from vk_api.bot_longpoll import VkBotEventType


static_nums = ['44', '443', '387', '187', '99']
csv_path = 'users_info.csv'
user_ids = []

print('yes')
for event in longpoll.listen():
    print('loop')
    print(event.obj)
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            with open('users_info.csv', 'r') as file:
                data = file.readlines()

            for user_info in data:
                user = user_info.rstrip().split(',')
                print(user)
                if user[0] not in user_ids:
                    user_ids.append(user[0])

            if str(event.object.from_id) not in user_ids:
                num = random.choice(static_nums)
                user_id = event.object.from_id
                info = str(user_id) + ',' + num
                csv_writer(csv_path, info.split(','))
                vk.messages.send(peer_id=event.object.peer_id,
                                 message=f'Вам присвоен номер участника {num}. В ближайшее время мы проведем итоги '
                                         'конкурса и пришлем Вам результаты. Удачи!', random_id=0)

    except Exception as exc:
        print(exc)
