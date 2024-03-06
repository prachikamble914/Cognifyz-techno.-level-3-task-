import pandas as pd
import plotly.express as px

def visualize_data(dataset_path):
    df=pd.read_csv(dataset_path)
    fig=px.scatter(df,x='X-axis_column',y='Y-axis_column',color='Category_column',size='Size_column', hover_data=['Additional_info_column'],
                   title='Interactive Scatter Plot')
    fig.show()
    if __name__ == "__main__":
        dataset_path = 'path/to/your/dataset.csv'
        visualize_data(dataset_path)