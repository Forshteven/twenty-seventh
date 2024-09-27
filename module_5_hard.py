class UrTube:
    users = {}
    videos = {}
    def __init__(self, current_user):
        self.current_user = current_user

    def log_in(self, nickname, password):
        while True:
            if nickname in self.users[nickname]:
                self.current_user = nickname
                if password == self.users[nickname]:
                    print(f"Вход выполнен, {nickname}")
                    break
                else:
                    print("Неверный пароль")

    def register(self, nickname, password, age):
        while True:
            if nickname not in self.users[nickname]:
                self.users.setdefault(nickname, password, age)
                print(f"Пользователь {nickname} добавлен")
                break
            else:
                print(f"Пользователь {nickname} уже существует")

    def add(self, *args):
        for i in args
            if isinstance(i, Video):
                self.videos.setdefault(i)

    def get_videos(self, title):
        return [i for i in self.videos if title in i]


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age