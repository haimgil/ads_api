import os

from flask import Flask
from flask_redis import Redis

from container import redis
from controller.ad_requests import ad_blueprint
from controller.impression_req import impression_blueprint
from controller.stats_req import stats_blueprint

app = Flask(__name__)
app.register_blueprint(ad_blueprint)
app.register_blueprint(impression_blueprint)
app.register_blueprint(stats_blueprint)
app.config['REDIS_HOST'] = os.environ.get('REDIS_HOST', 'localhost')
app.config['REDIS_PORT'] = int(os.environ.get('REDIS_PORT', 6379))
app.config['REDIS_DB'] = int(os.environ.get('REDIS_DB', 0))

redis.init_app(app)
