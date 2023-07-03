import string

class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 0  # Initialize rotor position

    def forward(self, char):
        index = (ord(char) - ord('A') + self.position) % 26
        encrypted_char = self.wiring[index]
        return chr((ord(encrypted_char) - ord('A') - self.position) % 26 + ord('A'))

    def backward(self, char):
        index = (ord(char) - ord('A') + self.position) % 26
        encrypted_char = self.wiring.index(chr(index + ord('A')))
        return chr((encrypted_char - self.position) % 26 + ord('A'))

    def rotate(self):
        self.position = (self.position + 1) % 26
        if self.position == ord(self.notch) - ord('A'):
            return True
        return False

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def set_rotor_positions(self, positions):
        for i, rotor in enumerate(self.rotors):
            rotor.position = ord(positions[i]) - ord('A')

    def encrypt_message(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                encrypted_char = self.encrypt_char(char.upper())
            else:
                encrypted_char = char
            encrypted_message += encrypted_char
        return encrypted_message

    def encrypt_char(self, char):
        for rotor in self.rotors:
            rotate_next = rotor.rotate()
            if not rotate_next:
                break

        encrypted_char = char
        for rotor in self.rotors[::-1]:
            encrypted_char = rotor.forward(encrypted_char)

        encrypted_char = self.reflector.forward(encrypted_char)

        for rotor in self.rotors:
            encrypted_char = rotor.backward(encrypted_char)

        return encrypted_char

def main():
    # Sample rotor wirings and notches
    rotor1_wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    rotor2_wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    rotor3_wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    reflector_wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    # Create rotor objects
    rotor1 = Rotor(rotor1_wiring, notch='Q')
    rotor2 = Rotor(rotor2_wiring, notch='E')
    rotor3 = Rotor(rotor3_wiring, notch='V')

    # Create reflector object
    reflector = Rotor(reflector_wiring, notch=None)

    # Create the Enigma machine
    enigma = EnigmaMachine(rotors=[rotor1, rotor2, rotor3], reflector=reflector)

    # Set initial rotor positions (e.g., 'AAA')
    enigma.set_rotor_positions('AAA')

    # Prompt the user to enter the message to encrypt
    message = input("Enter the message to encrypt: ")

    # Encrypt the message using the Enigma machine
    encrypted_message = enigma.encrypt_message(message)

    # Print the encrypted message
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
