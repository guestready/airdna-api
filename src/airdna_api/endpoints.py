from typing import Any

from generic_api.endpoints import PostEndpoint

from .client import AirDNAClient
from .serializers import RentalizerEstimateRequestSerializer, RentalizerEstimateResponseSerializer


class AirDNAEndpoint(PostEndpoint):

    def __init__(self, *args: Any, bearer_token: str, **kwargs: Any) -> None:
        self.bearer_token = bearer_token
        super().__init__(*args, **kwargs)

    def get_client_context(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        client_context = super().get_client_context(*args, **kwargs)
        client_context["bearer_token"] = self.bearer_token
        return client_context


class RentalizerEstimateEndpoint(AirDNAEndpoint):
    endpoint_url = "rentalizer/estimate"
    client_class = AirDNAClient
    response_entity_class = RentalizerEstimateResponseSerializer
    request_entity_class = RentalizerEstimateRequestSerializer
