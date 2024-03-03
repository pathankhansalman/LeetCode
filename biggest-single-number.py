import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    sercount = my_numbers.value_counts()
    single_numbers = list(sercount.loc[sercount == 1].index)
    if len(single_numbers) == 0:
        return pd.DataFrame([None], columns=["num"])
    return pd.DataFrame([max(single_numbers)], columns=["num"])