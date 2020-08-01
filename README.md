# Statistical Analysis Functions (Python)
A collection of statistical analysis functions to make the Exploratory Data Analysis (EDA) and advanced statistical analysis workflow smoother.

# Chapter 1: Graphical Exploratory Data Analysis (EDA)

Before diving into sophisticated statistical inference techniques, you should first explore your data by plotting them and computing simple summary statistics. This process, called exploratory data analysis, is a crucial first step in statistical analysis of data.

# 1. Histograms (Binning Bias)

Making a Histogram:

Using Matplotlib:

import matplotlib.pyplot as plt

## We can pass a df’s column or a numpy array with the same data.

_ = plt.hist(df[‘column_name’])
_ = plt.xlabel(’name_xaxis’)
_ = plt.ylabel(’name_yaxis')

plt.show()
