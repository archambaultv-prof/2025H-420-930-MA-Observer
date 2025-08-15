# Natacha MEYER 

import datetime
from abc import ABC, abstractmethod

class IObservateur(ABC):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def __str__(self):
        print(self.email)
        return self.email

    @abstractmethod
    def mettre_a_jour(self, title, email):
        pass

class Admin(IObservateur):
    def mettre_a_jour(self, post_title: str, admins):       # _send_email_to_admins
        """
        Envoi d'e-mails aux administrateurs.
        """
        print(f"[E-MAIL ADMIN] À : {admins} — L’article « {post_title} » est publié.")

class Subscriber(IObservateur):
    def mettre_a_jour(self, post_title: str, subscribers):  # _notify_subscribers
        """
        Envoi d'e-mails aux abonnés.
        """
        print(f"[E-MAIL ABONNÉ] À : {subscribers} — Nouvel article : « {post_title} » disponible !")

class Emetteur:
    def __init__(self):
        self.observateurs: list[IObservateur] = []

    def afficher_observateur(self):
        for i in self.observateurs:
            print(i.email)

    def ajouter_observateur(self, observateur: IObservateur):
        self.observateurs.append(observateur)

    def notifier_observateurs(self, post_title):
        for observateur in self.observateurs:
            observateur.mettre_a_jour(post_title, observateur.email)

class Blog(Emetteur):
    def __init__(self):
        super().__init__()
        self.posts = []

    def new_post(self, title: str, content: str):
        """
        Crée un nouvel article, l'enregistre et déclenche :
            1. le log
            2. la notification des admins & des abonnés
        """
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)

        # 1) Log inline — couplage direct
        self._log_post(post)

        # 2) Notification admins & abonnés inline — couplage direct
        self.notifier_observateurs(post['title'])

    def _log_post(self, post: dict):
        """
        Journalisation basique : affiche date et titre.
        """
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

def main():
    blog = Blog()

    admins = ['admin1@example.com', 'admin2@example.com']
    subscribers = ['reader1@example.com', 'reader2@example.com']

    for a in admins:
        blog.ajouter_observateur(Admin(a))
    for s in subscribers:
        blog.ajouter_observateur(Subscriber(s))

    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()
