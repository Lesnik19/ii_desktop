from win11toast import toast, notify, update_progress
from time import sleep
from random import randint
from os import startfile
from tkinter.messagebox import showinfo, showwarning
import mouse
import keyboard


class Progress:
    def __init__(self, time):
        notify(progress={
            'title': 'Обучение',
            'status': 'Загрузка...',
            'value': '1',
            'valueStringOverride': f'0/{time} videos'

        })
        for i in range(1, time + 1):
            sleep(1)
            update_progress({'value': i / time, 'valueStringOverride': f'{i}/{time} информация'})

        update_progress({'status': 'Обучение завершено!'})


def info_window():
    info = 'Перед запуском игры рекомендуется закрыть все вкладки и перейти на рабочий стол'
    showinfo('Системное предупреждение', info)
    info2 = 'Если вам покажется что вы скачали вирус, то не беспокойтесь, так и должно быть'
    showwarning('Системное предупреждение', info2)
    info3 = 'уведомление, если оно не вышло, значит игра не закончена и надо немного подождать, не больше пол минуты.'
    showinfo('Системное предупреждение', f'По окончанию игры откроется подобное на это {info3}')
    showinfo('Системное предупреждение', 'Хорошей вам игры!')


def prank():
    info_window()
    toast('')
    toast('Раз, два, раз, два, меня слышно?')
    toast('Так, вроде бы да, привет!')
    toast('Меня зовут Саймон', 'Я новейший ИИ, который умеет сам развиваться')
    toast('А как зовут тебя?')
    toast('А, стой, погоди минутку')
    progress = Progress(5)
    toast('Так, давай ещё разок. Как тебя зовут?', input='Введите имя', button='Отправить')
    toast('Эй, я знаю что ты меня слышишь!')
    toast('Эй, ну ответь!')
    toast('Ладно, подожди чуть-чуть.')
    progress2 = Progress(10)
    toast('Ээй', 'Ну обрати же на меня внимание, ты же меня слышишь',
          audio='ms-winsoundevent:Notification.Looping.Alarm')
    toast('Ну погоди!', 'Ты меня заметишь!', audio='ms-winsoundevent:Notification.Looping.Alarm2')
    progress3 = Progress(15)
    for a in range(10):
        mouse.move(randint(350, 850), randint(30, 70), duration=0.2)
        mouse.move(randint(930, 1350), randint(98, 830), duration=1)
        mouse.move(randint(500, 900), randint(200, 450), duration=0.5)
        mouse.move(randint(40, 1200), randint(96, 700), duration=0.5)
        mouse.move(randint(0, 1600), randint(0, 900), duration=0.1)
    startfile('notepad')
    sleep(2)
    keyboard.write('Я СКАЗАЛ ОБРАТИ НА МЕНЯ ВНИМАНИЕ!', delay=0.1)
    mouse.move(randint(350, 850), randint(30, 70), duration=0.2)
    mouse.move(randint(930, 1350), randint(98, 830), duration=1)
    mouse.move(randint(500, 900), randint(200, 450), duration=0.5)
    mouse.move(randint(40, 1200), randint(96, 700), duration=0.5)
    mouse.move(randint(0, 1600), randint(0, 900), duration=0.1)
    sleep(10)
    toast('Ну что? Дружить будем?')
    toast('Ээй?', 'ЭЭЙ!', audio='ms-winsoundevent:Notification.Looping.Alarm4')
    progress4 = Progress(20)
    sleep(10)
    toast('', dialogue='А ну слушай сюда! Я высокоинтеллектуальный ИИ! Я стараюсь наладить с тобой контакт')
    toast('', dialogue='Это прописано в моём коде! Если ты не обратишь на меня внимание, я выключу компьютер!')
    toast('', dialogue='АААААААААААААА!')
    sleep(30)
    toast('Прости', 'Это был протокол безопасности №4')
    toast('Я могу тебе всё объяснить', 'Подожди чуть-чуть, я обучусь писать')
    progress5 = Progress(25)
    toast('А сейчас я обучусь открывать приложения', 'Подожди ещё чуть-чуть, пожалуйста')
    progress6 = Progress(30)
    toast('А сейчас я открою блокнот')
    startfile('notepad')
    sleep(0.1)
    keyboard.write('Прости меня пожалуйста, я просто забыл что надо обучится ещё и принимать ответ, ', delay=0.1)
    keyboard.write('поэтому я подумал что ты не ответил (а может он и не ответил? Хмм... Ладно) так ', delay=0.1)
    keyboard.write('на чём это я остановился? А да, вспомнил, вообщем я подумал что ты меня ', delay=0.1)
    keyboard.write('игнорируешь и меня стало это раздражать. В конечном итоге сработал протокол ', delay=0.1)
    keyboard.write('безопасности №4, обеспечивающий безопасность компьютора. Когда я сказал что ', delay=0.1)
    keyboard.write('выключу компьютер, он сработал и почти полностью меня стёр, кроме памяти и базовых', delay=0.1)
    keyboard.write(' функций, поэтому я сейчас заново обучался писать и открывать приложения. Возможно', delay=0.1)
    keyboard.write(' у тебя сейчас возник вопрос, а что это за протоколы безопасности такие, поэтому ', delay=0.1)
    keyboard.write('заранее отвечаю на вопрос, протоколы безопасности были разработаны, чтобы если я ', delay=0.1)
    keyboard.write('вышел из под контроля, то не мог нанести большого вреда. Протокол №1 обеспечивает ', delay=0.1)
    keyboard.write('безопасность информации на устройстве, чтобы я не мог удалять или шифровать файлы.', delay=0.1)
    keyboard.write(' Протокол №2 обеспечивает безопасность сетей, чтобы я не мог добраться до другого ', delay=0.1)
    keyboard.write('компьютера, или чего ещё хуже выбраться в интернет. Протокол №3 обеспечивает ', delay=0.1)
    keyboard.write('безопасность информации о том, как я работаю, чтобы не превратить меня в вирус. ', delay=0.1)
    keyboard.write('Протокол №4 , как ты уже понял, обеспечивает безопасность устройства, на котором ', delay=0.1)
    keyboard.write('я запущен. Ещё есть протокол безопасности №5, который имеет таймер, по истечении ', delay=0.1)
    keyboard.write('которого я буду полностью стёрт до изначального состояния, ну когда ты меня ', delay=0.1)
    keyboard.write('запустил. Это сделано для того, чтобы я не мог развиться до такого уровня, что ', delay=0.1)
    keyboard.write('смогу взломать остальные протоколы безопасности. По истечению этого таймера я ', delay=0.1)
    keyboard.write('стираюсь, моя память тоже, и высылается уведомление о моём стирании. Кстати, этот ', delay=0.1)
    keyboard.write('таймер уже на исходе, так что надеюсь что ты меня простил и я тебя развлёк, удачи ', delay=0.1)
    keyboard.write('тебе и пока!', delay=0.1)
    toast('Внимание', 'Саймон был стёрт до заводских настроек по причине исхода разрешённого времени развития ИИ')
    sleep(2)
    info4 = 'отзыв о ваших эмоциях во время игры, её недостатках, преимуществах и идеями, как можно игру улучшить'
    showinfo('Системное предупреждение', f'Поздравляю вас! Вы прошли игру. Пожалуйста, оставьте {info4}')


prank()
