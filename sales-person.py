import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    sale_merged = sales_person.merge(orders, on="sales_id", how="left")
    comp_merged = sale_merged.merge(company, on="com_id", how="left", suffixes=["", "_comp"])
    set_names = set(comp_merged["name"]).difference(set(comp_merged.loc[comp_merged["name_comp"] == "RED", "name"]))
    return pd.DataFrame(list(set_names), columns=["name"])