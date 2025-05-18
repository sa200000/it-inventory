import csv

def add_device():
    device_id = input("Enter Device ID (e.g., Laptop-101): ")
    user = input("Enter User Email: ")
    os = input("Enter OS (e.g., Windows 11): ")
    
    # Add the device to the CSV
    with open('inventory.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([device_id, user, os, "Active"])
    print("Device added!")

def search_device():
    device_id = input("Enter Device ID to search: ")
    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == device_id:
                print(f"Found: {row}")
                return
    print("Device not found.")

# Main menu
while True:
    print("\nIT Inventory System")
    print("1. Add Device")
    print("2. Search Device")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")
    
    if choice == '1':
        add_device()
    elif choice == '2':
        search_device()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")