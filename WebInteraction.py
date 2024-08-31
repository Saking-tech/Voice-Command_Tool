import webbrowser
import pywhatkit as pk
import requests
from bs4 import BeautifulSoup

class WebInteraction:
    def __init__(self):
        self.yt_url = 'https://www.youtube.com'

    def open_website(self, url):
        """
        Opens the specified website in the default web browser.
        """
        webbrowser.open(url)
        print(f"Opening {url}")

    def search_google(self, query):
        """
        Performs a Google search using the specified query.
        """
        pk.search(query)
        print(f"Searching Google for: {query}")

    def play_youtube_video(self, video_name):
        """
        Plays a specified video on YouTube.
        """
        pk.playonyt(video_name)
        print(f"Playing {video_name} on YouTube")

    def get_website_content(self, url):
        """
        Fetches and returns the content of a website.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            print(f"Successfully fetched content from {url}")
            return soup.prettify()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch content from {url}: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    web_interact = WebInteraction()

    # Example: Open a website
    web_interact.open_website("https://www.google.com")

    # Example: Perform a Google search
    web_interact.search_google("OpenAI ChatGPT")

    # Example: Play a YouTube video
    web_interact.play_youtube_video("Never Gonna Give You Up")

    # Example: Get website content
    content = web_interact.get_website_content("https://www.wikipedia.org")
    if content:
        print(content[:500])  # Print the first 500 characters of the content
