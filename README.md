# Enigma Machine

The Enigma machine is an encryption device used during World War II for secure communication. This Python implementation simulates a simplified version of the Enigma machine.

## Features

- Supports three rotors with configurable wiring and notch positions.
- Includes a reflector for bi-directional encryption.
- Allows setting the initial positions of the rotors.
- Handles encryption of alphanumeric characters while preserving non-alphabetic characters in the message.

## Usage

1. Clone the repository or download the `main.py` file.

2. Make sure you have Python 3 installed on your system.

3. Open a terminal or command prompt and navigate to the directory where `main.py` is located.

4. Run the script by executing the following command:

```
python main.py
```


5. Follow the prompts:
- Enter the message you want to encrypt.
- The script will encrypt the message using the Enigma machine and display the encrypted message.

## Customization

You can customize the Enigma machine by modifying the rotor wirings and notch positions in the `main` function of the `main.py` file. The current implementation includes sample rotor wirings and notches.

Feel free to experiment with different rotor configurations to enhance the encryption strength or simulate the historical Enigma machine settings.

## Note

This implementation is a simplified version of the Enigma machine and does not include certain advanced features and encryption complexities found in the original Enigma machines.

## Resources

- [Wikipedia: Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
