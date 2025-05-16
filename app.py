import streamlit as st
import scipy.stats
import pandas as pd
import time
import math
# Updated app script
# Header
st.title("Coin Toss Simulation")
st.write("Simulate tossing a coin multiple times and observe the mean outcome over trials.")

# Sidebar for user inputs
st.sidebar.header("Simulation Settings")
number_of_trials = st.sidebar.slider("Number of trials", 1, 1000, 10)
start_button = st.sidebar.button("Run Simulation")

# Initialize session state for results
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0
if "df_experiment_results" not in st.session_state:
    st.session_state["df_experiment_results"] = pd.DataFrame(columns=["Experiment", "Trials", "Mean Outcome"])

# Function to simulate coin tosses
@st.cache_data
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    cumulative_mean = []
    outcome_1_count = 0

    for i, outcome in enumerate(trial_outcomes, start=1):
        outcome_1_count += outcome
        cumulative_mean.append(outcome_1_count / i)

    return cumulative_mean

# Run the simulation
if start_button:
    st.session_state["experiment_no"] += 1
    st.write(f"Running {number_of_trials} trials...")
    progress = st.progress(0)

    # Simulate coin tosses
    cumulative_mean = toss_coin(number_of_trials)
    for i in range(len(cumulative_mean)):
        progress.progress((i + 1) / number_of_trials)

    # Update results
    final_mean = cumulative_mean[-1]
    st.session_state["df_experiment_results"] = pd.concat(
        [
            st.session_state["df_experiment_results"],
            pd.DataFrame(
                [[st.session_state["experiment_no"], number_of_trials, final_mean]],
                columns=["Experiment", "Trials", "Mean Outcome"],
            ),
        ],
        ignore_index=True,
    )

    # Display results
    st.line_chart(cumulative_mean)
    st.write(f"Final Mean Outcome: {final_mean:.4f}")

# Display past results
st.header("Experiment Results")
st.dataframe(st.session_state["df_experiment_results"])

import math


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """Holds all the main logic."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
