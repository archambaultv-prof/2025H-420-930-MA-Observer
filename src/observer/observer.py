import datetime

class Observer:
    def update(self, post: dict):
        raise NotImplementedError("La méthode update doit être implémentée.")

class Logger(Observer):
    def update(self, post: dict):
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

class AdminNotifier(Observer):
    def __init__(self, admins):
        self.admins = admins

    def update(self, post: dict):
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post['title']} » est publié.")

class SubscriberNotifier(Observer):
    def __init__(self, subscribers):
        self.subscribers = subscribers

    def update(self, post: dict):
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post['title']} » disponible !")

class Blog:
    def __init__(self):
        self.posts = []
        self.admins = ['admin1@example.com', 'admin2@example.com']
        self.subscribers = ['reader1@example.com', 'reader2@example.com']
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, post: dict):
        for observer in self.observers:
            observer.update(post)

    def new_post(self, title: str, content: str):
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)
        self.notify_observers(post)

def main():
    blog = Blog()
    # Ajout des observateurs
    blog.add_observer(Logger())
    blog.add_observer(AdminNotifier(blog.admins))
    blog.add_observer(SubscriberNotifier(blog.subscribers))

    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()
