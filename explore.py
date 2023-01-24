import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

def plot_q1(train):
    '''this function plots the scatter plot for tax value and house sqft'''
    # columns    
    x = ['tax_value']
    y = ['house_sqft']
    
    sns.lmplot(x='tax_value', y='house_sqft', data=train.sample(1000), scatter=True, line_kws={'color': 'red'})
    plt.title('House SQFT Vs Tax Value')
    plt.show()
    
def plot_q2(train):
    '''this function plot the violin plot for tax value and bathrooms'''
    # plot 
    sns.violinplot(x='bathrooms', y='tax_value', data=train.sample(1000))
    plt.title('Does the number of bathrooms affect tax value?')
    plt.show()    
    
def plot_q3(train):
    '''this function plots the scatter plot for tax value and lot size'''
    # columns    
    x = ['tax_value']
    y = ['lot_size_sqft']
    
    sns.lmplot(x='tax_value', y='house_sqft', data=train.sample(1000), scatter=True, line_kws={'color': 'red'})
    plt.title('Lot Size SQFT Vs Tax Value')
    plt.show()
    
def plot_q4(train):
    '''this function plots the scatter plot for tax value and bedrooms'''
    # plot 
    plt.figure(figsize = (15,5))
    sns.barplot(x='bedrooms', y='tax_value', data=train.sample(500))
    plt.title('Bedrooms vs Tax Value')
    plt.show()
    
    
def q2_stats_test(train):
    
    '''a function which takes in a train data set and calculates and returns a
       pearsons r test for bathrooms and tax value'''
    
    # setting alpha
    a = 0.05
    
    # performing a t test
    corr, p = stats.pearsonr(train.bedrooms, train.tax_value)
    corr, p

    # if statement to return our results
    if p > a:
        print("We fail to reject null hypothesis")
    else:
        print("We reject the null hypothesis, there is correlation")
        
    print(f"correlation: {corr}")
    print(f"p:           {p}")
    
    
def q4_stats_test(train):
    
    '''a function which takes in a train data set and calculates and returns a
       pearsons r test for bedrooms and tax value'''
    
    # setting alpha
    a = 0.05
    
    # performing a t test
    corr, p = stats.pearsonr(train.bedrooms, train.tax_value)
    corr, p

    # if statement to return our results
    if p > a:
        print("We fail to reject null hypothesis")
    else:
        print("We reject the null hypothesis, there is correlation")
        
    print(f"correlation: {corr}")
    print(f"p:           {p}")
    

def q1_stats_test(train):
    
    '''a function which takes in a train data set and calculates and returns a
       pearsons r test for house sqft and tax value'''
    
    # setting alpha
    a = 0.05
    
    # performing a t test
    corr, p = stats.pearsonr(train.house_sqft, train.tax_value)
    corr, p

    # if statement to return our results
    if p > a:
        print("We fail to reject null hypothesis")
    else:
        print("We reject the null hypothesis, there is correlation")
        
    print(f"correlation: {corr}")
    print(f"p:           {p}")