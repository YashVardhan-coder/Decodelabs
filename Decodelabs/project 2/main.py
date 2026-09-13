import sys

def encrypt(text: str, shift: int) -> str:
    result = []
    shift = shift % 26
    for char in text:
        if char.isupper():
            base = ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        elif char.islower():
            base = ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

def decrypt(ciphertext: str, shift: int) -> str:
    return encrypt(ciphertext, -shift)

def brute_force_decrypt(ciphertext: str) -> list[tuple[int, str]]:
    attempts = []
    for key in range(1, 26):
        decrypted_text = decrypt(ciphertext, key)
        attempts.append((key, decrypted_text))
    return attempts

def get_integer_input(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_banner() -> None:
    print("=" * 60)
    print("      DECODELABS CYBER SECURITY - PROJECT 2")
    print("           Basic Encryption & Decryption")
    print("=" * 60)

def display_menu() -> None:
    print("\nPlease select an option:")
    print("  [1] Encrypt Plaintext")
    print("  [2] Decrypt Ciphertext")
    print("  [3] Complete IPO Cycle (Encrypt & Decrypt Verification)")
    print("  [4] Security Vulnerability Demo (Brute Force Key Space)")
    print("  [5] Exit")

def run_encrypt_option() -> None:
    plaintext = input("\nEnter plaintext to encrypt: ")
    shift = get_integer_input("Enter shift key (integer): ")
    ciphertext = encrypt(plaintext, shift)
    print("\n--- Encryption Result ---")
    print(f"Plaintext:   {plaintext}")
    print(f"Shift Key:   {shift}")
    print(f"Ciphertext:  {ciphertext}")

def run_decrypt_option() -> None:
    ciphertext = input("\nEnter ciphertext to decrypt: ")
    shift = get_integer_input("Enter shift key (integer): ")
    plaintext = decrypt(ciphertext, shift)
    print("\n--- Decryption Result ---")
    print(f"Ciphertext:  {ciphertext}")
    print(f"Shift Key:   {shift}")
    print(f"Plaintext:   {plaintext}")

def run_ipo_option() -> None:
    plaintext = input("\nEnter original raw text (Input): ")
    shift = get_integer_input("Enter secret shift key (Process): ")
    ciphertext = encrypt(plaintext, shift)
    decrypted_text = decrypt(ciphertext, shift)
    print("\n" + "-" * 40)
    print("      IPO MODEL DEMONSTRATION")
    print("-" * 40)
    print(f"[INPUT]      Plaintext:       {plaintext}")
    print(f"[PROCESS]    Shift Applied:   {shift}")
    print(f"[OUTPUT]     Ciphertext:      {ciphertext}")
    print(f"[VALIDATION] Decrypted Text:  {decrypted_text}")
    print("-" * 40)
    if plaintext == decrypted_text:
        print("Status: Verified! Data confidentiality restored successfully.")
    else:
        print("Status: Discrepancy detected during decryption.")

def run_brute_force_option() -> None:
    ciphertext = input("\nEnter ciphertext to brute force: ")
    print(f"\nAnalyzing 25-key space for ciphertext: '{ciphertext}'")
    print("-" * 60)
    print(f"{'Key':<6} | {'Decrypted Output'}")
    print("-" * 60)
    results = brute_force_decrypt(ciphertext)
    for key, text in results:
        print(f"{key:<6} | {text}")
    print("-" * 60)

def main() -> None:
    print_banner()
    try:
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            if choice == "1":
                run_encrypt_option()
            elif choice == "2":
                run_decrypt_option()
            elif choice == "3":
                run_ipo_option()
            elif choice == "4":
                run_brute_force_option()
            elif choice == "5":
                print("\nExiting program. Stay secure!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please select a number between 1 and 5.")
    except (KeyboardInterrupt, EOFError):
        print("\nSession terminated. Stay secure!")
        sys.exit(0)

if __name__ == "__main__":
    main()
