from typing import Any

from generic_api.errors_handler import HttpErrorsHandler
from generic_api.generics import GenericClient
from generic_api.retries_handler import RetryOnError

from .sessions import AirDNASession


class AirDNAClient(GenericClient):
    session_class = AirDNASession
    errors_handler_class = HttpErrorsHandler
    retries_handler_class = RetryOnError

    def __init__(self, *args: Any, bearer_token: str, **kwargs: Any) -> None:
        self.bearer_token = bearer_token
        super().__init__(*args, **kwargs)

    def get_session_context(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        session_context = super().get_session_context(*args, **kwargs)
        session_context["bearer_token"] = self.bearer_token
        return session_context
