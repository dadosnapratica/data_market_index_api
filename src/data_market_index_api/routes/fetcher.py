from fastapi import APIRouter, HTTPException, Query
from typing import Union
from data_market_index_api.services.fetcher import MarketIndexFetcher, Periodicity

router = APIRouter()

@router.get("/fetch-data", tags=["Market Data"])
def fetch_market_data(
    index_name: str,
    start_date: str,
    end_date: str,
    periodicity: Union[Periodicity, str] = Query("daily", enum=["daily", "weekly", "monthly"]),
):
    """
    Fetch market index data.

    Args:
        index_name (str): The name of the market index (e.g., "S&P500").
        start_date (str): Start date in the format YYYY-MM-DD.
        end_date (str): End date in the format YYYY-MM-DD.
        periodicity (str): Data periodicity ("daily", "weekly", or "monthly").

    Returns:
        JSON: Market data as a list of records.
    """
    try:
        # Call the fetcher service
        fetcher = MarketIndexFetcher()
        data = fetcher.fetch_data(index_name, start_date, end_date, periodicity)
        # Include input parameters and fetched data in the response
        return {
            "params": {
                "index_name": index_name,
                "start_date": start_date,
                "end_date": end_date,
                "periodicity": periodicity,
            },
            "data": data.to_dict(orient="records"),
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
