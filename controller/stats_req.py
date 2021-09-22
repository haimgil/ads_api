from flask import request, Blueprint, jsonify

from container import stats_service
from service.repository import StatsDimension

stats_blueprint = Blueprint('stats_blueprint', __name__)


@stats_blueprint.route('/api/getStats', methods=['GET'])
def get_stats():
    filter_type = request.args.get('filterType')
    if filter_type == 'user':
        dimension = StatsDimension.USER
    elif filter_type == 'sdk_version':
        dimension = StatsDimension.SDK_VERSION
    else:
        return 'unknown filterType', 400
    stats = stats_service.calc_stats(dimension)
    print(stats)
    return jsonify(stats)
