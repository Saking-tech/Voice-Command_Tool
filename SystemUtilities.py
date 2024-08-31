import os
import datetime
import random
from time import sleep

class SystemUtilities:
    def __init__(self):
        pass

    def get_current_time(self):
        """
        Returns the current time as a string.
        """
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Current time is: {current_time}")
        return current_time

    def shutdown_system(self):
        """
        Shuts down the system.
        """
        print("Shutting down the system...")
        os.system("shutdown /s /t 1")

    def restart_system(self):
        """
        Restarts the system.
        """
        print("Restarting the system...")
        os.system("shutdown /r /t 1")

    def sleep_system(self):
        """
        Puts the system to sleep.
        """
        print("Putting the system to sleep...")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    def create_random_number(self, start=1, end=100):
        """
        Generates a random number between the specified range.
        """
        number = random.randint(start, end)
        print(f"Generated random number: {number}")
        return number

    def delay_execution(self, seconds):
        """
        Delays the execution for the specified number of seconds.
        """
        print(f"Delaying execution for {seconds} seconds...")
        sleep(seconds)

    def list_directory_contents(self, path="."):
        """
        Lists the contents of the specified directory.
        """
        try:
            contents = os.listdir(path)
            print(f"Contents of directory {path}: {contents}")
            return contents
        except Exception as e:
            print(f"Error accessing directory {path}: {e}")
            return []

# Example usage:
if __name__ == "__main__":
    utils = SystemUtilities()

    # Example: Get the current time
    utils.get_current_time()

    # Example: Generate a random number
    utils.create_random_number(10, 50)

    # Example: List directory contents
    utils.list_directory_contents("/path/to/directory")

    # Example: Delay execution
    utils.delay_execution(5)

    # Example: Shutdown system (Use with caution)
    # utils.shutdown_system()
