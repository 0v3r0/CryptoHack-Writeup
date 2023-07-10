from pwn import xor

# Get user input for the label
label = input("Enter a label: ")

# Convert label to bytes
label_bytes = label.encode()

# XOR the label bytes with 13
xored_bytes = xor(label_bytes, 13)

# Convert XORed bytes back to string
xored_label = xored_bytes.decode()

# Print the result
print("Original Label:", label)
print("XORed Label:", xored_label)
