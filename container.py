from flask_redis import Redis

from service.ad_service import AdService
from service.gateway_service import GetAdGatewayService
from service.impression_service import ImpressionService
from service.repository import Repository
from service.stats_service import StatsService

redis = Redis()

repository = Repository(redis)

gw_service = GetAdGatewayService()
ads_service = AdService(repository, gw_service)
impression_service = ImpressionService(repository)
stats_service = StatsService(repository)

