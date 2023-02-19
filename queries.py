from process import Booking
def listBookings_resolver(obj, info):
    try:
        bookings = [booking.to_dict() for booking in Booking.query.all()]
        print(bookings)
        payload = {
            "success": True,
            "bookings": bookings
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload