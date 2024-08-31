# AI Personal Assistant

## Overview

The **AI Personal Assistant** is a versatile Python-based project that integrates various functionalities into a single cohesive application. This assistant is designed to perform a wide range of tasks based on voice commands, making it a powerful tool for personal automation and productivity. The assistant can handle tasks such as browsing the web, sending emails, recording videos, managing system utilities, and even interacting with a graphical user interface (GUI).

The project is built with modularity in mind, with each core functionality encapsulated in its own API. This design allows for easy extension and customization, making it suitable for a variety of personal or professional use cases.

## Features

### 1. Speech Recognition and Text-to-Speech
- **Speech Recognition**: The assistant uses the `SpeechRecognition` library to listen to and recognize voice commands. This allows for hands-free interaction with the assistant.
  - **Language Support**: The assistant is configured to recognize English (`en-in`), but this can be easily modified to support other languages by changing the language parameter in the `recognize_google` function.
  - **Custom Voice Commands**: You can add custom voice commands by modifying the command parsing section in `main.py`.

- **Text-to-Speech**: The assistant uses the `pyttsx3` library to convert text responses into speech, providing audible feedback to the user.
  - **Voice Customization**: The `pyttsx3` engine allows you to customize the voice (male/female), rate, and volume. These settings can be modified in the `SpeechAssistant` class.

### 2. Web Interaction
- **Google Search**: The assistant can perform Google searches based on user commands. This feature is powered by the `pywhatkit` library, which automates the process of searching Google.
  - **Search Customization**: The assistant can be configured to perform searches on other search engines by modifying the `search_google` method in the `WebInteraction` class.

- **Website Navigation**: Users can instruct the assistant to open specific websites in the default web browser. This is achieved using the `webbrowser` module.
  - **Favorite Websites**: You can add a list of frequently visited websites and allow the assistant to recognize commands like "Open Facebook" by customizing the `open_website` method.

- **YouTube Video Playback**: The assistant can search for and play videos on YouTube using voice commands. This feature is also powered by the `pywhatkit` library.
  - **Video Customization**: You can extend this functionality to play videos from other platforms (e.g., Vimeo) by modifying the `play_youtube_video` method.

### 3. Email and Communication
- **Send Emails**: The assistant can send emails based on voice commands. The `smtplib` library is used to handle email transmission. Users can specify the recipient, subject, and message content through spoken interaction.
  - **Email Templates**: You can create predefined email templates for recurring messages and trigger them with specific voice commands.

- **Contact Management**: The assistant manages a list of contacts, allowing for easy retrieval of email addresses. The `EmailAssistant` class stores these contacts in a dictionary.
  - **Dynamic Contact Loading**: The contact list can be extended to load dynamically from a database or a CSV file for more extensive contact management.

### 4. Media Handling
- **Video Recording**: The assistant can record video from the webcam, with customizable resolution and format settings. This feature is powered by the `opencv-python` (OpenCV) library.
  - **Advanced Recording Options**: You can extend the `record_video` method to include options such as recording time limits, frame rate adjustments, or even live streaming capabilities.

- **Screenshot Capture**: Users can capture screenshots through voice commands, which are then saved as image files using the `pyautogui` library.
  - **Region-Specific Screenshots**: You can modify the `capture_screenshot` method to capture specific regions of the screen by passing coordinates as parameters.

### 5. System Utilities
- **Time Management**: The assistant can provide the current time on request. The `SystemUtilities` class handles this using Python’s `datetime` module.
  - **Alarm and Reminders**: Extend the assistant to set alarms or reminders by adding methods that utilize Python's `time` and `sched` modules.

- **Random Number Generation**: Users can generate random numbers within a specified range. This is useful for tasks requiring randomization, such as picking a winner from a list.
  - **Random Word Generation**: Extend this feature to generate random words or phrases by integrating with external APIs like the Random Word API.

- **Directory Management**: The assistant can list the contents of directories, making file management easier. The `os` module is used for this functionality.
  - **File Operations**: You can extend this to include operations like creating, renaming, or deleting files and directories.

- **System Control**: The assistant can execute system-level commands such as shutdown, restart, and sleep. This is particularly useful for managing your computer without physical interaction.
  - **Custom Commands**: Add more system-level commands like locking the screen, logging off, or even launching specific applications.

