# Learning SIR Models with Python

A reusable Python module for constructing, simulating, and visualizing Susceptible–Infected–Recovered (SIR) epidemiological models.

This repository originated as a final project for **COGS 18 (Introduction to Python)** at the **University of California, San Diego** and has since been refactored into a reusable educational tool for exploring compartmental epidemic models.

The repository includes:

- `sir_modeling.py` – reusable functions for running and visualizing SIR models
- `covid_sir_example.ipynb` – a worked example using real-world COVID-19 surveillance data from California
- `data/` – supporting COVID-19 and population datasets used in the example notebook

---

## Project Overview

The SIR model divides a population into three compartments:

- **Susceptible (S)** – individuals who can become infected
- **Infected (I)** – individuals who are currently infected
- **Recovered (R)** – individuals who have recovered and are assumed to be immune

The model describes how individuals move between these compartments over time using a system of ordinary differential equations.

This project demonstrates:

- Basic compartmental epidemic modeling
- Numerical solution of differential equations using SciPy
- Data preparation and transformation using Pandas
- Visualization of epidemic dynamics with Matplotlib
- Construction of SIR model inputs from real-world surveillance data

---

## Repository Structure

```text
.
├── README.md
├── sir_modeling.py
├── covid_sir_example.ipynb
└── data/
    ├── covid_cases_by_state_archived.csv
    └── state_population_estimates.xlsx
```

---

## Example Usage

```python
import sir_modeling as sir

initial_conditions = sir.calculate_initial_conditions(
    susceptible=990,
    infected=10,
    recovered=0
)

t, results = sir.run_sir_model(
    initial_conditions=initial_conditions,
    beta=0.3,
    gamma=0.1,
    days=160
)

sir.plot_sir_model(
    t,
    results,
    title="Example SIR Simulation"
)
```

---

## Example Notebook

The notebook `covid_sir_example.ipynb` demonstrates how the module can be applied to a real-world dataset.

The workflow includes:

1. Loading COVID-19 surveillance data from the CDC
2. Loading annual population estimates from the U.S. Census Bureau
3. Estimating susceptible, infected, and recovered populations
4. Running SIR simulations for California in 2020, 2021, and 2022
5. Comparing epidemic dynamics across years
6. Performing sensitivity analysis on model parameters

The notebook is intended as an educational example rather than an epidemiological forecasting tool.

---

## Data Sources

### COVID-19 Surveillance Data

Centers for Disease Control and Prevention (CDC)

*United States COVID-19 Cases and Deaths by State Over Time*

### Population Estimates

United States Census Bureau

*Population Estimates Program*

---

## Limitations

This project is intended for educational purposes and makes several simplifying assumptions:

- Active infections are estimated using a 14-day rolling case window
- Recovered individuals are estimated indirectly from cumulative case counts
- Transmission and recovery rates are assumed constant during simulations
- Vaccination, reinfection, demographic heterogeneity, and geographic variation are not explicitly modeled

Consequently, the simulations should be interpreted as demonstrations of the SIR framework rather than epidemiological forecasts.

---

## Future Improvements

Potential extensions include:

- SEIR and other compartmental models
- Time-varying transmission and recovery parameters
- Parameter estimation from observed data
- Model calibration and validation
- Interactive visualizations and dashboards

---

## Acknowledgment

This project was originally developed as a final project for **COGS 18: Introduction to Python** at the **University of California, San Diego**, and was later refactored and expanded into its current form.

---

## License

This project is provided for educational and research purposes.
