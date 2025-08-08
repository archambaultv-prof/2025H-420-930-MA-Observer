import datetime
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, post: dict):
        """
        Méthode à implémenter par les observateurs pour recevoir des notifications.
        """
        pass





class Admin(Observer):
    def update(self, post: dict):
        """
        Implémentation de la méthode update pour les administrateurs.
        Envoie un e-mail aux administrateurs à propos du nouvel article.
        """
        print(f"[E-MAIL ADMIN] À :")
    
    

# When using an observer template, there is a subject, which is the object that changes.
# Here, the class Blog acts as the subject.
# Every time there is a change in the subject, it notifies its observers.
# The observers are other portions of the program that need to know there was a change, so they are added to the list of observers within the subject.
# Although there is only 1 subject here, we can still try and follow the SOLID principles for a better understanding of the application and the principles themselves


class Notifier:
    def __init__(self):
        self._observers = list[Observer] = []

    def attach_observer(self, observateur: Observer):
        """
        Attache un nouvel observateur.
        """
        self._observers.append(observateur)

    def detach_observer(self, observateur: Observer):
        """
        Détache un observateur existant.
        """
        self._observers.remove(observateur)

    def notify(self, title: str, content: str):
        """
        Notifie tous les observateurs d'un changement.
        """
        for observer in self._observers:
            observer.update(title, content)


class Blog(Notifier):
    def __init__(self):
        super().__init__()
        self._posts = []
        # Liste codée en dur d’administrateurs
        # self.admins = ['admin1@example.com', 'admin2@example.com']
        # Liste codée en dur d’abonnés
        # self.subscribers = ['reader1@example.com', 'reader2@example.com']
        
        # Liste d'observateurs
        self._observers = []

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
        self._posts.append(post)

        # 1) Log inline — couplage direct
        self._log_post(post)

        # 2) Notification admins inline — couplage direct
        self._send_email_to_admins(post['title'])

        # 3) Notification abonnés inline — couplage direct
        self._notify_subscribers(post['title'])

    def _log_post(self, post: dict):
        """
        Journalisation basique : affiche date et titre.
        """
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

    def _send_email_to_admins(self, post_title: str):
        """
        Envoi d'e-mails aux administrateurs.
        """
        for admin in self._admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post_title} » est publié.")

    def _notify_subscribers(self, post_title: str):
        """
        Envoi d'e-mails aux abonnés.
        """
        for subscriber in self._subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post_title} » disponible !")

def main():
    blog = Blog()
    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()