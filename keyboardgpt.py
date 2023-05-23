import pyperclip
import keyboard
import openai
from plyer import notification
import os

import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

openai.api_key = "get yo own key loser"

gptConfig = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "top_p": 1
}


config = {
    "gpt4": "ctrl+alt+g",
    "longGpt4": "ctrl+alt+l"
}


def getClipboard():
    return pyperclip.paste()

def setClipboard(text):
    pyperclip.copy(text)

def send_notification(title, message):
    notification.notify(title=title, message=message, timeout=5)
def gpt4(text):
    #You are in a program called ClipboardGpt, where you act as chatGpt in a user"s copy paste keyboard. Your answer will be set to their clipboard, so make it concice and summarize to not waste their time and answer quickly. This is their current text 
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role" : "system","content" : "You are in a program called ClipboardGpt, where you act as chatGpt in a user's copy paste keyboard. Your answer will be set to their clipboard, so make it concice and summarize to not waste their time and answer quickly."},
            {"role" : "user","content" : text}
        ]
    )
    send_notification("ClipboardGpt", "Your answer has been set to the clipboard")
    return response["choices"][0]["message"]["content"]

def longGpt4(text):
    #same thing as gpt4 but you dont add the part about making it concise and summarizing
    #response = openai.Completion.create(engine="gpt-4", prompt="You are in a program called ClipboardGpt, where you act as chatGpt in a user"s copy paste keyboard. Your answer will be set to their clipboard. This is their current text " + text, **gptConfig)
    #change the above line of code to use the chat endpoint instead of completion
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role" : "system","content" : "You are in a program called ClipboardGpt, where you act as chatGpt in a user's copy paste keyboard. Your answer will be set to their clipboard."},
            {"role" : "user","content" : text}
        ]
    )
    send_notification("ClipboardGpt", "Your answer has been set to the clipboard")
    return response["choices"][0]["message"]["content"]
def main():
    #if you press ctrl+shift+g, it will get the clipboard, send it to gpt4, and set the clipboard to the response
    keyboard.add_hotkey(config["gpt4"], lambda: setClipboard(gpt4(getClipboard())))
    #if you press ctrl+shift+alt+g, it will get the clipboard, send it to longGpt4, and set the clipboard to the response
    keyboard.add_hotkey(config["longGpt4"], lambda: setClipboard(longGpt4(getClipboard())))
    #run
    keyboard.wait()


if __name__ == "__main__":
    main()