### 6. GUI Interaction
- **Graphical Interface**: The assistant includes a `tkinter`-based GUI that can be opened via voice command. The GUI provides an alternative way to interact with the assistant, making it accessible to users who prefer visual interaction.
  - **Custom Widgets**: You can add more interactive widgets to the GUI, such as input fields, dropdowns, and sliders, to expand its functionality.

- **Interactive Widgets**: The GUI includes labels, buttons, and other interactive elements that enhance the user experience.
  - **Dynamic Content**: Extend the GUI to display dynamic content such as live weather updates, system status, or a list of recent commands.

### 7. External Services
- **Weather Information**: The assistant can fetch and report the current weather for a specified city using the OpenWeatherMap API. This feature is customizable by setting your API key in the `ExternalServices` class.
  - **Weather Alerts**: You can add functionality for weather alerts, such as notifications for severe weather conditions.

- **API Interaction**: A generic method for interacting with other external APIs, allowing for flexible integration of additional services.
  - **Service Extensions**: Extend the assistant to integrate with other services like news APIs, currency converters, or even smart home devices.

## Getting Started

### Prerequisites

To run this project, you need to have the following installed:

- **Python 3.6 or higher**
  - Ensure you have the latest version of Python installed.
- **pip (Python package installer)**
  - You can install pip from [here](https://pip.pypa.io/en/stable/installation/).

### Required Python Libraries

Install the necessary Python libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition webbrowser requests opencv-python pyautogui tkinter beautifulsoup4 pywhatkit
```

### API Keys

For the assistant to interact with external services like weather reporting, you need an API key from OpenWeatherMap. Replace `"your_api_key_here"` in the `ExternalServices` class with your actual API key. You can get a free API key by signing up [here](https://home.openweathermap.org/users/sign_up).

### Directory Structure

The project is structured into separate Python files, each representing a different API:

- `main.py`: The main script that ties everything together and handles voice commands.
- `speech_recognition_api.py`: Handles speech recognition and text-to-speech functionality.
- `web_interaction_api.py`: Manages web browsing, Google search, and YouTube video playback.
- `email_assistant_api.py`: Handles sending emails and managing contacts.
- `media_handler_api.py`: Manages video recording and screenshot capturing.
- `system_utilities_api.py`: Provides various system utilities such as time retrieval, random number generation, and directory listing.
- `gui_handler_api.py`: Manages the graphical user interface (GUI) using `tkinter`.
- `external_services_api.py`: Interacts with external services, such as fetching weather data.

### Running the Project

1. **Clone the repository** to your local machine:

```bash
git clone https://github.com/your-username/ai-personal-assistant.git
cd ai-personal-assistant
```

2. **Install dependencies**:

Ensure all required Python libraries are installed using the pip command provided above.

3. **Run the main script**:

```bash
python main.py
```

4. **Interact with the assistant** using voice commands. The assistant will respond to various commands and perform tasks as described in the features section.

## Customization

### Adding New Commands

To add new voice commands:

1. Open `main.py`.
2. In the `while True` loop, add a new condition to check for the command.
3. Call the appropriate method from the relevant API class to execute the command.

### Extending Functionality

You can extend the assistant’s functionality by adding new methods to the existing API classes or by creating new API classes. For example, you can add a method to the `ExternalServices` class to fetch stock market data or to the `SystemUtilities` class to automate file backups.

### Integrating with Other Services

Use the `ExternalServices` class as a template to integrate with additional external APIs. For instance, you can integrate the assistant with a news API to fetch and read out the latest news headlines or with a currency conversion API to provide real-time exchange rates.

## Contributing

Contributions are welcome!

 If you have ideas for improving the project or adding new features, feel free to fork the repository, make your changes, and submit a pull request.

### Steps to Contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix.
3. **Commit your changes**.
4. **Push to the branch**.
5. **Open a pull request**.

Please ensure that your code adheres to the existing style and structure of the project. Include detailed commit messages and documentation for any new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- **OpenAI**: For providing the foundational technology that inspires AI-driven projects.
- **Python**: For being an accessible and powerful programming language that enables projects like this.
- **Community**: For the support, tutorials, and documentation that make developing such projects possible.
