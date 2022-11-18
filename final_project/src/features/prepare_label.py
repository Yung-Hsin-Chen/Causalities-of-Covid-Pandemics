import pandas as pd

class PrepareLabel:

    def __init__(self, df):
        self._df = df

    def prepare_label(self):
        self._df["total_deaths_per_million_level"] = pd.cut(self._df["total_deaths_per_million"], \
                                                     bins=[0, 1500, 3500, 5000, 10000], \
                                                     labels=[0, 1, 2, 3])
        del self._df["total_deaths_per_million"]
        return

    def apply_prepare_label(self) -> pd.core.frame.DataFrame:

        self.prepare_label()
        return self._df