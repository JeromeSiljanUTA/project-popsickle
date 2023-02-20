import os
import pickle
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

from statsmodels.tsa.arima.model import ARIMA


def fit_arima(df, arima_order):
    df.set_index("Time", inplace=True)
    ercot = df["ERCOT"]
    train_end = datetime(2021, 1, 1)
    train_data = ercot["2003":"2021"].asfreq("h")
    test_data = ercot["2022"].asfreq("h")
    arima_unfitted = ARIMA(train_data, order=arima_order)
    start = time.perf_counter()
    arima = arima_unfitted.fit()
    print(f"Took {time.perf_counter() - start}s to train ARIMA{arima_order}")
    pickle_arima(arima, arima_order)


def pickle_arima(arima_model, arima_order):
    with open(f"../data/04_models/arima_{arima_order}.obj", "wb") as file:
        pickle.dump(arima_model, file)


def threaded_arima(df, arima_orders):
    with ThreadPoolExecutor() as executor:
        for thread_num, arima_order in enumerate(arima_orders):
            thread_num = executor.submit(fit_arima, df, arima_order)
