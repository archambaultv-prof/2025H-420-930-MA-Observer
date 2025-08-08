import datetime

# --- Les Observateurs ---
class LoggerObserver:
    def update(self, post):
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

class AdminEmailObserver:
    def __init__(self, admins):
        self.admins = admins

    def update(self, post):
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post['title']} » est publié.")

class SubscriberEmailObserver:
    def __init__(self, subscribers):
        self.subscribers = subscribers

    def update(self, post):
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post['title']} » disponible !")

# --- Blog ---
class Blog:
    def __init__(self):
        self.posts = []
        # Liste codée en dur d’administrateurs
        self.admins = ['admin1@example.com', 'admin2@example.com']
        # Liste codée en dur d’abonnés
        self.subscribers = ['reader1@example.com', 'reader2@example.com']

        # Création des observateurs
        self.logger = LoggerObserver()
        self.admin_notifier = AdminEmailObserver(self.admins)
        self.subscriber_notifier = SubscriberEmailObserver(self.subscribers)

    def new_post(self, title: str, content: str):
        """
        Crée un nouvel article, l'enregistre et déclenche :
         1. le log
         2. la notification des admins
         3. la notification des abonnés
        """

        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)

        # Appels directs aux observateurs
        self.logger.update(post)
        self.admin_notifier.update(post)
        self.subscriber_notifier.update(post)

# --- Main ---
def main():
    blog = Blog()
    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()
