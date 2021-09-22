from flask import request, Blueprint
from container import ads_service

ad_blueprint = Blueprint('ad_blueprint', __name__)


@ad_blueprint.route('/api/getAd', methods=['POST'])
def get_ad_delegate():
    request_data = request.get_json()
    sdk_version = request_data['sdkVersion']
    session_id = request_data['sessionId']
    platform = request_data['platform']
    username = request_data['username']
    country_code = request_data['countryCode']

    response = ads_service.get_ad(sdk_version, username)

    return response.content
