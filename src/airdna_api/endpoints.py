from generic_api.endpoints import PostEndpoint

from client import AirDNAClient
from serializers import ReportRequestSerializer, ReportResponseSerializer


class RentalizerEndpoint(PostEndpoint):
    endpoint_url = "rentalizer/estimate"
    client_class = AirDNAClient
    response_entity_class = ReportResponseSerializer
    request_entity_class = ReportRequestSerializer
