from SecondExercise import HookStr
from ThirdExercise import MailBox, create_config


if __name__ == '__main__':
    # 1-2 exercises
    string = "[()()()()({[]})(){}{(((())))}]"
    hook_str = HookStr()
    hook_str.push(string)
    print(hook_str.is_balanced())
    # 3 exercise
    path = "settings.ini"
    create_config(path)
    mail_box = MailBox()
    mail_box.send_message()
    mail_box.receive_message()
