#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """determine if a given data set represents a valid UTF-8 encoding."""
    num_bytes_to_check = 0
    # This variable will keep track of how many continuation bytes we expect to see after a multi-byte leading character.
    for byte in data:
        # Check if the current byte is a continuation byte (10xxxxxx)
        byte = byte & 0xFF  # Mask the byte to ensure we are only working with the last 8 bits
        if num_bytes_to_check == 0:
            # This is the state where you expect to find the start of a new UTF-8 character.
            if (byte >> 7) == 0:
                pass
            elif (byte >> 5) == 0b110:
                num_bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
            
        elif num_bytes_to_check > 0:
            # This is the state where you expect to find a continuation byte.
            if (byte >> 6) != 0b10:
                num_bytes_to_check -= 1
            else: 
                return False
        # If we have processed all expected continuation bytes, return false. 
    return num_bytes_to_check == 0
