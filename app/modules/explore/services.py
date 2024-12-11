from app.modules.explore.repositories import ExploreRepository
from core.services.BaseService import BaseService


class ExploreService(BaseService):
    def __init__(self):
        super().__init__(ExploreRepository())

    def filter(self, query="", sorting="newest", publication_type="any", tags=[],
               config_number=0, core_features=0, **kwargs):

        if config_number == '' or int(config_number) < 0:
            config_number = 0
        if core_features == '' or int(core_features) < 0:
            core_features = 0

        return self.repository.filter(query, sorting, publication_type, tags, config_number, core_features, **kwargs)
