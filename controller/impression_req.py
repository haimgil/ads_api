import flask
from flask import request, Blueprint

from container import impression_service

impression_blueprint = Blueprint('impression_blueprint', __name__)


@impression_blueprint.route('/api/impression', methods=['POST'])
def impression():
    request_data = request.get_json()
    username = request_data['username']
    sdk_version = request_data['sdkVersion']
    session_id = request_data['sessionId']
    platform = request_data['platform']
    country_code = request_data['countryCode']

    impression_service.impression(username, sdk_version)
    return flask.Response(status=200)
