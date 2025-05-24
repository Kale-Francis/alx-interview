# 0x04. UTF-8 Validation

## Project Overview

This project delves into the fascinating world of character encoding, specifically focusing on **UTF-8**. The primary goal is to write a Python method that can determine if a given list of integers, representing raw bytes, constitutes a valid UTF-8 encoded sequence. This task requires a deep understanding of bitwise operations and the precise rules that govern how characters are encoded in UTF-8.

This project is crucial for understanding low-level data representation and validation, which are fundamental concepts in computer science and software development.

## Concepts Explored

To successfully complete this project, the following key concepts were essential:

* **UTF-8 Encoding Scheme:**
    * **Variable-width encoding:** UTF-8 characters can be 1 to 4 bytes long.
    * **Leading Byte Patterns:** How the first byte of a multi-byte sequence indicates its length.
        * `0xxxxxxx`: 1-byte character (ASCII).
        * `110xxxxx`: Start of a 2-byte character.
        * `1110xxxx`: Start of a 3-byte character.
        * `11110xxx`: Start of a 4-byte character.
    * **Continuation Byte Pattern:** All subsequent bytes in a multi-byte sequence must start with `10xxxxxx`.
    * **Invalid Patterns:** Any byte not fitting these rules, or an incomplete sequence, indicates invalid UTF-8.

* **Bitwise Operations in Python:**
    * Crucial for inspecting and manipulating the individual bits of each integer (byte).
    * **Bitwise AND (`&`):** Used extensively with "masks" to check if specific leading bits match the required UTF-8 patterns (e.g., `byte & 0b10000000` to check the most significant bit).
    * **Bitwise Right Shift (`>>`):** Used to conveniently check leading bit patterns by shifting bits to the right and comparing against binary literals (e.g., `byte >> 7` checks the 8th bit).
    * **Masking (`byte & 0xFF`):** Ensures that only the 8 least significant bits of an integer are considered, discarding any higher bits that might be set (important as input integers could exceed 255 if not masked).

* **Data Representation:** Understanding that each integer in the input list directly corresponds to an 8-bit byte, and how to effectively work with this byte-level data in Python.

* **List Manipulation:** Iterating through the input list (`data`) byte by byte and understanding how to maintain state (`num_bytes_to_check`) across iterations.

* **Boolean Logic:** Applying conditional statements (`if`, `elif`, `else`) to implement the validation rules based on the bit patterns, and ultimately returning `True` or `False`.

## Project Structure

The project directory `0x04-utf8_validation` contains the following files:

* **`0-validate_utf8.py`**: This is the main solution file containing the `validUTF8` function.
* **`0-main.py`**: (Likely provided by the project's auto-checker) A test script to verify the correctness of the `validUTF8` function with various test cases.
* **`README.md`**: This file, providing an overview and documentation for the project.

## How to Run (Testing)

To test your `0-validate_utf8.py` solution:

1.  **Navigate to your project directory:**
    ```bash
    cd alx-backend-javascript/0x04-utf8_validation
    ```
2.  **Ensure your script is executable:**
    ```bash
    chmod +x 0-validate_utf8.py
    chmod +x 0-main.py
    ```
3.  **Run the main test script:**
    ```bash
    ./0-main.py
    ```

## Example Usage and Expected Output

Running `0-main.py` will produce output similar to the following, demonstrating the function's ability to correctly validate UTF-8 byte sequences:

```bash
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False

