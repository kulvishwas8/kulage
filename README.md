# kulAge
This application is an age-based asset allocation tool that calculates investment allocation solely from the user’s date of birth, assuming a maximum age of 85 years. It is implemented in Python using NumPy, pandas, Plotly, and Streamlit for an interactive web-based interface.

## Overview

This project helps users quickly derive a suggested asset mix based on their current age, following the common principle that risk exposure should decrease as age increases. The core output is a set of age-dependent allocation percentages (for example, equity vs. debt) visualized and served through a Streamlit app.
## Core Logic

The only required input is the user’s date of birth, from which the current age is computed using today’s date, capped at a maximum of 85 years for allocation purposes. The allocation logic is age-based and  follow simple heuristics such as “rule of 100” style formulas with modification where the equity proportion is derived from age and the remainder is assigned to lower-risk assets.

## Technology Stack

The backend is written in Python and relies on NumPy for numerical calculations and vectorized age and allocation computations. Pandas is used to structure intermediate data (such as age bands and corresponding allocations), and Plotly generates interactive allocation charts that are embedded in the Streamlit interface.

## Frontend and User Flow

Streamlit provides the entire user interface, including input widgets for date of birth, buttons to trigger calculations, and sections to display cards and charts of the computed asset allocation. Once the user enters a valid date of birth, the app calculates age in real time, applies the allocation logic, and renders interactive Plotly visualizations and summary cards.

## Intended Use and Limitations

This tool is designed as an educational or exploratory aid to illustrate how asset allocation can change with age, not as personalized financial advice. The logic does not consider risk tolerance, goals, income, or other financial factors and assumes ages beyond 85 map to the same “max age” allocation profile.


