def calculate_checksum(ascii_values):
    ascii_sum = sum(ascii_values)
    
    print(f"\nTotal ASCII Sum: {ascii_sum} (Binary: {format(ascii_sum, '08b')})")

    while ascii_sum > 0xFF:
        overflow = ascii_sum >> 8 
        ascii_sum = (ascii_sum & 0xFF) + overflow

    print(f"Wrap-around (8 bits): {ascii_sum} (Binary: {format(ascii_sum, '08b')})")
    checksum = ~ascii_sum & 0xFF
    print(f"Checksum (decimal): {checksum}\n")

    return checksum

def sender(data):
    print("\nSender:")
    print("Character\tASCII Value")
    ascii_values = [ord(char) for char in data]
    
    for char, ascii_value in zip(data, ascii_values):
        print(f"{char}\t\t{ascii_value}")
    
    checksum = calculate_checksum(ascii_values)
    return ascii_values, checksum

def receiver(ascii_values, checksum):
    packet = ascii_values
    packet.append(checksum)

    print("\nReceiver:")
    print("Character\tASCII Value")
    for i in range(len(ascii_values)-1):
        char = chr(ascii_values[i])
        print(f"{char}\t\t{ascii_values[i]}")
        
    receiver_checksum = calculate_checksum(packet)

    if receiver_checksum == 0:
        print("Data received correctly! No errors found.")
    else:
        print(f"Error detected! Checksum mismatch. Final complemented checksum: {receiver_checksum:#04x}")

if __name__ == "__main__":
    message = input("Enter the message to be sent: ")
    ascii_values, checksum = sender(message)
    receiver(ascii_values, checksum)
