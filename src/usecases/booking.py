from src.domain.booking import BookingWish
from src.interfaces.player_credentials import CredentialsFetcher
from src.interfaces.website_handler import authenticate

TCP_WEBSITE_URL = "https://www.tennisclubdeparis.fr/"
class UseCaseBooking:
    def __init__(self, driver, booking_wish: BookingWish, credentials: CredentialsFetcher) -> None:
        self.driver = driver
        self.booking_wish: booking_wish
        self.credentials = credentials

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
        authenticate(self.driver, self.credentials, TCP_WEBSITE_URL)
        self.driver.close()


