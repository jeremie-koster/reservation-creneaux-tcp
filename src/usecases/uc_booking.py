from src.domain.booking import BookingWish
from src.interfaces.player_credentials import CredentialsFetcher
from src.interfaces.website_handler import authenticate, complete_booking_form

TCP_WEBSITE_URL = "https://www.tennisclubdeparis.fr/"
TCP_RESERVATION_URL = "https://www.tennisclubdeparis.fr/fo/prive/reservation/reserver/step1"

class UseCaseBooking:
    def __init__(self, driver, booking_wish: BookingWish, credentials: CredentialsFetcher) -> None:
        self.driver = driver
        self.booking_wish = booking_wish
        self.credentials = credentials

    # func execute
    # - connexion
    # - sélectionner le bon jour et créneau horaire (simple web, jour, créneau de 2h)
    # - wait for liste des créneaux
    # - récupère la liste des créneaux dispo et l'envoie à l'algo du meilleur choix -> test possible
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
        print("Authentication successful")

        self.driver.get(TCP_RESERVATION_URL)
        self.book_tennis_slot(self.driver, self.booking_wish)


        self.driver.close()


    def book_tennis_slot(self, driver, booking_wish: BookingWish):
        # remplit le formulaire -> interface
        approximate_period_ideal_time = booking_wish.get_approximate_time_period_starting_at(booking_wish.ideal_start_time)
        complete_booking_form(driver, approximate_period_ideal_time, booking_wish.date_of_play, booking_wish.booking_type)
        # parser la liste des créneaux dispo -> interface
        # créer un DF, filtrer sur les min/max -> domain
        # ajout colonne : distance du créneau par rapport à l'idéal
        # trier sur cette colonne
        # si égalités, utiliser la surface pour choisir le créneau à réserver
        # tout en conservant cette liste (au cas où la réservation échoue et pour donner les autres choix possibles), cliquer sur le créneau choisi
        # remplir nom partenaire et valider
        pass