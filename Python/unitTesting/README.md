# Hotel Room Booking Application

The Hotel Room Booking Application is a simple Python program that allows users to check the availability of rooms in a hotel, book available rooms, and display information about each room, including its type and price.

## Features

- **Check Room Availability:** Users can check whether a specific room is available for booking.
- **Book a Room:** Users can book an available room, and the program will mark it as occupied.
- **Display All Rooms:** Users can view a list of all available rooms, including their types, prices, and availability.
- **Exit:** Users can exit the program.

## How to Use

1. Run the `hotel_booking.py` file to start the application.
2. Follow the on-screen menu options to interact with the program.

## Room Types and Prices

The application supports three types of rooms, each with different prices:

- **Single:** $100 per night
- **Double:** $150 per night
- **Suite:** $200 per night

## Tests

This application includes unit tests to ensure its functionality. The following tests have been implemented:

### Test 1: `test_add_room`

This test checks if the `add_room` method in the `Hotel` class correctly adds a room to the list of available rooms.

### Test 2: `test_is_room_available`

This test checks if the `is_room_available` method correctly determines the availability of a room.

### Test 3: `test_book_room_unoccupied`

This test checks if the `book_room` method correctly books an unoccupied room and returns the expected message.

### Test 4: `test_book_room_occupied`

This test checks if the `book_room` method correctly handles booking an already occupied room and returns the expected message.

### Test 5: `test_display_rooms`

This test checks if the `display_rooms` method in the `Hotel` class correctly displays room information.

## Running the Tests

You can run the tests using the following command:

```bash
python -m unittest hotel_test.py

License
This project is licensed under the MIT License - see the LICENSE file for details.