total_classes = 0
attended_classes = 0

def mark_attendance():
    global total_classes, attended_classes

    print("\n1. Present")
    print("2. Absent")

    choice = input("Enter choice: ")

    total_classes += 1

    if choice == '1':
        attended_classes += 1
        print("Marked Present ✅")
    elif choice == '2':
        print("Marked Absent ❌")
    else:
        print("Invalid choice!")

def show_attendance():
    if total_classes == 0:
        print("No classes recorded yet.")
        return

    percentage = (attended_classes / total_classes) * 100

    print(f"\nTotal Classes: {total_classes}")
    print(f"Attended Classes: {attended_classes}")
    print(f"Attendance: {percentage:.2f}%")

    if percentage < 75:
        print("⚠️ Low Attendance!")
    else:
        print("✅ Good Attendance")

while True:
    print("\n==== MENU ====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    option = input("Choose option: ")

    if option == '1':
        mark_attendance()
    elif option == '2':
        show_attendance()
    elif option == '3':
        print("Exiting...")
        break
    else:
        print("Invalid option!")
