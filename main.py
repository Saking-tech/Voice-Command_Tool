# Importing the required API classes
from SpeechAssistant import SpeechAssistant
from WebInteraction import WebInteraction
from EmailAssistant import EmailAssistant
from MediaHandler import MediaHandler
from SystemUtilities import SystemUtilities
from GuiHandler import GUIHandler
from ExternalServices import ExternalServices


def main():
    # Initialize all API objects
    speech_assistant = SpeechAssistant()
    web_interaction = WebInteraction()
    email_assistant = EmailAssistant()
    media_handler = MediaHandler()
    system_utilities = SystemUtilities()
    # If you want to run the GUI separately, skip initializing here
    gui_handler = GUIHandler()
    external_services = ExternalServices()

    # Greet the user
    speech_assistant.speak("Hello, how can I assist you today?")

    while True:
        # Listen for the user's command
        command = speech_assistant.listen().lower()

        if "google" in command:
            query = command.replace("google", "").strip()
            speech_assistant.speak(f"Searching Google for {query}")
            web_interaction.search_google(query)

        elif "open website" in command:
            website = command.replace("open website", "").strip()
            speech_assistant.speak(f"Opening website {website}")
            web_interaction.open_website(website)

        elif "youtube" in command:
            video_name = command.replace("youtube", "").strip()
            speech_assistant.speak(f"Playing {video_name} on YouTube")
            web_interaction.play_youtube_video(video_name)

        elif "send email" in command:
            speech_assistant.speak("Who is the recipient?")
            recipient_name = speech_assistant.listen().lower().strip()
            recipient_email = email_assistant.get_contact_email(recipient_name)
            if recipient_email:
                speech_assistant.speak("What should be the subject?")
                subject = speech_assistant.listen().strip()
                speech_assistant.speak("What is the message?")
                body = speech_assistant.listen().strip()
                email_assistant.send_email(
                    to_address=recipient_email, subject=subject, body=body)
                speech_assistant.speak(f"Email sent to {recipient_name}")
            else:
                speech_assistant.speak("I don't have this contact saved.")

        elif "record video" in command:
            speech_assistant.speak("Recording video. Press 'q' to stop.")
            media_handler.record_video()
            speech_assistant.speak("Video recording stopped and saved.")

        elif "take screenshot" in command:
            filename = "screenshot.png"
            media_handler.capture_screenshot(filename=filename)
            speech_assistant.speak(f"Screenshot saved as {filename}.")

        elif "time" in command:
            current_time = system_utilities.get_current_time()
            speech_assistant.speak(f"The current time is {current_time}.")

        elif "random number" in command:
            number = system_utilities.create_random_number(1, 100)
            speech_assistant.speak(f"Your random number is {number}.")

        elif "list directory" in command:
            speech_assistant.speak("Which directory should I list?")
            path = speech_assistant.listen().strip()
            contents = system_utilities.list_directory_contents(path)
            speech_assistant.speak(f"The contents of {path} are {contents}")

        elif "weather" in command:
            speech_assistant.speak(
                "Which city's weather would you like to know?")
            city = speech_assistant.listen().strip()
            weather_report = external_services.get_weather(city)
            if weather_report:
                speech_assistant.speak(weather_report)

        elif "open gui" in command or "start gui" in command:
            speech_assistant.speak("Opening the graphical user interface.")
            gui_handler = GUIHandler()  # Initialize GUI handler
            gui_handler.run()  # Run the GUI


# Modify the 'quit' command handling to also close the GUI if it's open
        elif "quit" in command or "exit" in command:
            speech_assistant.speak("Goodbye!")
            try:
                gui_handler.root.destroy()  # Close the GUI window if it's open
            except:
                pass  # GUI was not initialized or already closed
            break
        
        else:
            speech_assistant.speak(
            "I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
