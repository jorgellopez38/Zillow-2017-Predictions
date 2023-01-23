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
    
    '''this function which takes in a train data set and calculates and returns a specific 
       t-test for the mean of bathroom data'''
    
    # setting alpha
    a = 0.05
    # creating a mean of bathrooms
    avg_bath = train['bathrooms'].mean()
    
    # using the mean to create mask data frames on either side
    above_bath = train[train.bathrooms >avg_bath].bathrooms
    below_bath = train[train.bathrooms <= avg_bath].bathrooms
    
    # performing a t test
    t, p = stats.ttest_ind(above_bath, below_bath, equal_var=False)

    # if statement to return our results
    if p / 2 > a:
        print("We fail to reject null hypothesis")
    elif t < 0:
        print("We fail to reject null hypothesis")
    else:
        print("We reject the null hypothesis")
        
    print(f"t: {t}")
    print(f"p: {p}")
    
def q4_stats_test(train):
    '''this function which takes in a train data set and calculates and returns a specific 
       t-test for the mean of bedroom data'''
    a = 0.05
    # creating an average metric of bedroom count
    avg_bed = train['bedrooms'].mean()
    
    # creating a mask for a new data frame
    abov_bed_sample = train[train.bedrooms > avg_bed].bedrooms
    
    # perform a t test
    t, p = stats.ttest_1samp(abov_bed_sample , avg_bed)
    
    # if statement to return our results
    if p > a:
        print('We fail to reject null hypothesis: There is not a significant difference in the mean')
    else:
        print("We reject null hypothesis: There is some significant difference in the mean")
        
    print(f"t: {t}")
    print(f"p: {p}")

def q1_stats_test(train):
    
    '''a function which takes in a train data set and calculates and returns a specific 
       t-test for the mean of house sqft data'''
    
    # setting alpha
    a = 0.05
    # creating a mean of house sqft
    avg_house_sqft = train['house_sqft'].mean()
    
    # using the mean to create mask data frames on either side
    above_house_sqft = train[train.house_sqft >avg_house_sqft].house_sqft
    below_house_sqft = train[train.house_sqft <= avg_house_sqft].house_sqft
    
    # performing a t test
    t, p = stats.ttest_ind(above_house_sqft, below_house_sqft, equal_var=False)

    # if statement to return our results
    if p / 2 > a:
        print("We fail to reject null hypothesis")
    elif t < 0:
        print("We fail to reject null hypothesis")
    else:
        print("We reject the null hypothesis")
        
    print(f"t: {t}")
    print(f"p: {p}")