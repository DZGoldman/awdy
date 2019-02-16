from flask import Flask, render_template
from flask_cors import CORS

import os, json, time
from threading import Thread
import yaml

app = Flask(__name__, static_folder="./build/static", template_folder="./build")

CORS(app)

def set_up():
    stream = open('config.yml', 'r')
    config = yaml.load(stream).copy()
    def read_coin_data(name):
        fname = "_data/coins/{}.yml".format(name)
        stream = open(fname, 'r')
        return yaml.load(stream).copy()

    all_data = []
    for name in config:
        if config[name]:
            all_data.append(read_coin_data(name))
    return all_data 

all_coin_data = set_up()


@app.route('/data', methods=['Get'])
def home():
    return  json.dumps(all_coin_data)


@app.route('/', methods=['Get'])

def index():
    '''Return index.html for all non-api routes'''
    # return render_template( 'index.html') 
    return render_template( 'index.html', coming_soon = os.environ.get('COMING_SOON') ) 

 
def cron():
    global all_coin_data
    while True:
        time.sleep(60*5)
        all_coin_data = set_up()
Thread(target = cron).start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEV'), use_reloader=False)


