import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def _tr_helper_(ser):
        if ser.loc['x'] + ser.loc['y'] > ser.loc['z'] and\
                ser.loc['x'] + ser.loc['z'] > ser.loc['y'] and\
                ser.loc['z'] + ser.loc['y'] > ser.loc['x']:
            return "Yes"
        return "No"
    triangle_copy = triangle.copy()
    triangle_copy.loc[:, "triangle"] = triangle.apply(_tr_helper_, axis=1)
    return triangle_copy