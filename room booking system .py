rooms = {
    101: ["Single", 1200, "Available"],
    102: ["Double", 1800, "Available"],
    103: ["Deluxe", 2500, "Available"],
    104: ["Single", 1200, "Available"],
    105: ["Deluxe", 2500, "Available"]
}

bookings = {}
booking_id = 1001


def view_rooms():
    print("\n===== ROOM DETAILS =====")
    print("Room No. | Type   | Price/Night | Status")

    for room_no, details in rooms.items():
        print(
            room_no, "|",
            details[0], "| Rs.", 
            details[1], "|",
            details[2]
        )


def book_room():
    global booking_id

    print("\n===== BOOK A ROOM =====")

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    view_rooms()

    try:
        room_no = int(input("\nEnter room number: "))

        if room_no not in rooms:
            print("Invalid room number!")
            return

        if rooms[room_no][2] == "Booked":
            print("Sorry! This room is already booked.")
            return

        nights = int(input("Enter number of nights: "))

        if nights <= 0:
            print("Number of nights must be greater than 0.")
            return

        room_type = rooms[room_no][0]
        price = rooms[room_no][1]
        total = price * nights

        bookings[booking_id] = {
            "name": name,
            "phone": phone,
            "room": room_no,
            "room_type": room_type,
            "nights": nights,
            "total": total
        }

        rooms[room_no][2] = "Booked"

        print("\n===== BOOKING SUCCESSFUL =====")
        print("Booking ID:", booking_id)
        print("Customer:", name)
        print("Room:", room_no)
        print("Room Type:", room_type)
        print("Nights:", nights)
        print("Total Amount: Rs.", total)

        booking_id += 1

    except ValueError:
        print("Please enter a valid number.")


def search_booking():
    print("\n===== SEARCH BOOKING =====")

    try:
        bid = int(input("Enter Booking ID: "))

        if bid in bookings:
            booking = bookings[bid]

            print("\nBooking Found!")
            print("Customer:", booking["name"])
            print("Phone:", booking["phone"])
            print("Room:", booking["room"])
            print("Room Type:", booking["room_type"])
            print("Nights:", booking["nights"])
            print("Total Amount: Rs.", booking["total"])

        else:
            print("Booking not found.")

    except ValueError:
        print("Please enter a valid Booking ID.")


def cancel_booking():
    print("\n===== CANCEL BOOKING =====")

    try:
        bid = int(input("Enter Booking ID: "))

        if bid not in bookings:
            print("Booking not found.")
            return

        room_no = bookings[bid]["room"]

        rooms[room_no][2] = "Available"

        del bookings[bid]

        print("Booking cancelled successfully.")

    except ValueError:
        print("Please enter a valid Booking ID.")


def checkout():
    print("\n===== CHECK-OUT =====")

    try:
        bid = int(input("Enter Booking ID: "))

        if bid not in bookings:
            print("Booking not found.")
            return

        booking = bookings[bid]
        room_no = booking["room"]

        print("\n===== FINAL BILL =====")
        print("Customer:", booking["name"])
        print("Room:", room_no)
        print("Room Type:", booking["room_type"])
        print("Number of Nights:", booking["nights"])
        print("Total Amount: Rs.", booking["total"])

        rooms[room_no][2] = "Available"

        del bookings[bid]

        print("\nCheck-out completed successfully.")

    except ValueError:
        print("Please enter a valid Booking ID.")


def main():
    while True:

        print("   HOTEL ROOM BOOKING SYSTEM")
        print("================================")
        print("1. View Rooms")
        print("2. Book a Room")
        print("3. Search Booking")
        print("4. Cancel Booking")
        print("5. Check-out")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            search_booking()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("\nThank you for using Hotel Room Booking System!")
            break

        else:
            print("Invalid choice! Please try again.")


main()