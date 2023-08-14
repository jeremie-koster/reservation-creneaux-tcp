from domain.booking import BookingWish


class UseCaseBooking:
    def __init__(self, driver, booking_wish: BookingWish) -> None:
        self.driver = driver

    # func execute
    # - connexion
    # - sélectionner le bon jour et créneau horaire
    # - wait for liste des créneaux
    # - récupère la liste des créneaux dispo et l'envoie à l'algo du meilleur choix
    # Click sur le bon créneau
    # Wait la page du partenaire
    # Remplir le nom du partenaire
    # Attendre statut vert
    # Click sur Valider
    # ---
    # Inputs : credentials, souhait de créneau, nom partenaire
    # Output : les créneaux proches de celui demandé


    def execute(self):
        pass