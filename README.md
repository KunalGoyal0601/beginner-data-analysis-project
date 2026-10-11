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

Most project folders contain a notebook and its supporting CSV file. **Project 8 - Netflix is an exception:** the notebook is included, but `netflix.csv` is not redistributed because its original source and redistribution license have not been verified. Obtain it from its original publisher, review the terms, and place it next to the notebook before running it. The notebook now reports a clear error when the local file is missing. Check each notebook's first cells for the exact questions and analysis because this README describes broad project themes.

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


## Dataset licensing note

Do not add third-party CSV files to this repository until the original source and redistribution terms are confirmed. For the Netflix exercise, keep the dataset local and record its source URL and license in your own notes. The notebook is a learning exercise; several question prompts are intentionally not fully implemented yet.


## Dataset provenance and redistribution

The notebooks are based on a tutorial playlist, but this repository does not yet record the original download URL and redistribution terms for each of the CSV files in Projects 1–7. Before reusing or redistributing those files, verify the source and license for each one. A tutorial link or public download alone is not a redistribution license. If permission cannot be confirmed, remove the affected CSV from the public repository and document how readers can obtain it from the original publisher. The Netflix CSV is intentionally not included until its source and terms are verified.
