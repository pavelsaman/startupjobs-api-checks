import pytest
import requests
from Configuration.Config import Config
from Libraries.JSONReader import JSONReader


class TestOffersUrlEndpoint:

    endpoint = "/api/offers-url"

    @pytest.mark.parametrize(
        ("query_params", "expected_status_code", "expected_offer_url"),
        JSONReader.read_json(f"Resources/offers_url.json")
    )
    def test_invalid_identifiers(self, query_params, expected_status_code, expected_offer_url):
        response = requests.get(f"{Config.base_url()}{self.endpoint}", params=query_params)
        assert response.status_code == expected_status_code
        if expected_offer_url:
            assert response.text == expected_offer_url
