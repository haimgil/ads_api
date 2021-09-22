from service.repository import Repository, StatsDimension


class StatsService:

    def __init__(self, repository: Repository):
        self.repository = repository

    def calc_stats(self, filter_type: StatsDimension) -> []:
        ad_requests_counts = self.repository.get_ad_requests_amount(filter_type)
        impressions_counts = self.repository.get_impressions_amount(filter_type)
        keys = set(ad_requests_counts.keys()).union(set(impressions_counts.keys()))
        stats = []
        for key in keys:
            ad_req_count = ad_requests_counts.get(key, 0)
            imp_count = impressions_counts.get(key, 0)
            fill_rate = imp_count / ad_req_count if ad_req_count else 0

            stat = {
                filter_type.value: key,
                'ads': ad_req_count,
                'impression': imp_count,
                'fill_rate': fill_rate
            }
            stats.append(stat)
        return stats
