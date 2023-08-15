from selenium import webdriver
from domain.booking import BookingWish
from interfaces.player_credentials import LocalCredentialsFetcher
from usecases.booking import UseCaseBooking
from usecases.usecases import Usecase



def main(usecase: Usecase, input_data):
    match usecase:
        case Usecase.BOOKING.value:
            booking_uc = setup_booking_uc()
            booking_uc.execute()


def setup_booking_uc() -> UseCaseBooking:
    driver = setup_selenium_driver()
    booking_data = setup_booking_wish()
    credentials = setup_credentials()
    return UseCaseBooking(driver, booking_data, credentials)



def setup_selenium_driver():
    return webdriver.Chrome()

def setup_booking_wish(booking_data: dict) -> BookingWish:
    return BookingWish(
        partner_first_name=booking_data["partner_first_name"],
        partner_last_name=booking_data["partner_lastname"],
        court_surface=booking_data["court_surface"],
        date=booking_data["date"],
        min_start_time=booking_data["min_time"],
        max_start_time=booking_data["max_time"]
    )

def setup_credentials():
    return LocalCredentialsFetcher()

if __name__ == "__main__":
    print("Starting")
    payload = {
        "partner_first_name": "Aurélien",
        "partner_last_name": "Buchet",
        "court_surface": "TB",
        "date": "15-08-2023",
        "min_time": "16:15",
        "max_time": "16:45"
    }
    main("booking", payload)
