import datetime
from abc import ABC, abstractmethod

class IObserver(ABC):
    """
    Interface pour les observateurs.
    Les classes qui implémentent cette interface doivent définir la méthode `update`.
    """
    @abstractmethod
    def update(self, post):
        pass
class LogObserver(IObserver):
    """
    Observateur pour la journalisation des articles.
    Implémente l'interface IObserver.
    """
    def update(self, post):
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

class EmailAdminObserver(IObserver):
    """
    Observateur pour l'envoi d'e-mails aux administrateurs.
    Implémente l'interface IObserver.
    """
    def __init__(self, admins):
        self.admins = admins

    def update(self, post):
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post['title']} » est publié.")

class EmailSubscriberObserver(IObserver):
    """
    Observateur pour l'envoi d'e-mails aux abonnés.
    Implémente l'interface IObserver.
    """
    def __init__(self, subscribers):
        self.subscribers = subscribers

    def update(self, post):
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post['title']} » disponible !")
class Blog:
    def __init__(self):
        self.posts = []
        self.observers = []
        # # Liste codée en dur d’administrateurs
        # self.admins = ['admin1@example.com', 'admin2@example.com']
        # # Liste codée en dur d’abonnés
        # self.subscribers = ['reader1@example.com', 'reader2@example.com']

    def add_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, post):
        for observer in self.observers:
            observer.update(post)

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
        self.notify_observers(post)

        # # 1) Log inline — couplage direct
        # self._log_post(post)

        # # 2) Notification admins inline — couplage direct
        # self._send_email_to_admins(post['title'])

        # # 3) Notification abonnés inline — couplage direct
        # self._notify_subscribers(post['title'])

    # def _log_post(self, post: dict):
    #     """
    #     Journalisation basique : affiche date et titre.
    #     """
    #     timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
    #     print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

    # def _send_email_to_admins(self, post_title: str):
    #     """
    #     Envoi d'e-mails aux administrateurs.
    #     """
    #     for admin in self.admins:
    #         print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post_title} » est publié.")

    # def _notify_subscribers(self, post_title: str):
    #     """
    #     Envoi d'e-mails aux abonnés.
    #     """
    #     for subscriber in self.subscribers:
    #         print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post_title} » disponible !")

def main():
    blog = Blog()
    log_observer = LogObserver()
    admin_observer = EmailAdminObserver(['admin1@example.com', 'admin2@example.com'])
    subscriber_observer = EmailSubscriberObserver(['reader1@example.com', 'reader2@example.com'])

    blog.add_observer(log_observer)
    blog.add_observer(admin_observer)
    blog.add_observer(subscriber_observer)

    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")
        

if __name__ == "__main__":
    main()