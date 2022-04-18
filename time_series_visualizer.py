import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =pd.read_csv("fcc-forum-pageviews.csv")
df.date=pd.to_datetime(df.date)


# Clean data
df =df[(df["value"]>=df["value"].quantile(0.025))&
(df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots(figsize=(21,7))
    ax.plot(df,"r")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    




    # Save image and return fig (don't change this part)
    fig.figure.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy()
    df_bar["Year"]=df["date"].dt.year
    df_bar["Month"]=df["date"].dt.month
    df_bar_ave=df_bar.groupby(["Year","Month"]).mean().unstack()

    # draw multiindex bar plot
    fig = df_bar_ave.plot(kind='bar',figsize=(5,5)).figure
    plt.title("Average daily page views, by Month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(fontsize = 10, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    df_box["month"]=pd.Categorical(df_box["month"], categories=month_order,ordered=True)
    df_box["year"]
  
    fig,axes=plt.subplots(1,2,figsize=(21,7))
    sns.boxplot(data=df_box,x="year",
                  y="value",ax=axes[0],orient="v")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")


    sns.boxplot(data=df_box,x="month",
                y="value",ax=axes[1],orient="v")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
