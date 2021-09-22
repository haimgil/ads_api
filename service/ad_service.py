from requests import Response
from service.repository import Repository, StatsDimension
from service.gateway_service import GetAdGatewayService


class AdService:

    def __init__(self, repository: Repository, gw_service: GetAdGatewayService) -> None:
        self.repository = repository
        self.gw_service = gw_service

    def get_ad(self, sdk_version, username):
        response: Response = self.gw_service.get_ad_external()
        if response.ok:
            self.repository.ad_increment(StatsDimension.USER, username)
            self.repository.ad_increment(StatsDimension.SDK_VERSION, sdk_version)
        return response
