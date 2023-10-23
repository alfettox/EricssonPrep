class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_occupied = False

class Hotel:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def is_room_available(self, room_number):
        room = self.rooms.get(room_number)
        return room is not None and not room.is_occupied

    def book_room(self, room_number):
        room = self.rooms.get(room_number)
        if room is not None:
            if room.is_occupied:
                return "Room is already occupied."
            room.is_occupied = True
            return f"Room {room_number} has been booked. Enjoy your stay!"
        return "Room not found."

    def display_rooms(self):
        room_info = []
        for room in self.rooms.values():
            status = "Occupied" if room.is_occupied else "Available"
            room_info.append(f"Room {room.room_number} ({room.room_type}): ${room.price} - {status}")
        return room_info

if __name__ == "__main__":
    hotel = Hotel()

    single_room = Room(1, "Single", 100)
    double_room = Room(2, "Double", 150)
    suite_room = Room(3, "Suite", 200)

    hotel.add_room(single_room)
    hotel.add_room(double_room)
    hotel.add_room(suite_room)

    while True:
        print("Hotel Room Booking Menu:")
        print("1. Check Room Availability")
        print("2. Book a Room")
        print("3. Display All Rooms")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = int(input("Enter room number: "))
            if hotel.is_room_available(room_number):
                print("Room is available.")
            else:
                print("Room not found or already occupied.")
        elif choice == '2':
            room_number = int(input("Enter room number: "))
            result = hotel.book_room(room_number)
            print(result)
        elif choice == '3':
            hotel.display_rooms()
        elif choice == '4':
            print("Exiting the program.")
            break
