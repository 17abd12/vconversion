import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Convert text to speech
text = "Hello, how are you?"
engine.say(text)

# Play the speech
engine.runAndWait()