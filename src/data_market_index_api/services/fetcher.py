from typing import Union
import pandas as pd
from enum import Enum
from data_market_index_fetcher.indexes.ibov.IbovWebScrapperB3 import IBovWebScrapperB3, Periodicity

class Periodicity(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class MarketIndexFetcher:
    def fetch_data(
        self,
        index_name: str,
        start_date: str,
        end_date: str,
        periodicity: Union[Periodicity, str] = Periodicity.DAILY,
    ) -> pd.DataFrame:
        """
        Fetch market index data.

        Args:
            index_name (str): Name of the market index (e.g., "S&P500").
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            periodicity (Union[Periodicity, str]): Data periodicity (daily, weekly, or monthly).

        Returns:
            pd.DataFrame: DataFrame containing market index data.
        """
        if index_name.upper()=="IBOV":
            ibov_fetcher=IBovWebScrapperB3()
            df_return=ibov_fetcher.fetch_data(start_date, end_date, periodicity)
        else:    
            # Mock implementation for demonstration
            data = {
                "date": pd.date_range(start=start_date, end=end_date, freq="D"),
                "value": [100 + i for i in range((pd.to_datetime(end_date) - pd.to_datetime(start_date)).days + 1)],
            }

            df_return=pd.DataFrame(data)
        return df_return
