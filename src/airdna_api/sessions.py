from typing import Any


class AirDNASession:
    base_url = "https://api.airdna.co/api/enterprise/v1/"

    def __init__(self, *args: Any, context: dict[str, Any], **kwargs: Any) -> None:
        self.bearer_token = context["bearer_token"]
        super().__init__(*args, **kwargs)

    def params(self) -> dict[str, Any]:
        return {}

    def get_base_url(self) -> str:
        return self.base_url

    def headers(self) -> dict[str, Any]:
        return {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
        }
