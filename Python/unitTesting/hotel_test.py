import unittest
from hotel_booking import Room, Hotel

class TestHotelBooking(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()
        self.single_room = Room(1, "Single", 100)
        self.double_room = Room(2, "Double", 150)
        self.suite_room = Room(3, "Suite", 200)
        self.hotel.add_room(self.single_room)
        self.hotel.add_room(self.double_room)
        self.hotel.add_room(self.suite_room)

    def test_is_room_available(self):
        self.assertTrue(self.hotel.is_room_available(1))
        self.assertTrue(self.hotel.is_room_available(2))
        self.assertTrue(self.hotel.is_room_available(3))
        self.assertFalse(self.hotel.is_room_available(4))

    def test_book_room(self):
        self.assertEqual(self.hotel.book_room(1), "Room 1 has been booked. Enjoy your stay!")
        self.assertEqual(self.hotel.book_room(2), "Room 2 has been booked. Enjoy your stay!")
        self.assertEqual(self.hotel.book_room(3), "Room 3 has been booked. Enjoy your stay!")
        self.assertEqual(self.hotel.book_room(4), "Room not found.")

    def test_display_rooms(self):
        expected_output = [
            "Room 1 (Single): $100 - Available",
            "Room 2 (Double): $150 - Available",
            "Room 3 (Suite): $200 - Available",
        ]
        self.assertEqual(self.hotel.display_rooms(), expected_output)

if __name__ == "__main__":
    unittest.main()
