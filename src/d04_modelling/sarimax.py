import pickle
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from statsmodels.tsa.statespace.sarimax import SARIMAX


def fit_sarimax(df, seasonal_order, order):
    print(f"fitting sarimax {seasonal_order}, {order}")
    df.set_index("Time", inplace=True)
    ercot = df["ERCOT"]
    train_end = datetime(2021, 1, 1)
    train_data = ercot["2003":"2021"].asfreq("h")
    test_data = ercot["2022"].asfreq("h")
    sarimax_unfitted = SARIMAX(train_data, seasonal_order=seasonal_order, order=order)
    start = time.perf_counter()
    sarimax = sarimax_unfitted.fit()
    print(
        f"Took {time.perf_counter() - start}s to train SARIMAX{seasonal_order},{order}"
    )
    pickle_sarimax(sarimax, seasonal_order, order)


def pickle_sarimax(sarimax_model, seasonal_order, order):
    with open(f"../data/04_models/sarimax_{seasonal_order}_{order}.obj", "wb") as file:
        pickle.dump(sarimax_model, file)
