attempts = 0

while True:
    response = input("Do you want to quit? (y/n): ")
    attempts += 1
    if response == "y":
        break
print("Exiting after", attempts,"attempts")