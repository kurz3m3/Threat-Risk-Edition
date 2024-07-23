from flask import Flask
import probability
import pygame
import random
import numpy as np
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
