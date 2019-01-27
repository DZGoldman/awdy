from flask import Flask, render_template
from flask_cors import CORS

import os, json, time
from threading import Thread

app = Flask(__name__, static_folder="./build/static", template_folder="./build")

CORS(app)

 

# data = main() if not os.environ.get('DEV') else read_json_file() 

# @app.route('/data', methods=['Get'])
# def home():

#     return  json.dumps(data)


@app.route('/', methods=['Get'])

def index():
    '''Return index.html for all non-api routes'''
    return render_template( 'index.html') 

 
# def cron():
#     global data
#     while True:
#         time.sleep(60*30)
#         data = main()
# Thread(target = cron).start()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEV'), use_reloader=False)


