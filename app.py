import streamlit as st
import scipy.stats
import time

# Header
st.header('Tossing a Coin')

# Slider for number of trials
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)

# Button to start the experiment
start_button = st.button('Run')

# Initialize the chart
chart = st.line_chart([0.5])

# Function to simulate coin tosses
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# Run the experiment if the button is clicked
if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    mean = toss_coin(number_of_trials)
    st.write(f'Final mean outcome: {mean}')