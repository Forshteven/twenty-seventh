class Video:
    def __init__(self, title, duration, adult_mode=True):
        self.title = title.lower()
        self.duration = duration
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = True

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                if password == self.users[nickname]:
                    print(f"Вход выполнен, {nickname}")
                else:
                    print("Неверный пароль")

    def register(self, nickname, password, age):
        if nickname not in self.users:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print(f"Пользователь {nickname} добавлен")
        else:
            print(f"Пользователь {nickname} уже существует")

    def add_videos(self, *video):
        for video in self.videos:
            if video.title.lower() not in self.videos:
                self.videos.append(video)
                print(f"Видео {video.title} добавлено")
            else:
                print(f"Видео уже существует")

    def get_videos(self, title):
        for video in self.videos:
            if video.title == title:
                return video
            else:
                print(f"Видео не найдено")


#
# if __name__ == "__main__":

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add_videos(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
