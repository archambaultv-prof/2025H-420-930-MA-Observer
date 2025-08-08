import datetime
from abc import ABC, abstractmethod

# Interface abstraite pour les observateurs
class Observateur(ABC):
    @abstractmethod
    def mise_a_jour(self, sujet):
        pass

# Blog ne sait plus QUI fait quoi ; il diffuse juste l’événement
class Blog:
    def __init__(self):
        self.posts = []
        self._observateurs = []
    #remplace les listes fixes par attacher/detacher qui permettent d’ajouter ou retirer n’importe quel observateur
    def attacher(self, observateur: Observateur):
        self._observateurs.append(observateur)

    def detacher(self, observateur: Observateur):
        self._observateurs.remove(observateur)




    def notifier(self, post):
        for obs in self._observateurs:   # <-  déclenche chaque observateur
            obs.mise_a_jour(post)

    def new_post(self, title: str, content: str):
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)
        self.notifier(post)       # <- plus de couplage direct


#====================================================================
# Chaque classe  remplace une méthode privée de l’ancienne version :
class LogObservateur(Observateur):
    def mise_a_jour(self, post):
        print('log', post['title'])

class AdminObservateur(Observateur):
    def __init__(self):
        self.admins = ['admin1@example.com', 'admin2@example.com']

    def mise_a_jour(self, post):
        for admin in self.admins:
            print('admin', admin, post['title'])

class SubscriberObservateur(Observateur):
    def __init__(self):
        self.subscribers = ['reader1@example.com', 'reader2@example.com']

    def mise_a_jour(self, post):
        for subscriber in self.subscribers:
            print('sub', subscriber, post['title'])

def main():
    blog = Blog()
    
    # Attacher les observateurs
    blog.attacher(LogObservateur())
    blog.attacher(AdminObservateur())
    blog.attacher(SubscriberObservateur())
    
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()