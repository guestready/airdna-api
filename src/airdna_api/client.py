from generic_api.errors_handler import HttpErrorsHandler
from generic_api.generics import GenericClient
from generic_api.retries_handler import RetryOnError

from .sessions import AirDNASession


class AirDNAClient(GenericClient):
    session_class = AirDNASession
    errors_handler_class = HttpErrorsHandler
    retries_handler_class = RetryOnError
