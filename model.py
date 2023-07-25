import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

def find_song_peaks(id, title):
    milk_data = pd.read_csv("./audio_files/" + id + '.csv')
    time_series = milk_data['heat_score']

    indices = find_peaks(time_series, distance=15, prominence=0.1)[0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=time_series,
        mode='lines+markers',
        name='Original Plot'
    ))

    fig.add_trace(go.Scatter(
        x=indices,
        y=[time_series[j] for j in indices],
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            symbol='cross'
        ),
        name='Detected Peaks'
    ))

    # fig.show()

    new_indices = []
    for i in indices: 
        new_indices.append(milk_data['time'][i])

    return new_indices

