class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title.lower()
        self.duration = duration
        self.time_now = 0
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
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == password:
                    self.current_user = user
                    print(f"Вход выполнен, {nickname}")
                    return
                else:
                    print("Неверный пароль")
                    return
            else:
                print("Пользователь не найден")

    def register(self, nickname, password, age):
        if not any(user.nickname == nickname for user in self.users):
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} добавлен")
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        if self.current_user:
            print(f"Вы вышли из аккаунта {self.current_user.nickname}")
            self.current_user = None
        else:
            print("Нет активного пользователя для выхода")

    def add_videos(self, *videos):
        for video in videos:
            if not any(v.title == video.title.lower() for v in self.videos):
                self.videos.append(video)
                print(f"Видео {video.title} добавлено")
            else:
                print(f"Видео {video.title} уже существует")

    def get_videos(self, title):
        found_videos = [video.title for video in self.videos if title.lower() in video.title]
        if found_videos:
            return found_videos
        else:
            print("Видео не найдено")
            return []

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title.lower() in video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    print(f"{video.time_now + 1}", end=' ')
                    video.time_now += 1  # Симуляция просмотра видео
                print("\nКонец видео")
                video.time_now = 0  # Сбрасываем текущее время просмотра
                return
            else:
                print("Видео не найдено для просмотра")


#
if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add_videos(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')