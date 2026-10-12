import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema_mod = cinema.loc[cinema["id"] % 2 != 0, :].copy()
    cinema_mod = cinema_mod.loc[cinema_mod["description"] != "boring", :]
    return cinema_mod.sort_values(by="rating", ascending=False)