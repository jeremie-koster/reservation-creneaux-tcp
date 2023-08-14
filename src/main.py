from selenium import webdriver
from usecases.usecases import Usecase



def main(usecase: Usecase):
    match usecase:
        case Usecase.BOOKING.value:
            setup_booking_uc()

def setup_booking_uc():
    # return driver, booking wish et credentials, puis lance l'uc
    print("Youpi")

if __name__ == "__main__":
    print("Starting")
    main("booking")