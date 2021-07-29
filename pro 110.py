import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import plotly.express as px


df=pd.read_csv("medium_data.csv") #reading the file
data= df["temp"].tolist() #converting to list

# fig= ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()

population_mean=statistics.mean(data) #rando name
std_dev=statistics.stdev(data)
print(f"Population mean: {population_mean}")
print(f"Standard Deviation: {std_dev}")

def show_fig(mean_list):
    df=mean_list #data is now mean_list
    mean=statistics.mean(df) #mean
    fig=ff.create_distplot([df],["temp"],show_hist=False) #creating dist_plot
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))#adding trace line
    fig.show()



dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)

print(f"Mean of sample: {mean}")
print(f"Standard Deviation of sample: {std_deviation} ")

def random_set_mean(counter):
    dataset=[]
    for i in range(0,counter): #counter u can put--> check line 52
     random_index=random.randint(0,len(data)-1)
     value=data[random_index]
     dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_mean(30) #taking 100 rando values from 1000 to see the mean
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print(f"Mean of sampling distribution: {mean}")

setup()


def standard_dev(): #gives std_dev
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_mean(100)
        mean_list.append(set_of_means)
    std_devi=statistics.stdev(mean_list)
    print(f"Standard deviation of sampling distribution: {std_devi}")

standard_dev()