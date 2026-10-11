# Beginner Data Analysis Projects

A collection of beginner-friendly Python/Jupyter exercises focused on data cleaning, exploratory data analysis, and visualization. The notebooks are practice projects based on tutorials and public datasets.

## Projects

| Project folder | Dataset / topic | Main learning goals |
|---|---|---|
| `Project 1 - Weather/` | Weather data | Inspect, clean, and summarize weather observations |
| `Project 2 - Cars/` | Car data | Explore columns, filter records, and summarize vehicle data |
| `Project 3 - Police/` | Police data | Practice grouping, filtering, and exploratory analysis |
| `Project 4 - Covid19/` | COVID-19 data | Explore trends and summarize time-related data |
| `Project 5 - London housing/` | London housing | Clean and explore housing-related data |
| `Project 6 - Census/` | Census data | Practice descriptive analysis of census variables |
| `Project 7 - Udemy/` | Udemy data | Explore course-related data |
| `Project 8 - Netflix/` | Netflix data | Explore a streaming-catalog dataset |

Each project folder generally contains a notebook and its supporting CSV file. Check the notebook's first cells for the exact questions and analysis because this README describes the broad project themes.

## Repository layout

```text
beginner-data-analysis-project/
├── Project 1 - Weather/
├── Project 2 - Cars/
├── Project 3 - Police/
├── Project 4 - Covid19/
├── Project 5 - London housing/
├── Project 6 - Census/
├── Project 7 - Udemy/
├── Project 8 - Netflix/
└── README.md
```

Jupyter checkpoint copies have been removed from the current branch. The Netflix notebook, which previously existed only as a checkpoint, has been preserved under `Project 8 - Netflix/`.

## Getting started

1. Clone or download the repository.
2. Create a Python virtual environment.
3. Install Jupyter, pandas, and the visualization libraries required by a specific notebook.
4. Open the selected notebook and check its relative CSV paths before running all cells.

Example:

```bash
python -m venv .venv
python -m pip install jupyter pandas matplotlib seaborn
jupyter notebook
```

This is a learning/practice repository, not a production application. The notebooks have not all been executed in a clean environment as part of this documentation update.

## Reference

The projects were inspired by tutorial material: [YouTube playlist](https://youtube.com/playlist?list=PLy3lFw0OTlutzXFVwttrtaRGEEyLEdnpy).

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
