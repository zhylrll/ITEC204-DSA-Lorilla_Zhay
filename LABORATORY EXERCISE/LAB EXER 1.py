tickets = [
    {"id": "INC1392939", "bot": "BOT-Inventory", "desc": "Failed to generate the daily report"},
    {"id": "INC1392940", "bot": "BOT-Email", "desc": "Failed to send the scheduled notification"},
    {"id": "INC1392941", "bot": "BOT-DataSync", "desc": "Encountered an error during data transfer"},
    {"id": "INC1392942", "bot": "BOT-Invoice", "desc": "Failed to process an invoice"},
    {"id": "INC1392943", "bot": "BOT-Report", "desc": "Failed to generate the weekly report"},
    {"id": "INC1392944", "bot": "BOT-FileTransfer", "desc": "Failed to upload the required file"},
    {"id": "INC1392945", "bot": "BOT-DataEntry", "desc": "Encountered an error while entering records"},
    {"id": "INC1392946", "bot": "BOT-Backup", "desc": "Failed to complete the scheduled backup"},
    {"id": "INC1392947", "bot": "BOT-Validation", "desc": "Failed to validate the submitted records"},
    {"id": "INC1392948", "bot": "BOT-Notification", "desc": "Failed to send the system alert"}
]

while True:
    print("\n===== IT AUTOMATION INCIDENT TICKET MANAGER =====")
    print("1. Add Ticket")
    print("2. Display Tickets")
    print("3. Search Ticket")
    print("4. Remove Ticket")
    print("5. Count Tickets")
    print("6. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        i = input("Incident ID: ").strip()
        b = input("Bot: ").strip()
        d = input("Short Description: ").strip()

        if i == "" or b == "" or d == "":
            print("All fields are required.")
        else:
            exists = False
            for t in tickets:
                if t["id"].upper() == i.upper():
                    exists = True
                    break

            if exists:
                print("Ticket already exists.")
            else:
                tickets.append({"id": i, "bot": b, "desc": d})
                print("Ticket added!")

    elif choice == "2":
        if len(tickets) == 0:
            print("No active tickets.")
        else:
            print(f"\n{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
            print("-" * 75)
            for t in tickets:
                print(f"{t['id']:<15}{t['bot']:<20}{t['desc']}")

    elif choice == "3":
        i = input("Enter Incident ID: ").strip()
        found = False
        for t in tickets:
            if t["id"].upper() == i.upper():
                print("\nTicket found:")
                print("Incident ID       :", t["id"])
                print("Bot               :", t["bot"])
                print("Short Description :", t["desc"])
                found = True
                break
        if not found:
            print("Ticket not found.")

    elif choice == "4":
        i = input("Enter Incident ID to remove: ").strip()
        removed = False
        for t in tickets:
            if t["id"].upper() == i.upper():
                tickets.remove(t)
                print("Ticket removed!")
                removed = True
                break
        if not removed:
            print("Ticket not found.")

    elif choice == "5":
        print("Total active tickets:", len(tickets))

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")