# Chiffre ADFGVX - Phase de substitution

This Python script implements the substitution phase of the ADFGVX cipher. It includes functions to generate a substitution key, display the key in a grid, create a substitution dictionary, and encrypt a message using the ADFGVX cipher.

## Prerequisites

Before using this code, make sure you have the following:

- Python installed on your system.

## Functions

### `generer_cle_substitution()`

This function generates a substitution key consisting of 36 randomly shuffled characters, including uppercase letters (A-Z) and digits (0-9).

### `afficher_cle_substitution(cle)`

This function takes a substitution key as input and displays it in a 6x6 grid format representing the ADFGVX cipher grid.

### `creer_dict_de_substitution(cle)`

This function creates a substitution dictionary that associates each of the 36 characters from the key with its corresponding ADFGVX diagram.

### `substituer_message(dict_subst, message)`

This function encrypts a message by substituting each letter or digit with its ADFGVX diagram based on the provided substitution dictionary. Non-alphanumeric characters are removed from the message.

### `main()`

The main function generates a substitution key, displays the ADFGVX cipher grid, and allows the user to input a message for encryption. It then displays the encrypted message.

## Usage

1. Run the script using Python:

python script_name.py

3. Follow the on-screen instructions to input a message for encryption. The script will display the encrypted message.

## Example

Suppose you have the following substitution key:
['R', 'I', 'C', '8', 'O', 'E', 'S', 'A', '6', 'U', 'L', '9', 'K', 'Y', 'B', 'N', 'F', '3', 'H', '5', 'T', '1', 'Q', 'D', 'G', 'V', 'W', 'Z', '2', '0', 'X', 'J', 'M', 'P', '7', '4']


Using this key, if you input the message "HELLO123" for encryption, you would get the encrypted message:
AF AF GD GD VA AF DD XF XD

## Note

- This code provides the substitution phase of the ADFGVX cipher. For a complete ADFGVX implementation, you would also need the transposition phase.

- Make sure to customize and expand this code as needed for your specific use case.

Feel free to add more details or explanations if required.



