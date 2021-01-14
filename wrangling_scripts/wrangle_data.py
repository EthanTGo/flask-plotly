import pandas as pd
import plotly.graph_objs as go


# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    data = pd.read_csv('data/vgsales.csv')
    
    df_one = data[data.Platform == 'DS']
    df_one = df_one.groupby('Year')['Global_Sales'].sum()
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = list(df_one.index[1:]),
      y = list(df_one.values[1:]),
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Nintendo DS Games Sales <br> From 2004 onwards',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Global Sales (Millions)'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Bar(
      x = list(data['Platform'].value_counts().index),
      y = list(data['Platform'].value_counts().values),
      )
    )

    layout_two = dict(title = 'Number of Games per Platform',
                xaxis = dict(title = 'Company',),
                yaxis = dict(title = 'Number of Games'),
                font=dict(
                    family="Courier New, monospace",
                    size=10
                )     
            )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    df3 = data[data.Publisher == 'Nintendo']
    df3 = df3.groupby('Year')['Global_Sales'].sum()
    graph_three.append(
      go.Scatter(
      x = list(df3.index),
      y = list(df3.values),
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Overall Nintendo Sales <br> throughout the years',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures

return_figures()