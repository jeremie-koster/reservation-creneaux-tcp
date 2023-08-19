from selenium import webdriver
from src.domain.booking import BookingWish
from src.interfaces.player_credentials import LocalCredentialsFetcher
from usecases.uc_booking import UseCaseBooking
from src.usecases.usecases import Usecase



def main(usecase: Usecase, input_data):
    match usecase:
        case Usecase.BOOKING.value:
            print("Booking usecase")
            booking_uc = setup_booking_uc(input_data)
            booking_uc.execute()


def setup_booking_uc(booking_input) -> UseCaseBooking:
    driver = setup_selenium_driver()
    booking_model = setup_booking_wish(booking_input)
    credentials = setup_credentials()
    return UseCaseBooking(driver, booking_model, credentials)



def setup_selenium_driver():
    return webdriver.Chrome()

def setup_booking_wish(booking_data: dict) -> BookingWish:
    return BookingWish(
        partner_first_name=booking_data["partner_first_name"],
        partner_last_name=booking_data["partner_last_name"],
        court_surface=booking_data["court_surface"],
        date=booking_data["date"],
        min_start_time=booking_data["min_time"],
        max_start_time=booking_data["max_time"]
    )

def setup_credentials():
    return LocalCredentialsFetcher()

if __name__ == "__main__":
    print("--- Starting ---")
    payload = {
        "partner_first_name": "Aurélien",
        "partner_last_name": "Buchet",
        "court_surface": "TB",
        "date": "15-08-2023",
        "min_time": "16:15",
        "max_time": "16:45"
    }
    main("booking", payload)
