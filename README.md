# RiverAnalyserPRO
![Continuous Integration build in GitHub Actions](https://github.com/qq23840/python-intermediate-rivercatchment/actions/workflows/main.yml/badge.svg?branch=develop)

![396adf79-2f6b-43ea-946a-f93208f1a76a](https://github.com/PriyaGordon/python-intermediate-rivercatchment/assets/93257279/2b4e792f-00f2-430d-ab25-27c10b40deb5)


# RiverAnalyserPRO

RiverAnalyserPRO is a sophisticated data management system tailored for river catchment surveys and campaigns. Developed in Python, it facilitates the management and analysis of measurement data, supporting a range of functionalities to enhance data understanding and decision-making in hydrological research.

## Main Features

RiverAnalyserPRO offers an array of powerful features:

- **Statistical Analysis**: Perform basic statistical analyses to extract meaningful insights from your data.
- **Multiple Format Support**: Seamlessly work with measurement data in Comma-Separated Value (CSV), XML, and JSON formats.
- **Data Visualization**: Generate intuitive plots to visualize measurement data.
- **Extensible Architecture**: Leverage its Model-View-Controller architecture to easily extend analytical functions and views.

## Prerequisites

Before installing RiverAnalyserPRO, ensure you have the following Python packages installed:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Pandas](https://pandas.pydata.org/) - makes use of Panda's dataframes
- [GeoPandas](https://geopandas.org/) - makes use of GeoPanda's spatial operations
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

### Optional Packages

The following optional packages are required to run RiverCatch's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - RiverCatch's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation

1. **Clone the Repository**: First, clone the RiverAnalyserPRO repository to your local machine using Git.

```bash
git clone https://github.com/PriyaGordon/python-intermediate-rivercatchment/ RiverAnalyserPro
cd RiverAnalyserPRO
```

2. **Set up a Virtual Environment:** It's recommended to create a Python virtual environment for project dependencies.

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies:** RiverAnalyserPRO utilizes Poetry for dependency management. Install all required packages using the following command:

```
poetry install
```

4. **Verify Installation:** Ensure that all dependencies are correctly installed.

```
poetry check
```

5. **Running the Application:** You can now run RiverAnalyserPRO using the following command:

```
python catchment-analysis.py path/to/your/input/file.csv --full-data-analysis
```

6. **Use Optional Flags:** You can use the optional *-m* or *--measurements* flag to specify the name of the measurement data series to load:

```
python catchment-analysis.py path/to/your/input/file.csv --full-data-analysis -m variable
```