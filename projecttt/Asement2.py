class Requisition:

    next_id = 10001
    all_requisitions = []
    total_submitted = 0
    total_approved = 0
    total_pending = 0
    total_not_approved = 0

    def __init__(self, date, staff_id, staff_name):

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1

        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

        Requisition.all_requisitions.append(self)
        Requisition.total_submitted += 1
        Requisition.total_pending += 1

    # Collects info from the user
    @classmethod
    def add_requisition(cls):

        print("Requisition for Business!!")
        print("\nEnter your information:")

        date = input("Date: ")
        staff_id = input("Staff ID: ")
        staff_name = input("Staff Name: ")

        # Create a requisition object
        r = cls(date, staff_id, staff_name)

        print("Requisition ID:", r.requisition_id)

        items = []

        print("\nAdd items:")

        another = "yes"

        while another == "yes":

            item_name = input("Item Name: ")
            price_text = input("Item Price $  : ")

            while price_text.replace(".", "", 1).isdigit() == False:
                print("Please enter a number, e.g. 12.50")
                price_text = input("Item Price $  : ")

            item_price = float(price_text)

            items.append((item_name, item_price))

            another = input("Add another item yes/no: ").lower()

        # Calculate total
        r.requisitions_details(items)

        print("Total: $" + str(r.total))

        # Auto check approval
        r.approve_requisition()

        print("Status:", r.status)

        print("Approval Reference Number:", r.approval_ref)

    # Calculate requisition total
    def requisitions_details(self, items):

        total = 0

        for item_name, cost in items:
            total += cost

        self.total = total

        return total

    # Auto approval
    def approve_requisition(self):

        if self.total <= 500:

            self.status = "Approved"

            self.approval_ref = self.staff_id + str(self.requisition_id)[-3:]

            Requisition.total_pending -= 1
            Requisition.total_approved += 1

    # Manager response
    def respond_to_requisition(self, decision):

        if self.status != "Pending":
            print("Requisition", self.requisition_id, "is not pending.")
            return

        if decision == "Approved":

            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.requisition_id)[-3:]

            Requisition.total_approved += 1
            Requisition.total_pending -= 1

        elif decision == "Not approved":

            self.status = "Not approved"

            Requisition.total_not_approved += 1
            Requisition.total_pending -= 1

    # Display all requisitions
    @classmethod
    def display_requisitions(cls):

        print("\nPrinting requisitions:")

        for r in cls.all_requisitions:

            print("\nDate:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + str(r.total))
            print("Status:", r.status)
            print("Approval Reference Number:", r.approval_ref)

    # Display stats
    @classmethod
    def requisition_statistics(cls):

        print("\nDisplaying the Requisition Statistics")
        print("The total number of requisitions submitted:", cls.total_submitted)
        print("The total number of approved requisitions:", cls.total_approved)
        print("The total number of pending requisitions:", cls.total_pending)
        print("The total number of not approved requisitions:", cls.total_not_approved)


# MAIN

print("Welcome to the Requisition System")

another = "yes"

while another == "yes":

    Requisition.add_requisition()

    another = input("\nWould you like to submit another requisition? yes/no: ").lower()

# The manager decisions
for r in Requisition.all_requisitions:

    if r.status == "Pending":

        print("\nRequisition ID:", r.requisition_id)
        print("Staff Name:", r.staff_name)
        print("Total: $", r.total)

        decision = input("Manager decision (Approved/Not approved/Leave): ")

        if decision == "Approved" or decision == "Not approved":
            r.respond_to_requisition(decision)

# Final output
Requisition.display_requisitions()
Requisition.requisition_statistics()