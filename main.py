def create_theater():
    rows = "ABCDEFGHIJ"
    # Initialize each row with 10 seats, all available (True).
    seats = {row: [True] * 10 for row in rows}
    # Define the price for each row.
    prices = {
        'A': 100, 'B': 100,
        'C': 90, 'D': 90,
        'E': 80, 'F': 80,
        'G': 70, 'H': 70,
        'I': 60, 'J': 60
    }
    return seats, prices

def available(seats, row_col):
    row = row_col[0]
    col = int(row_col[1:]) - 1  # Convert to 0-based index
    if row in seats and 0 <= col < 10:
        return seats[row][col]
    return False

def purchase(seats, prices, row_col):
    row = row_col[0]
    col = int(row_col[1:]) - 1  # Convert to 0-based index
    if row in seats and 0 <= col < 10:
        if seats[row][col]:
            seats[row][col] = False  # Mark seat as occupied
            return prices[row]
        else:
            return -1 
    return -1  # Invalid seat

def number_of_available_seats(seats):
    return sum(seat for row in seats.values() for seat in row)

def print_seat_layout(seats):
    for row, seat_list in seats.items():
        row_display = ''.join('O' if seat else 'X' for seat in seat_list)
        print(f"{row}: {row_display}")

def reset_seat_layout(seats):
    rows = "ABCDEFGHIJ"
    for row in rows:
        seats[row] = [True] * 10  # Reset all seats to available

# Example usage
def main():
    # Create the theater setup
    seats, prices = create_theater()
    
    while True:
        print("\n1. Check seat availability")
        print("2. Purchase a ticket")
        print("3. Number of available seats")
        print("4. Print seat layout")
        print("5. Reset seat layout")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            seat = input("Enter seat (e.g., B4): ").strip()
            print("Available" if available(seats, seat) else "Not Available")
        
        elif choice == '2':
            seat = input("Enter seat (e.g., B4): ").strip()
            price = purchase(seats, prices, seat)
            if price == -1:
                print("Seat is already occupied or invalid.")
            else:
                print(f"Ticket purchased for {price}")
        
        elif choice == '3':
            print(f"Number of available seats: {number_of_available_seats(seats)}")
        
        elif choice == '4':
            print("Current seat layout:")
            print_seat_layout(seats)
        
        elif choice == '5':
            reset_seat_layout(seats)
            print("Seat layout has been reset.")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
