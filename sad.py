
import tkinter as tk
from tkinter import messagebox
import uuid

class Flight:
    def __init__(self, destination, price, available_seats):
        self.destination = destination
        self.price = price
        self.available_seats = available_seats

class Booking:
    def __init__(self, flight, name, passport_number):
        self.booking_id = str(uuid.uuid4())
        self.flight = flight
        self.name = name
        self.passport_number = passport_number

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking System")
        
        self.flights = [
            Flight("Mexico City", 300, 5),
            Flight("Cancun", 400, 3),
            Flight("Guadalajara", 350, 4)
        ]
        
        self.create_main_menu()

    def create_main_menu(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)

        view_btn = tk.Button(main_frame, text="View Available Flights", command=self.view_flights)
        view_btn.pack(side=tk.LEFT, padx=10)

        book_btn = tk.Button(main_frame, text="Book a Ticket", command=self.book_ticket)
        book_btn.pack(side=tk.LEFT, padx=10)

        exit_btn = tk.Button(main_frame, text="Exit", command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=10)

    def view_flights(self):
        flights_window = tk.Toplevel(self.root)
        flights_window.title("Available Flights")
        
        for idx, flight in enumerate(self.flights, start=1):
            info = f"Destination: {flight.destination}, Price: ${flight.price}, Available Seats: {flight.available_seats}"
            lbl = tk.Label(flights_window, text=info)
            lbl.pack()

    def book_ticket(self):
        book_window = tk.Toplevel(self.root)
        book_window.title("Book a Ticket")
        
        tk.Label(book_window, text="Flight Number:").grid(row=0, column=0)
        tk.Label(book_window, text="Name:").grid(row=1, column=0)
        tk.Label(book_window, text="Passport Number:").grid(row=2, column=0)
        
        self.flight_num_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.passport_var = tk.StringVar()

        tk.Entry(book_window, textvariable=self.flight_num_var).grid(row=0, column=1)
        tk.Entry(book_window, textvariable=self.name_var).grid(row=1, column=1)
        tk.Entry(book_window, textvariable=self.passport_var).grid(row=2, column=1)
        
        tk.Button(book_window, text="Book", command=self.confirm_booking).grid(row=3, column=0, columnspan=2, pady=10)

    def confirm_booking(self):
        try:
            choice = int(self.flight_num_var.get())
            name = self.name_var.get()
            passport_number = self.passport_var.get()

            if 1 <= choice <= len(self.flights):
                selected_flight = self.flights[choice - 1]
                if selected_flight.available_seats > 0:
                    booking = Booking(selected_flight, name, passport_number)
                    selected_flight.available_seats -= 1
                    messagebox.showinfo("Booking Confirmed", f"Booking confirmed! Your booking ID is {booking.booking_id}.")
                else:
                    messagebox.showerror("Error", "Sorry, no seats available on this flight.")
            else:
                messagebox.showerror("Error", "Invalid flight selection.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingApp(root)
    root.mainloop()