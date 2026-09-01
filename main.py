from covid_analyzer import CovidAnalyzer


# --------------------------------------------------
# DATASET PATH
# --------------------------------------------------

FILE_PATH = "data/owid-covid-data.csv"


# --------------------------------------------------
# CREATE ANALYZER OBJECT
# --------------------------------------------------

analyzer = CovidAnalyzer(FILE_PATH)


# --------------------------------------------------
# MENU
# --------------------------------------------------

while True:

    print("\n")
    print("=" * 60)
    print("          🦠 COVID-19 DATA ANALYSIS SYSTEM")
    print("=" * 60)

    print("1.  Dataset Summary")
    print("2.  Global COVID Statistics")
    print("3.  Top 10 Countries by Cases")
    print("4.  Top 10 Countries by Deaths")
    print("5.  Top 10 Countries by Vaccinations")
    print("6.  Search Country")
    print("7.  Country COVID Analysis")
    print("8.  Plot Top 5 Countries by Cases")
    print("9.  Plot Top 5 Countries by Deaths")
    print("10. Plot Cases Over Time")
    print("11. Plot Deaths Over Time")
    print("12. Plot Vaccination Progress")
    print("13. Export Country Report")
    print("14. Exit")

    print("=" * 60)

    choice = input(
        "Enter your choice: "
    ).strip()

    # --------------------------------------------------
    # DATASET SUMMARY
    # --------------------------------------------------

    if choice == "1":

        analyzer.dataset_summary()

    # --------------------------------------------------
    # GLOBAL STATISTICS
    # --------------------------------------------------

    elif choice == "2":

        analyzer.global_statistics()

    # --------------------------------------------------
    # TOP CASES
    # --------------------------------------------------

    elif choice == "3":

        analyzer.top_countries_by_cases(
            10
        )

    # --------------------------------------------------
    # TOP DEATHS
    # --------------------------------------------------

    elif choice == "4":

        analyzer.top_countries_by_deaths(
            10
        )

    # --------------------------------------------------
    # TOP VACCINATIONS
    # --------------------------------------------------

    elif choice == "5":

        analyzer.top_countries_by_vaccinations(
            10
        )

    # --------------------------------------------------
    # SEARCH COUNTRY
    # --------------------------------------------------

    elif choice == "6":

        country = input(
            "\nEnter country name: "
        ).strip()

        analyzer.search_country(
            country
        )

    # --------------------------------------------------
    # COUNTRY ANALYSIS
    # --------------------------------------------------

    elif choice == "7":

        country = input(
            "\nEnter exact country name: "
        ).strip()

        analyzer.country_analysis(
            country
        )

    # --------------------------------------------------
    # TOP CASES CHART
    # --------------------------------------------------

    elif choice == "8":

        analyzer.plot_top_cases(
            5
        )

    # --------------------------------------------------
    # TOP DEATHS CHART
    # --------------------------------------------------

    elif choice == "9":

        analyzer.plot_top_deaths(
            5
        )

    # --------------------------------------------------
    # CASES OVER TIME
    # --------------------------------------------------

    elif choice == "10":

        country = input(
            "\nEnter country name: "
        ).strip()

        analyzer.cases_over_time(
            country
        )

    # --------------------------------------------------
    # DEATHS OVER TIME
    # --------------------------------------------------

    elif choice == "11":

        country = input(
            "\nEnter country name: "
        ).strip()

        analyzer.deaths_over_time(
            country
        )

    # --------------------------------------------------
    # VACCINATION
    # --------------------------------------------------

    elif choice == "12":

        country = input(
            "\nEnter country name: "
        ).strip()

        analyzer.vaccination_analysis(
            country
        )

    # --------------------------------------------------
    # EXPORT REPORT
    # --------------------------------------------------

    elif choice == "13":

        country = input(
            "\nEnter country name: "
        ).strip()

        analyzer.export_country_report(
            country
        )

    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------

    elif choice == "14":

        print("\nThank you for using")
        print("COVID-19 Data Analysis System!")

        break

    else:

        print(
            "\nInvalid choice."
            " Please enter a number from 1 to 14."
        )