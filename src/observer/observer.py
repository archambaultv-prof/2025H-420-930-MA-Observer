import datetime
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, post: dict):
        pass

class Blog:
    def __init__(self):
        self.posts = []
        # Liste codée en dur d’administrateurs
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)


    def _notify_observers(self, post: dict):
        for observer in self.observers:
            observer.update(post)

    def new_post(self, title: str, content: str):
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)
        self._notify_observers(post)


    class Logger(Observer):
            pass
    class AdminNotifier(Observer):
        pass
    
    class SubscriberNotifier(Observer):
        pass

   

def main():
    blog = Blog()
    # Ajouter les observateurs
    blog.add_observer(Logger())
    blog.add_observer(AdminNotifier())
    blog.add_observer(SubscriberNotifier())

    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")


if __name__ == "__main__":
    main()