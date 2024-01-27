def speeding_ticket(speed, is_birthday):
    speed_offset = 5 if is_birthday else 0

 
    if speed <= 60 + speed_offset:
        return "no tickets"
    elif 61 <= speed <= 80 + speed_offset:
        return "small tickets"
    else:
        return "big tickets"

print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, True))   # Expected output: "No Ticket", because of the birthday allowance
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"

