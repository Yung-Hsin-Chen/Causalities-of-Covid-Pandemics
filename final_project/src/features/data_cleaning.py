import pandas as pd

class CleanData:

    def __init__(self, df:list, boundary:int=200):
        self._df = df
        self._boundary = boundary
        self._keep_col = ["location", "date", "aged_65_older", "aged_70_older", "cardiovasc_death_rate",
                          "diabetes_prevalence", "gdp_per_capita", "hospital_beds_per_thousand", "people_fully_vaccinated_per_hundred",\
                          "human_development_index", "life_expectancy", "median_age", "population_density", "population",\
                          "total_cases_per_million"]

    def get_count(self, df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:

        df = df.groupby(["location"])[["date"]].count().rename(columns={"date": "count"})\
            .reset_index()

        return df

    def remove_less_entry_countries(self):

        below_boundary_country = self.get_count(self._df)[self.get_count(self._df)["count"] < self._boundary]\
                                 ["location"].tolist()
        self._df = self._df[~self._df.location.isin(below_boundary_country)]

        return

    def apply_remove_less_entry_countries(self):
        self.remove_less_entry_countries()
        return

    def get_location_wo_null(self):
        self._df = self._df[self._keep_col]
        self._df = self._df.sort_values(by=["location", "date"])
        self._df = self._df.groupby(["location", "aged_65_older"]).agg("last").reset_index()
        self._df = self._df.drop("date", axis=1)
        return

    def apply_get_location_wo_null(self):
        self.get_location_wo_null()

        return

    def age_percentage(self):
        self._df["aged_65_older_percentage"] = self._df["aged_65_older"] / self._df["population"]
        self._df["aged_70_older_percentage"] = self._df["aged_70_older"] / self._df["population"]
        del self._df["aged_65_older"]
        del self._df["aged_70_older"]
        del self._df["population"]
        return

    def apply_age_percentage(self):
        self.age_percentage()
        return

    def apply_clean_data(self) ->  pd.core.frame.DataFrame:
        self.apply_remove_less_entry_countries()
        self.apply_get_location_wo_null()
        self.apply_age_percentage()
        return self._df
