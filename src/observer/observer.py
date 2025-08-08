import datetime
from abc import ABC, abstractmethod

class Observateur(ABC):
   
    @abstractmethod
    def mise_a_jour(self, post: dict):
        pass
"""
Ajout de la class Blog qui gère les posts et les observateurs
"""
class Blog:
    def __init__(self):
        self.posts = []
        self.observateurs = []

    def attacher(self,observateur:Observateur):
        if observateur not in self.observateurs:
            self.observateurs.append(observateur)

    def detacher(self,observateur:Observateur):
        if observateur in self.observateurs:
            self.observateurs.remove(observateur)
    
    def notifier(self, post: dict):
        for observateur in self.observateurs:
            observateur.mise_a_jour(post)



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
# Anciennes méthodes qu'on remplace par le patron observateur self.notifier(post)
        # def _log_post(self, post: dict):
        #     timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        #     print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")
        # 
        # def _send_email_to_admins(self, post_title: str):
        #     for admin in self.admins:
        #         print(f"[E-MAIL ADMIN] À : {admin} — L'article « {post_title} » est publié.")
        # 
        # def _notify_subscribers(self, post_title: str):
        #     for subscriber in self.subscribers:
        #         print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post_title} » disponible !")
        # Notifier tous les observateurs
        self.notifier(post)

    def _log_post(self, post: dict):
        
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

    def _send_email_to_admins(self, post_title: str):
        """
        Envoi d'e-mails aux administrateurs.
        """
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post_title} » est publié.")

    def _notify_subscribers(self, post_title: str):
        """
        Envoi d'e-mails aux abonnés.
        """
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post_title} » disponible !")
    
    """
    Class logger recoit un post et l'affiche dans le log
    """
class Logger(Observateur): 
    def mise_a_jour(self, post: dict):
        
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

#Ici on crée les classes qui gèrent les emails
class EmailAdminNotifier(Observateur):
    def mise_a_jour(self, post: dict):
        print(f"[E-MAIL ADMIN] L'article « {post['title']} » est publié.")

class EmailSubscriberNotifier(Observateur):
    def mise_a_jour(self, post: dict):
        print(f"[E-MAIL ABONNÉ] Nouvel article : « {post['title']} » disponible !")

def main():
    blog = Blog()
#Ici on crée les observateurs qu'on attache au blog
    # Créer les observateurs
    logger = Logger()
    email_admin = EmailAdminNotifier()
    email_subscriber = EmailSubscriberNotifier()
    
    # Bim bam boum on attache les observateurs au blog
    blog.attacher(logger)
    blog.attacher(email_admin)
    blog.attacher(email_subscriber)
    
    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

   



if __name__ == "__main__":
    main()