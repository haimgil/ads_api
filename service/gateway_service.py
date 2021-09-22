import requests


class GetAdGatewayService:

    @staticmethod
    def get_ad_external():
        external_api = "https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast"
        response = requests.get(external_api)
        return response
