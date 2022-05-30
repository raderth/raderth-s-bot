from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return ('<script type="text/javascript">window.location.href = "https://stats.uptimerobot.com/m8jYYs5qjD";</script>')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
  