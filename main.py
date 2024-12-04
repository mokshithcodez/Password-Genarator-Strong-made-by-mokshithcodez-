import random
import string
import pyttsx3

engine = pyttsx3.init()

alphabet_characters = list(string.ascii_uppercase) + list(string.ascii_lowercase)
even_numbers = [str(num) for num in range(0, 101, 2)] 
combined_list = alphabet_characters + even_numbers

def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Welcome to the Password Generator!")
print("Welcome to the Password Generator!")

speak("Select the number of digits for your password.")
user_input = int(input("Number of Digits: "))

password = "".join(random.sample(combined_list, user_input))  
speak(f"Your password is ready. Here it is: {password}")
print("Generated Password:", password)
