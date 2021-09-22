from service.repository import Repository, StatsDimension


class ImpressionService:

    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def impression(self, username, sdk_version):
        self.repository.impression_increment(StatsDimension.USER, username)
        self.repository.impression_increment(StatsDimension.SDK_VERSION, sdk_version)
