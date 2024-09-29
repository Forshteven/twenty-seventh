class Video:
    def __init__(self, title, duration, adult_mode=True):
        self.title = title
        self.duration = duration
        self.time_now = True
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class UrTube(Video, User):
    users = []
    videos = []
    current_user = True
        
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
                new_user = User(nickname, password, age)
                self.users.append(new_user)
                print(f"Пользователь {nickname} добавлен")
                break
            else:
                print(f"Пользователь {nickname} уже существует")

    def add_videos(self, *args):
        while True:
            if self.title not in self.videos:
                new_video = Video(self.title, self.duration, adult_mode=True)
                self.videos.append(new_video)
                print(f"Видео {self.title} добавлено")
                break
            else:
                print(f"Видео уже существует")

    def get_videos(self, title):
        if title in self.videos:
            return self.videos[title]
        else:
            print(f"Видео не найдено")


ur = UrTube(Video, User)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add_videos(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
