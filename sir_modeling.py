import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def calculate_initial_conditions(susceptible, infected, recovered, scale=True):
    """
    Calculate initial SIR conditions.

    Parameters:
    ==========
    susceptible: int or float
        Number of susceptible individuals.
    infected: int or float
        Number of infected individuals.
    recovered: int or float
        Number of recovered individuals.
    scale: bool, default=True
        If True, return proportions. If False, return raw counts.
    
    Returns:
    =========
    list
        Initial SIR values as [S, I, R].
    """

    total_population = susceptible + infected + recovered 

    if total_population <= 0:
        raise ValueError("Total population must be greater than zero (0).")
    if min(susceptible, infected, recovered) < 0:
        raise ValueError("Susceptible (S), infected (I), and recovered (R) counts must be non-negative.")
    if scale:
        return [susceptible / total_population, 
                infected / total_population, 
                recovered / total_population,]
    
    return [susceptible, infected, recovered]

def sir_derivatives(y, t, beta, gamma):
    """
    Calculate derivatives for the SIR model.

    Parameters:
    ==========
    y: list
        Current values [S, I, R].
    t: float
        Current time step. (Required by odeint.)
    beta: float
        Transmission/infection rate.
    gamma: float
        Recovery rate.
    
    Returns:
    =========
    list
        Derivatives [dS/dt, dI/dt, dR/dt].
    """

    s, i, r = y

    dsdt = -beta * s * i
    didt = beta * s * i - gamma * i
    drdt = gamma * i

    return [dsdt, didt, drdt]

def run_sir_model(initial_conditions, beta, gamma, days=160, points=1000):
    """
    Run a basic SIR model simulation.

    Parameters:
    ==========
    initial_conditions: list
        Initial SIR values as [S, I, R].
    beta: float
        Transmission/infection rate.
    gamma: float
        Recovery rate.
    days: int, default=160
        Total number of days to simulate.
    points: int, default=1000
        Number of time points in the simulation.
    
    Returns:
    =========
    tuple
        Time points and SIR values as (t, S, I, R).
    """

    if beta < 0:
        raise ValueError("Transmission/infection rate (beta) must be non-negative.")
    if gamma < 0:
        raise ValueError("Recovery rate (gamma) must be non-negative.")
    if days <= 0:
        raise ValueError("Number of days to simulate must be greater than zero (0).")
    if points <= 1:
        raise ValueError("Number of time points must be greater than one (1).")
    
    t = np.linspace(0, days, points)
    results = odeint(
        sir_derivatives, 
        initial_conditions, 
        t, 
        args=(beta, gamma),
    )

    return t, results

def plot_sir_model(t, results, title="SIR Model", show=True):
    """
    Plot SIR model results.

    Parameters:
    ==========
    t: array-like
        Time points.
    results: array-like
        SIR model output with columns [S, I, R].
    title: str, default="SIR Model"
        Title for the plot.
    show: bool, default=True
        If True, display the plot.
    
    Returns:
    =========
    matplotlib.axes.Axes
        The plot axes.
    """

    s = results[:, 0]
    i = results[:, 1]  
    r = results[:, 2]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(t, s, label="Susceptible (S)", color="blue")
    ax.plot(t, i, label="Infected (I)", color="red")
    ax.plot(t, r, label="Recovered (R)", color="green")

    ax.set_title(title)
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Proportion of Population")
    ax.legend()
    ax.grid(True, alpha=0.3)

    if show:
        plt.show()
    
    return ax