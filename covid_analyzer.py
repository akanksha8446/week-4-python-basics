import pandas as pd
import matplotlib.pyplot as plt
import os


class CovidAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.DataFrame()
        self.load_data()

    # --------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------

    def load_data(self):

        try:
            self.df = pd.read_csv(
                self.file_path,
                parse_dates=["date"]
            )

            print("\nDataset loaded successfully!")
            print(f"Total records: {len(self.df):,}")

        except FileNotFoundError:
            print("\nERROR: Dataset file not found.")
            print(
                "Please place owid-covid-data.csv "
                "inside the data folder."
            )

        except Exception as e:
            print("\nERROR while loading dataset:", e)

    # --------------------------------------------------
    # DATASET SUMMARY
    # --------------------------------------------------

    def dataset_summary(self):

        if self.df.empty:
            return

        print("\n" + "=" * 55)
        print("             DATASET SUMMARY")
        print("=" * 55)

        print(f"Total Records       : {len(self.df):,}")
        print(
            f"Total Countries/Locations : "
            f"{self.df['location'].nunique():,}"
        )

        print(
            f"Date Range          : "
            f"{self.df['date'].min().date()} "
            f"to "
            f"{self.df['date'].max().date()}"
        )

        print(
            f"Total Columns       : "
            f"{len(self.df.columns)}"
        )

    # --------------------------------------------------
    # GLOBAL STATISTICS
    # --------------------------------------------------

    def global_statistics(self):

        if self.df.empty:
            return

        # Get latest available record for each country
        latest = self.df.sort_values("date").groupby(
            "location"
        ).tail(1)

        total_cases = latest["total_cases"].sum(
            skipna=True
        )

        total_deaths = latest["total_deaths"].sum(
            skipna=True
        )

        total_vaccinations = latest[
            "total_vaccinations"
        ].sum(skipna=True)

        print("\n" + "=" * 55)
        print("             GLOBAL COVID STATISTICS")
        print("=" * 55)

        print(
            f"Total Cases        : "
            f"{total_cases:,.0f}"
        )

        print(
            f"Total Deaths       : "
            f"{total_deaths:,.0f}"
        )

        print(
            f"Total Vaccinations : "
            f"{total_vaccinations:,.0f}"
        )

        print(
            f"Countries/Locations: "
            f"{latest['location'].nunique():,}"
        )

    # --------------------------------------------------
    # TOP COUNTRIES BY CASES
    # --------------------------------------------------

    def top_countries_by_cases(self, n=10):

        if self.df.empty:
            return pd.DataFrame()

        latest = self.df.sort_values(
            "date"
        ).groupby(
            "location"
        ).tail(1)

        result = latest[
            [
                "location",
                "total_cases"
            ]
        ].dropna()

        result = result.sort_values(
            "total_cases",
            ascending=False
        ).head(n)

        print("\n" + "=" * 55)
        print(f"       TOP {n} COUNTRIES BY TOTAL CASES")
        print("=" * 55)

        print(
            result.to_string(index=False)
        )

        return result

    # --------------------------------------------------
    # TOP COUNTRIES BY DEATHS
    # --------------------------------------------------

    def top_countries_by_deaths(self, n=10):

        if self.df.empty:
            return pd.DataFrame()

        latest = self.df.sort_values(
            "date"
        ).groupby(
            "location"
        ).tail(1)

        result = latest[
            [
                "location",
                "total_deaths"
            ]
        ].dropna()

        result = result.sort_values(
            "total_deaths",
            ascending=False
        ).head(n)

        print("\n" + "=" * 55)
        print(f"       TOP {n} COUNTRIES BY TOTAL DEATHS")
        print("=" * 55)

        print(
            result.to_string(index=False)
        )

        return result

    # --------------------------------------------------
    # TOP COUNTRIES BY VACCINATION
    # --------------------------------------------------

    def top_countries_by_vaccinations(self, n=10):

        if self.df.empty:
            return pd.DataFrame()

        latest = self.df.sort_values(
            "date"
        ).groupby(
            "location"
        ).tail(1)

        result = latest[
            [
                "location",
                "total_vaccinations"
            ]
        ].dropna()

        result = result.sort_values(
            "total_vaccinations",
            ascending=False
        ).head(n)

        print("\n" + "=" * 55)
        print(
            f"     TOP {n} COUNTRIES BY VACCINATIONS"
        )
        print("=" * 55)

        print(
            result.to_string(index=False)
        )

        return result

    # --------------------------------------------------
    # SEARCH COUNTRY
    # --------------------------------------------------

    def search_country(self, country):

        if self.df.empty:
            return pd.DataFrame()

        countries = self.df[
            "location"
        ].dropna().unique()

        matches = [
            c for c in countries
            if country.lower() in c.lower()
        ]

        if not matches:

            print(
                "\nNo matching country found."
            )

            return pd.DataFrame()

        print("\nMatching countries:")

        for i, name in enumerate(
            matches,
            start=1
        ):
            print(f"{i}. {name}")

        try:

            choice = int(
                input(
                    "\nSelect country number: "
                )
            )

            selected_country = matches[
                choice - 1
            ]

            return self.country_analysis(
                selected_country
            )

        except (
            ValueError,
            IndexError
        ):

            print(
                "\nInvalid selection."
            )

            return pd.DataFrame()

    # --------------------------------------------------
    # COUNTRY ANALYSIS
    # --------------------------------------------------

    def country_analysis(self, country):

        data = self.df[
            self.df["location"] == country
        ].copy()

        if data.empty:

            print(
                "\nCountry not found."
            )

            return pd.DataFrame()

        latest = data.sort_values(
            "date"
        ).iloc[-1]

        print("\n" + "=" * 55)
        print(
            f"       COVID ANALYSIS - {country.upper()}"
        )
        print("=" * 55)

        self.print_value(
            "Total Cases",
            latest.get("total_cases")
        )

        self.print_value(
            "Total Deaths",
            latest.get("total_deaths")
        )

        self.print_value(
            "New Cases",
            latest.get("new_cases")
        )

        self.print_value(
            "New Deaths",
            latest.get("new_deaths")
        )

        self.print_value(
            "Population",
            latest.get("population")
        )

        self.print_value(
            "Total Vaccinations",
            latest.get("total_vaccinations")
        )

        self.print_value(
            "People Vaccinated",
            latest.get("people_vaccinated")
        )

        self.print_value(
            "Fully Vaccinated",
            latest.get("people_fully_vaccinated")
        )

        self.print_value(
            "Cases per Million",
            latest.get(
                "total_cases_per_million"
            )
        )

        self.print_value(
            "Deaths per Million",
            latest.get(
                "total_deaths_per_million"
            )
        )

        return data

    # --------------------------------------------------
    # PRINT VALUES
    # --------------------------------------------------

    def print_value(self, label, value):

        if pd.isna(value):

            print(
                f"{label:<25}: N/A"
            )

        else:

            if isinstance(
                value,
                (int, float)
            ):

                print(
                    f"{label:<25}: "
                    f"{value:,.2f}"
                )

            else:

                print(
                    f"{label:<25}: "
                    f"{value}"
                )

    # --------------------------------------------------
    # CASES OVER TIME
    # --------------------------------------------------

    def cases_over_time(self, country):

        data = self.df[
            self.df["location"] == country
        ].copy()

        if data.empty:
            print("\nCountry not found.")
            return

        data = data.dropna(
            subset=["total_cases"]
        )

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            data["date"],
            data["total_cases"]
        )

        plt.title(
            f"COVID-19 Total Cases - {country}"
        )

        plt.xlabel("Date")
        plt.ylabel("Total Cases")

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        os.makedirs(
            "charts",
            exist_ok=True
        )

        plt.savefig(
            f"charts/{country}_cases.png"
        )

        plt.show()

        plt.close()

        print(
            "\nCases chart generated successfully."
        )

    # --------------------------------------------------
    # DEATHS OVER TIME
    # --------------------------------------------------

    def deaths_over_time(self, country):

        data = self.df[
            self.df["location"] == country
        ].copy()

        if data.empty:
            print("\nCountry not found.")
            return

        data = data.dropna(
            subset=["total_deaths"]
        )

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            data["date"],
            data["total_deaths"]
        )

        plt.title(
            f"COVID-19 Total Deaths - {country}"
        )

        plt.xlabel("Date")
        plt.ylabel("Total Deaths")

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        os.makedirs(
            "charts",
            exist_ok=True
        )

        plt.savefig(
            f"charts/{country}_deaths.png"
        )

        plt.show()

        plt.close()

        print(
            "\nDeaths chart generated successfully."
        )

    # --------------------------------------------------
    # VACCINATION PROGRESS
    # --------------------------------------------------

    def vaccination_analysis(
        self,
        country
    ):

        data = self.df[
            self.df["location"] == country
        ].copy()

        if data.empty:
            print("\nCountry not found.")
            return

        data = data.dropna(
            subset=[
                "total_vaccinations"
            ]
        )

        if data.empty:

            print(
                "\nVaccination data unavailable."
            )

            return

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            data["date"],
            data["total_vaccinations"]
        )

        plt.title(
            f"COVID-19 Vaccination Progress - "
            f"{country}"
        )

        plt.xlabel("Date")
        plt.ylabel("Total Vaccinations")

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        os.makedirs(
            "charts",
            exist_ok=True
        )

        plt.savefig(
            f"charts/{country}_vaccinations.png"
        )

        plt.show()

        plt.close()

        print(
            "\nVaccination chart generated successfully."
        )

    # --------------------------------------------------
    # TOP CASES BAR CHART
    # --------------------------------------------------

    def plot_top_cases(self, n=5):

        result = self.top_countries_by_cases(n)

        if result.empty:
            return

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(
            result["location"],
            result["total_cases"]
        )

        plt.title(
            f"Top {n} Countries by Total COVID-19 Cases"
        )

        plt.xlabel("Country")
        plt.ylabel("Total Cases")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        os.makedirs(
            "charts",
            exist_ok=True
        )

        plt.savefig(
            "charts/top_cases.png"
        )

        plt.show()

        plt.close()

        print(
            "\nTop cases chart generated successfully."
        )

    # --------------------------------------------------
    # TOP DEATHS BAR CHART
    # --------------------------------------------------

    def plot_top_deaths(self, n=5):

        result = self.top_countries_by_deaths(n)

        if result.empty:
            return

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(
            result["location"],
            result["total_deaths"]
        )

        plt.title(
            f"Top {n} Countries by COVID-19 Deaths"
        )

        plt.xlabel("Country")
        plt.ylabel("Total Deaths")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        os.makedirs(
            "charts",
            exist_ok=True
        )

        plt.savefig(
            "charts/top_deaths.png"
        )

        plt.show()

        plt.close()

        print(
            "\nTop deaths chart generated successfully."
        )

    # --------------------------------------------------
    # EXPORT DATA
    # --------------------------------------------------

    def export_data(
        self,
        data,
        filename
    ):

        if data.empty:

            print(
                "\nNo data available to export."
            )

            return

        os.makedirs(
            "output",
            exist_ok=True
        )

        path = os.path.join(
            "output",
            filename
        )

        data.to_csv(
            path,
            index=False
        )

        print(
            f"\nReport saved successfully:"
            f"\n{path}"
        )

    # --------------------------------------------------
    # COUNTRY REPORT
    # --------------------------------------------------

    def export_country_report(
        self,
        country
    ):

        data = self.df[
            self.df["location"] == country
        ].copy()

        if data.empty:

            print(
                "\nCountry not found."
            )

            return

        filename = (
            country.replace(" ", "_")
            .replace("/", "_")
            + "_covid_report.csv"
        )

        self.export_data(
            data,
            filename
        )