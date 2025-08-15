import datetime
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    """Interface Observer pour le patron observateur"""
    
    @abstractmethod
    def update(self, subject, event_data):
        """Méthode appelée quand le sujet notifie un changement"""
        pass

class Subject(ABC):
    """Interface Subject pour le patron observateur"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """Attache un observateur"""
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Détache un observateur"""
        self._observers.remove(observer)
    
    def notify(self, event_data):
        """Notifie tous les observateurs"""
        for observer in self._observers:
            observer.update(self, event_data)

class LogObserver(Observer):
    """Observateur pour la journalisation des articles"""
    
    def update(self, subject, event_data):
        post = event_data
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

class AdminObserver(Observer):
    """Observateur pour notifier les administrateurs"""
    
    def __init__(self, admins: List[str]):
        self.admins = admins
    
    def update(self, subject, event_data):
        post = event_data
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L'article « {post['title']} » est publié.")

class SubscriberObserver(Observer):
    """Observateur pour notifier les abonnés"""
    
    def __init__(self, subscribers: List[str]):
        self.subscribers = subscribers
    
    def update(self, subject, event_data):
        post = event_data
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post['title']} » disponible !")

class Blog(Subject):
    def __init__(self):
        super().__init__()
        self.posts = []

    def new_post(self, title: str, content: str):
        """
        Crée un nouvel article, l'enregistre et notifie les observateurs
        """
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)
        
        # Notification des observateurs via le patron observateur
        self.notify(post)

def main():
    blog = Blog()
    
    # Configuration des observateurs
    log_observer = LogObserver()
    admin_observer = AdminObserver(['admin1@example.com', 'admin2@example.com'])
    subscriber_observer = SubscriberObserver(['reader1@example.com', 'reader2@example.com'])
    
    # Attachement des observateurs
    blog.attach(log_observer)
    blog.attach(admin_observer)
    blog.attach(subscriber_observer)
    
    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()