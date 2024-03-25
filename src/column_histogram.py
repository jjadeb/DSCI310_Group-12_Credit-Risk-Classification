import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class EmptyDataFrameError(ValueError):
    '''raise this when there is an empty DataFrame passed to the function'''

class NumericColumnError(TypeError):
    '''raise this when the column of interest for the histogram is not numeric'''

def column_histogram(fig_width, fig_height, data_frame, column_name):
    """
    Create a histogram for a numerical column in a dataframe.

    Parameters:
    ----------
    fig_width : int
        The width of the figure created
    fig_height : int
        The height of the figure created
    data_frame : pandas.DataFrame
        The input DataFrame containing the data to plot
    column_name : str
        The name of the numerical column in the DataFrame that we want to plot

    Returns:
    -------
    matplotlib.axes._axes.Axes
        A Matplotlib Axes object
        
    Examples:
    --------
    >>> import matplotlib.pyplot as plt
    >>> import seaborn as sns
    >>> data = pd.read_csv('mtcars.csv')  # Replace 'mtcars.csv' with your dataset file
    >>> column_plot = create_column_histogram(10,4,data,mpg) # Replace mpg with column of interest 
    >>> column_plot
    
    Notes:
    -----
    This function uses the matplotlib.pyplot and seaborn libraries to create the histogram plot.

    """

    if type(data_frame) != pd.core.frame.DataFrame:
        raise TypeError('DataFrame must be of type pandas.core.frame.DataFrame')
    
    if data_frame.empty:
        raise EmptyDataFrameError('DataFrame must contain a column with numeric values')

    if type(column_name) != str:
        raise TypeError('Column name must be of type string')

    if column_name not in data_frame.columns:
        raise KeyError('Column name must exist in the DataFrame')

    data_frame[column_name] = data_frame[column_name].infer_objects(copy=None) # making sure null values are considered numeric
    if column_name not in data_frame.select_dtypes(include=["float", 'int']).columns:
        raise NumericColumnError('DataFrame column must be numeric')

    if (type(fig_width) != int) | (type(fig_height) != int) | (fig_width  == 0) | (fig_height  == 0):
        raise TypeError('Width and height must be a non-zero integers')
    
    plt.figure(figsize=(fig_width, fig_height)) # create figure with given height and width
    sns.histplot(data_frame[column_name], kde=True) # plot numeric column data as a histogram
    plt.title(f'Histogram of {column_name}') # add title to histogram
    return plt.gca()

