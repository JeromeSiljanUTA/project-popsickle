from threading import Lock

import pandas as pd

# df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, index=[1, 2, 3])

# cols = df.columns.to_list()

counter = 0
 
def increment()
    global counter
    counter += 1


