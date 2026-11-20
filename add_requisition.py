

#part 1
def add_requisition():
    total = 0
    total += 1
    requisition_id = 10000 + total   
    return requisition_id   

print("Enter your INFORMATION BELOW;")
date = input("Enter the date;")
staff_id = input("Enter your staff ID;")
staff_name = input("Enter your name;")

requisition_id = add_requisition()
print("Requisition ID:",requisition_id)











#part 2


print("ADD ITEMS")
total2 = 0
item = input("Enter item name: ")
price = int(input("Enter item price: "))
total2 = total2 + price

again = input("Enter another item? (yes/no): ")

while again == "yes":
    item = input("Enter item name: ")
    price = int(input("Enter item price: "))
    total2 = total2 + price
    again = input("Enter another item? (yes/no): ")

print("Your total is $",total2)



apple = ""
if total2 < 500:
    status = "Approved"
    apple = (f"{staff_id}{requisition_id}")
    print("Status: Approved")
    print("Approval Reference Number:", apple)

else:
    status = "Pending"
    print("Status: Pending")












#part 3

def display_requisitions():
    print("Printing requisitions:")
    print("Date:",date )
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total $", total2)
    print("Status:", status)

    if apple != "":
        print("Approval Reference Number:", apple)


display_requisitions()
