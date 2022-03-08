###plotting locally to avoid paying $15/month


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates


#making individual function for ease of callable in future uses (websites, anvil)
def plot_career():

    #colorPallete
    colo_baseA = '#F6D7A7'          
    colo_baseB = '#F6EABE'      
    colo_accA  = '#C8E3D4'
    colo_accB  = '#87AAAA'

    def color(row):
        colrDict = {'jobA':colo_accA, 'colg':colo_accB, 'jobB':colo_accA, 'jobC':colo_accB, \
                    'jobD':colo_accA, 'jobE':colo_accB}
        return colrDict[row['jobID']]
    

    #making dataframe with career table values to play with locally
    cDict = {'work_start': ['6/3/2015', '9/25/2015', '6/12/2016', '5/13/2017', '6/11/2018', '6/1/2019'], \
             'work_end': ['9/16/2015', '6/4/2019', '9/18/2016', '9/16/2018', '6/1/2019', '3/3/2022'], \
             'work_job': ['Ranch Intern', 'College', 'R&D Intern', 'Line Crew, Customer Service, Operations', \
                          'Engineering Intern', 'Design Engineer, Product Development'], \
             'jobID': ['jobA', 'colg', 'jobB', 'jobC', 'jobD', 'jobE'],}

    df = pd.DataFrame(data = cDict)



    #making date types
    df['work_start'] = pd.to_datetime(df['work_start'])
    df['work_end'] = pd.to_datetime(df['work_end'])

    

    #time from start to end of job
    df['start_to_end'] = df['work_end'] - df['work_start']

    #adding colors
    df['colors'] = df.apply(color, axis=1)



    print(df)

    #plotting------------------------------------
    #setup
    fig, ax = plt.subplots(1, figsize=(12,6))
    fig.set_facecolor(colo_baseB)

    height = 0.4
    
    #defining data
    ax.barh(df['work_job'], df['start_to_end'], height = 0.4, left=df['work_start'], \
            color=df['colors'])

    #setting up x axis labeling
    ax.set_xticks(df['work_start'])
    ax.set_xticklabels(df['work_start'], color='#5B5B5B')
    dateForm = mdates.DateFormatter("%m-%Y")
    ax.xaxis.set_major_formatter(dateForm)
    plt.xticks(rotation=45)
    ax.xaxis.grid(color=colo_baseA, linestyle='--', linewidth=1)
    ax.set_axisbelow(True)
    ax.spines['bottom'].set_color('#5B5B5B')


    #put job names in front of bars
    for jobName, row in df.iterrows():
        ax.text(row['work_start'] - pd.DateOffset(30), jobName, row['work_job'], \
                va='center', ha='right', fontstretch='condensed', color='#5B5B5B')

    #getting rid of y axis labels
    ax.set_yticks([])
    ax.set_yticklabels([])

    #removing ugly borders
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)

    #add some pop-pop!
    ax.set_facecolor(colo_baseB)

    plt.show()
    #plt.savefig('careerChart.png')

    
    

    
                          


#run fuction locally
plot_career()
