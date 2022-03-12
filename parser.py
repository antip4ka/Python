import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])

from bs4 import BeautifulSoup

import requests


url = "https://news.ycombinator.com/"

requests = requests.get(url)

soup = BeautifulSoup(requests.text, "html.parser")

print (soup