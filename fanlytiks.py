from flask import Flask, render_template, request, send_from_directory
import requests
from twitter import *


app = Flask(__name__)

@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
	api = Api(consumer_key='QBSJiqeISh3g98v4En482W0rU',
                      consumer_secret='x8Wgr1RIF5b6sR14wkuNIZvNOTslCBkrRKUBLCSCBT6Od0oM0S',
                      access_token_key='518104135-N40eShH1AonSJ4Ca0STFbw8ht9VbyCSoeHw8tJig',
                      access_token_secret='gvJewbmkt3PhNg24WU6ITitsAyMVHex3VgcWYV4BJbTWr')
	results = api.GetSearch(raw_query="q=%23VIVOIPL&result_type=recent&since=2014-07-19&count=100")
	return str(results)



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)