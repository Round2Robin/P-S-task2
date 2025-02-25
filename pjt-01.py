import datetime as dt

# Function to calculate fare based on traveler categories and zones traveled
def calculate_fare(adults, children, seniors, students, zones_traveled):
    # Define fare rates per category per zone (in cents)
    adult_fare_per_zone = 2105  # Fare per adult per zone
    child_fare_per_zone = 1410  # Fare per child per zone
    senior_fare_per_zone = 1025  # Fare per senior per zone
    student_fare_per_zone = 1750  # Fare per student per zone
    
    # Calculate total fare for each category based on zones traveled
    total_adult_fare = adults * adult_fare_per_zone * zones_traveled
    total_child_fare = children * child_fare_per_zone * zones_traveled
    total_senior_fare = seniors * senior_fare_per_zone * zones_traveled
    total_student_fare = students * student_fare_per_zone * zones_traveled
    
    # Calculate total fare and total travelers
    total_fare = total_adult_fare + total_child_fare + total_senior_fare + total_student_fare
    total_travelers = adults + children + seniors + students
    
    return total_adult_fare, total_child_fare, total_senior_fare, total_student_fare, total_fare, total_travelers

# Function to get valid integer input within a range
def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to generate travel vouchers
def generate_voucher():
    while True:

        print("---      Travel Voucher System    ---")
        print("---         Available Zones      ---")
        print("\nZone 1: Downtown -   Stations:   Erean, Brunad, Zord, Perinad, Keivia, Elyot, Adohad, Marend, Ryall, Ederif, Holmer")
        print("Zone 2: Midtown  -   Stations:   Riclya, Quthiel,Wicyt, Riladia, Oloadus, Sylas, Agralle, Docia, Stonyam, Obelyn, Ralith, Garion")
        print("Zone 3: Central  -   Stations:   Centrala, Yaen, Bylyn, Rede, Frestin, Jaund, Ninia, Tallan, Lomil, Soth, Pryn, Ruril, Vertwall\n")
        
        # Get boarding and destination zones
        boarding_zone = get_valid_input("Enter boarding zone number (1-3): ", 1, 3)
        destination_zone = get_valid_input("Enter destination zone number (1-3): ", 1, 3)
        
        # Calculate zones traveled (absolute difference between zones) ALSO ensuring at least one zone is traveled (minimum fare applies)
        zones_traveled = max(abs(boarding_zone - destination_zone),1)
        
        # Map zone numbers to names
        zone_names = {1: "Downtown", 2: "Midtown", 3: "Central"}
        boarding_zone_name = zone_names[boarding_zone]
        destination_zone_name = zone_names[destination_zone]
        
        # Get number of travelers in each category
        adults = get_valid_input("\nEnter number of Adults: ", 0, 100)
        children = get_valid_input("Enter number of Children: ", 0, 100)
        seniors = get_valid_input("Enter number of Seniors: ", 0, 100)
        students = get_valid_input("Enter number of Students: ", 0, 100)
        
        # Calculate fares based on zones traveled
        total_adult_fare, total_child_fare, total_senior_fare, total_student_fare, total_fare, total_travelers = calculate_fare(adults, children, seniors, students, zones_traveled)
        
        # Get current date and time
        current_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the travel voucher

        print("\n=== Travel Voucher ===")
        print(f"\n{'Date & Time:':<20} {current_datetime}")
        print(f"{'Boarding Zone:':<20} {boarding_zone_name}")
        print(f"{'Destination Zone:':<20} {destination_zone_name}")
        print(f"\n{'Zones Travelled:':<20} {zones_traveled}")
        print(f"{'Adults:':<20} {adults:<5} (Fare: {total_adult_fare:<7} cents)")
        print(f"{'Children:':<20} {children:<5} (Fare: {total_child_fare:<7} cents)")
        print(f"{'Seniors:':<20} {seniors:<5} (Fare: {total_senior_fare:<7} cents)")
        print(f"{'Students:':<20} {students:<5} (Fare: {total_student_fare:<7} cents)")

        print(f"{'Total Travellers:':<20} {total_travelers:<5} cents")
        print(f"{'Total Fare:':<20} {total_fare:<5} cents")
        print("====================\n")
      
        # Ask if the user wants to generate another voucher
        another_voucher = input("Do you want to generate another voucher? (yes/no): ").strip().lower()
        if another_voucher != 'yes':
            print("Thank you for using the Centrala Underground System. Save Travels!")
            break

# Run the program
if __name__ == "__main__":
    generate_voucher()