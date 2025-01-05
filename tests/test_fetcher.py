from fastapi.testclient import TestClient
from data_market_index_api.main import app

client = TestClient(app)

def test_fetch_market_data():
    response = client.get(
        "/api/v1/fetch-data",
        params={
            "index_name": "S&P500",
            "start_date": "2023-01-01",
            "end_date": "2023-01-07",
            "periodicity": "daily"
        },
    )
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 7
    assert data[0]["value"] == 100
