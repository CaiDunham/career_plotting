# career_plotting
A python script utilizing matplotlib for creating Gantt Charts forms of Career History.


Listing out long form details of job history in resumes and portfolios can be exhausting, and tedious for recruiters to search through.
As a mitigation, I've created this project to plot an individual's career history in an easy to read Gantt Chart.


Currently, the script is simple and the logic is as follows:

    1. Define a Pandas DataFrame from a set dictionary with Series: 
              'work_start' = beginning of job
              'work_end'   = end of job
              'work_job'   = Title of Posistion
              'jobID'      = simplified string assigned to each instance for easy calling
              
    2. Convert input dates for 'work_start' and 'work_end' to datetime datatypes
    
    3. Plot horizontal bar chart using Matplotlib, offsetting ranges to correlate with 
       'work_start' and 'work_end' dates.
       
    4. Lots of formatting to make the chart enjoyable to read.
    
    
This is just the basic form of the chart. Functions under construction for the next revision include:


     1. Mouseover Event functions that will display details of each job when hovered over on the chart.
  
     2. GUI (tkinter) for inputting job history to increase program accessability.
     
     3. Connection options to portfolio's hosted on websites or apps such as Anvil.works
     
    
