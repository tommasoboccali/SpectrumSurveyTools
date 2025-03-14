import csv
import pprint 


def slicer(theSurvey, theQuestion, theAnswers):

    #returns only the part of the survey whse lines match question = one of the answers
    # theSurvey is the list of dictionaries
    # theQuestion is the key of the dictionary to be matched
    # theAnswers is a list of strings to be matched

    slicedSurvey=[]
    for row in theSurvey:
        #print ("ANSWER",row[theQuestion],row[theQuestion].split('; ') )
        answers = row[theQuestion].split('; ')
        #print ("the answers in this row",answers)
        for a in theAnswers:
            if a  in answers:
                slicedSurvey.append(row)
                #print ("MATCHED")


    print ("Slicing returned ",len(slicedSurvey)," entries", "out of ",len(theSurvey))
    return slicedSurvey


def printList(theSurvey,plot):
    print ("=====Printing list for ", plot)
    for i in theSurvey:
        if i[plot] !="":
         print (i[plot])



def dictforbar(theSlicedSurvey, theString):
    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
            answer = i[stringQ]
#            if answer == "":
                #print ("EMPTY ANSWER", i['\ufeffYour name'])
#        print ('Answer:',answer)
            answers = answer.split('; ')
#        print (answers)
            for j in answers:
 #           print (j)
                if j in plotdict.keys():
                    plotdict[j]=plotdict[j]+1
                else:
                    plotdict[j]=1

    if "" in plotdict.keys():
        del plotdict['']
#    print ("DICT for the PLOT using Query:",stringQ, "\n",plotdict)     
    return plotdict


def dictforpie(theSlicedSurvey, theString):
    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
        answer = i[stringQ]
    #    print ('Answer:',answer)
        answers = answer.split('; ')
        for j in answers:
 #           print (j)
            if j in plotdict.keys():
                plotdict[j]=plotdict[j]+1
            else:
                plotdict[j]=1

    if "" in plotdict.keys():
 #       plotdict['N/A']=plotdict['']
        del plotdict['']
#    print ("DICT for the PLOT Using Query:",stringQ, "\n", plotdict)      
    return plotdict

def textforwcl(theSlicedSurvey, theString):
    stringQ = theString

    text = ""

    for i in theSlicedSurvey:
        answer = i[stringQ]
        text = text + " "+ str(answer)
    
#    print ("TEXT for the WORDCLOUD using Query",stringQ,"\n",text)      
    return text

def vectforhist(theSlicedSurvey, theString):
    stringQ = theString
    histvect=[]
    
    for i in theSlicedSurvey:
        answer = i[stringQ]
        histvect.append(answer)
    return histvect
        

def dictfortable(theSlicedSurvey, theString):
    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
            answer = i[stringQ]
#            if answer == "":
#
#        print ('Answer:',answer)
            answers = answer.split('; ')
#        print (answers)
            for j in answers:
 #           print (j)
                if j in plotdict.keys():
                    plotdict[j]=plotdict[j]+1
                else:
                    plotdict[j]=1

    if "" in plotdict.keys():
#        plotdict['N/A']=plotdict['']
        del plotdict['']
    print ("DICT for the TABLE using Query:",stringQ, "\n",plotdict)     
    return plotdict


def histogram(theSlicedSurvey, theString):
                
        import matplotlib.pyplot as plt
        import numpy as np
    
        # 1 - 'What is the team size (in number of collaborators) of the initiative?'
    
        histvect = vectforhist(theSlicedSurvey, theString)

        #plt.hist([float(plotdict[v]) for v in plotdict], bins=range(0, 100, 10), alpha=0.75)
        print (histvect)
        plt.hist(histvect,bins=10)
        plt.xticks(rotation=30, ha='right')

        plt.title(theString)
    
        plt.show() 
    
        return

def pieplot(theSlicedSurvey, theString):
            
    import matplotlib.pyplot as plt
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    plotdict=dictforpie(theSlicedSurvey, theString)

    plt.pie([float(plotdict[v]) for v in plotdict], labels=[str(k) for k in plotdict], autopct='%1.1f%%')
    plt.title(theString)

    plt.show() 

    return


def barplot(theSlicedSurvey, theString):
            
    import matplotlib.pyplot as plt
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    plotdict=dictforbar(theSlicedSurvey, theString)
    print ("DICT for the PLOT using Query:",theString, "\n",plotdict)     

    plt.figure(figsize=(10, 30))
    plt.bar(*zip(*plotdict.items()))
    plt.title(theString)
    plt.xticks(rotation=30, ha='right')

    plt.show() 

    return

def tableplot3(theSliceAll,theSlicedSurvey1, theSlicedSurvey2, theString, titleall, title1, title2):
    import plotly.graph_objects as go

    utabdictall = dictfortable(theSliceAll,theString)
    utabdict1 = dictfortable(theSlicedSurvey1,theString)
    utabdict2 = dictfortable(theSlicedSurvey2,theString)
    
    tabdictall = {key: value for key, value in sorted(utabdictall.items())}
    tabdict1 = {key: value for key, value in sorted(utabdict1.items())}
    tabdict2 = {key: value for key, value in sorted(utabdict2.items())}
    

    from plotly.subplots import make_subplots

    limits = [100,35,35]

    fig = make_subplots(
        rows=1, 
        cols=3,
        start_cell="top-left", 
        specs=[
            [{"type": "table"}, {"type": "table"}, {"type": "table"}    ]
            
        ]
    )

    x = [key for key in tabdictall.keys()]
    y = [value for value in tabdictall.values()]


    tot=0
    for i in y:
        tot+=i
    f = [str(round(100*i/tot,1))+"%" for i in y]
    x.append("Total")
    y.append(tot)
    f.append("100%")


    fig.add_trace(go.Table(columnwidth=limits,header=                           
        dict(values=[titleall+": "+theString, 'Answers', 'Fraction (%)']),
        cells=dict(values=[x,y,f])
    ),row=1, col=1)

#fig 2

    x = [key for key in tabdict1.keys()]
    y = [value for value in tabdict1.values()]

    tot=0
    for i in y:
        tot+=i
    f = [str(round(100*i/tot,1))+"%" for i in y]
    x.append("Total")
    y.append(tot)
    f.append("100%")


    fig.add_trace(go.Table(columnwidth=limits,header=                           
        dict(values=[title1+": "+theString, 'Answers', 'Fraction (%)']),
                 cells=dict(values=[x,y,f])
    ),row=1, col=2)

#fig 3

    x = [key for key in tabdict2.keys()]
    y = [value for value in tabdict2.values()]

    tot=0
    for i in y:
        tot+=i
    f = [str(round(100*i/tot,1))+"%" for i in y]
    x.append("Total")
    y.append(tot)
    f.append("100%")


    fig.add_trace(go.Table(columnwidth=limits,header=                           
        dict(values=[title2+": "+theString, 'Answers', 'Fraction (%)']),
                 cells=dict(values=[x,y,f])
    ),row=1, col=3)

    fig.show()


def tableplot(theSlicedSurvey, theString):
    import plotly.graph_objects as go

    tabdict = dictfortable(theSurvey,theString)


    headerline=list(tabdict.keys())
    cellsline=list(tabdict.values())
    tot=0
    for i in cellsline:
        tot+=i
    fractions = [str(round(100*i/tot,1))+"%" for i in cellsline]
    headerline.append("Total")
    cellsline.append(tot)
    fractions.append("100%")

    print ("CHECK",headerline, cellsline)
    limits = [100,35,35]
    fig = go.Figure(data=[go.Table(columnwidth=limits,header=                           
        dict(values=[theString, 'Answers', 'Fraction (%)']),
                 cells=dict(values=[headerline,cellsline,fractions])
    )])
    fig.show()

def extract_speed_info(item,unit_order):
    # Check for a recognized unit
    import re
    for unit in unit_order:
        if unit in item:
            # Extract numeric parts (handles ranges like '10-100' or '< 1')
            numbers = re.findall(r'\d+', item)
            # Return tuple (unit order, first number, second number if exists)
            return (unit_order[unit], int(numbers[0]) if numbers else 0, int(numbers[1]) if len(numbers) > 1 else 0)
    # If no unit is found, push it to the end
    return (99, 0, 0)



def extractBars(theSlicedSurvey, theString):
    import matplotlib.pyplot as plt
    import numpy as np
    import textwrap

    plotdict=dictforbar(theSlicedSurvey, theString)
    x = [key.replace('+', ',') for key in plotdict.keys()]   
    y = [value for value in plotdict.values()]
    #sort x and y on the y values
    #y, x = zip(*sorted(zip(y, x), reverse=True))

    unit_order = {'MB': 1, 'GB': 2, 'TB': 3, "day": 4, "week": 5, "month": 6, "year": 7, "16 - 31": 8,"32 - 64": 9, "thousand":10, "million":11, "billion":12}

    sorted_pairs = sorted(zip(x, y), key=lambda pair: extract_speed_info(pair[0],unit_order),reverse=True)

# Unpack the sorted pairs
    a_sorted, b_sorted = zip(*sorted_pairs)

# Convert tuples back to lists
    x = list(a_sorted)
    y = list(b_sorted)




    y_norm = [value/sum(y) for value in y]
    wrapped_x = [ "\n".join(textwrap.wrap(label, width=25)) for label in x ]

    print("BARH")
    print (wrapped_x)
    print (y)
    print (y_norm)
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.barh(wrapped_x, y, color='skyblue')
    total = sum(y)
    tit = theString.replace('+', ',')

# Add annotations for the relative fraction
    for bar, fraction in zip(bars, y_norm):
        width = bar.get_width()
    #    ax.text(bar.get_width() +  total * 0.02,
    #        bar.get_y() + bar.get_height() / 2, 
    #        f"{fraction:.1%}", 
    #        va='center', ha='left', fontsize=12, color='black')
        ax.text(width * 0.5,
            bar.get_y() + bar.get_height()/2,
            f"{fraction:.1%}",
            va='center', ha='center', fontsize=14, color='black', fontweight='bold')
    ax.tick_params(axis='y', labelsize=14)

    ax.set_xlabel('Entries')
    w_title = "\n".join(textwrap.wrap(tit, width=60))
    #ax.set_title(w_title)
    ax.set_title(w_title, fontsize=14, fontweight='bold')
    ax.set_xlim(0, max(y) * 1.1)

    plt.tight_layout()
    plt.show()


def barplot2(theSlicedSurvey, theString):
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    plotdict=dictforbar(theSlicedSurvey, theString)
    print ("DICT for the PLOT using Query:",theString, "\n",plotdict)     

    x = [key for key in plotdict.keys()]   
    y = [value for value in plotdict.values()]


    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(        
        go.Bar(x=x, y=y),
        row=1, col=1
    )


    fig.update_layout(height=600, width=800, title_text=(theString))
    fig.update_xaxes(       
        tickangle = 45)
    fig.show()

    return

def barplot2Slices(theSlicedSurvey1, theSlicedSurvey2, theString, title1, title2):
            
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    plotdict1=dictforbar(theSlicedSurvey1, theString)
    plotdict2=dictforbar(theSlicedSurvey2, theString)

    fig = make_subplots(rows=1, cols=2)

    x = [key for key in plotdict1.keys()]
    y = [value for value in plotdict1.values()]

    fig.add_trace(        
        go.Bar(x=x, y=y),
        row=1, col=1
    )

    x2 = [key for key in plotdict2.keys()]   
    y2 = [value for value in plotdict2.values()]

    fig.add_trace(
        go.Bar(x=x2, y=y2),
        row=1, col=2
    )

    fig.update_layout(height=600, width=800, title_text=(title1+" vs "+title2))
    fig.update_xaxes(       
        tickangle = 45)
    fig.show()

    return

def barplot3Slices(theSliceAll,theSlicedSurvey1, theSlicedSurvey2, theString, titleall, title1, title2):
            
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    plotdictall=dictforbar(theSliceAll, theString)
    plotdict1=dictforbar(theSlicedSurvey1, theString)
    plotdict2=dictforbar(theSlicedSurvey2, theString)

    fig = make_subplots(rows=1, cols=3)


    x = [key for key in plotdictall.keys()]
    y = [value for value in plotdictall.values()]

    fig.add_trace(        
        go.Bar(x=x, y=y, name=titleall),
        row=1, col=1
    )



    x = [key for key in plotdict1.keys()]
    y = [value for value in plotdict1.values()]

    fig.add_trace(        
        go.Bar(x=x, y=y, name=title1),
        row=1, col=2
    )

    x2 = [key for key in plotdict2.keys()]   
    y2 = [value for value in plotdict2.values()]

    fig.add_trace(
        go.Bar(x=x2, y=y2, name=title2),
        row=1, col=3
    )

    fig.update_layout(height=600, width=800, title_text=(titleall+" vs "+title1+" vs "+title2))
    fig.update_xaxes(       
        tickangle = 45)
    fig.show()

    return


def wclplot(theSlicedSurvey, theString):
    import matplotlib.pyplot as plt
    import numpy as np
    from wordcloud import WordCloud

    # 1 - 'Which are the categories which better describe your role(s)?'
    text=textforwcl(theSlicedSurvey, theString)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(theString)      
    plt.axis("off")

    plt.show() 

    return


###MAIN



#test to read the very large csv file
# note the file comes from the excel, after you have changed all the "," to a "+" and removed the first 3 lines
filename='/Users/tom/Downloads/Content_Export_SPECTRUM-JENA_Survey1_oct09/Export583072tab1CSV.csv'
filename='Export583072tab1CSV.csv'
#filename='Export2csv.csv'
#filename='/Users/tom/Downloads/Content_Export_SPECTRUM-JENA_Survey1_oct09/Export2csv.csv'
headerline=True
theSurvey=[]

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for row in reader:
        print ("ROW",row)
#        if row['Your name'] == "Tomm" or row['Your name'] == "test" or row['Your name'] == "ewrwe" or row['Your name'] == "dsadas":
#NEEDED FOR FIRST FILE
        if row['\ufeffYour name'] == "Tomm" or row['\ufeffYour name'] == "test" or row['\ufeffYour name'] == "ewrwe" or row['\ufeffYour name'] == "dsadas":

            continue
        theSurvey.append    (row)

print ("Finished reading the file, read  entries:"  + str(len(theSurvey)))       

# save it as json file
import json
#with open('survey.json', 'w') as f:
#    json.dump(theSurvey, f)
#print ("Finished writing the file")

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(theSurvey[0])
for i in theSurvey[0].keys():
    #print ("KEY",i)
    continue

#
# start doing easy plots
#

#tableplot(theSurvey,'Which are the categories which better describe your role(s)?')

#NEEDED FOR FIRST FILE
sliceRA = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Observational Radio Astronomy (RA)'])
sliceHEP = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Experimental High Energy Physics (HEP)'])

sliceAll = theSurvey


fullPlots = {
    'Which are the categories which better describe your role(s)?':'table',
    #'Describe in a few words what is your activity':"wcl",
    'Which is/are your scientific domain(s) of expertise (if applicable)?':"table",
    'On behalf of whom are you submitting the survey?':'pie',
    'Please select your areas of expertise+ for which you can answer technical questions:':'table',
    'Are you (ALSO) manager of an infrastructure? (computing centre+ a federated infrastructure+ a data centre+ ...)': 'pie',
    'Provide a short name for your initiative / use case / centre (for our indexing) (for example+ data analysis at ATLAS)': 'wcl',
}

fullPlots ={
    'Authentication and Authorization supported method(s) [this includes Workload and Storage management]':'table',
    'Technical solutions supported for AA':'table',
    'Which AA tools do you support or make use of?':'table',
}
fullPlots={
#        'Global CPU needs in core-hours per year (if you have the number in other units+ like node hours/year+ Teraflops/year+ ...+ please specify the unit)': 'list',
           'Global GPU needs in GPU hours per year (if you know the number in different units+ please specify)': 'list',
           'On which timescale are these needs evaluated / requested? (for example+ requests are submitted year by year+ every 5 years+ ...)':'pie',
           'Duration':'pie',
           'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'pie',
           'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'pie',
           'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'pie',
           'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'pie',
           
           
           }

#over .....

fullPlots = {'Do your processes require access to external (remote) services (data sources+ accounting+ monitoring+ management+. ..)?':'pie',
             'Please give it a short name (e.g. "reconstruction at CMS") for identification purposes':'wcl',
             'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'pie',
             'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'pie',
             'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'pie',
             'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'pie',
           }

fullPlots = {'Total expected volume to be handled (including everything: data from instruments+ simulations+ analysis samples) - in PB (PetaBytes)': 'list',
            'Please specify which formats are you using (for example+ CSV+ XLS+ ROOT+ HDF5+ FITS+ ...)' : 'wcl',
'How many total files / records are expected in your global storage systems?' : 'pie',
             'Do you handle data respecting FAIR Principles? (see for example here)' : 'pie',
             
             }





allhepraPlots = { 'Which facilities are you using?':'table',

#AAI

    'Typical computing access type': 'table',
    'Typical application type(s)': 'table',
    'Granularity of job submission': 'table',
    'Which is (are) the most common current resource allocation pattern(s)?': 'table',
    'Do you have a higher level Workload Management System (WMS:for example+ an initiative-specific layer handling a distributed computing infrastructure and interactive with lower level SLURM+ HTCondor or similar)?': 'table',
    'How do you discover available resources?': 'table',    
    'Access to data while the processes are executing': 'table',
    



#over .....
}

allhepraPlots = {            'Which low level protocols are you using for data ingestion / transfer / access?' : 'table',
                 'Typical storage solutions' : 'table',
    'Typical data structures'   : 'table',
    'Typical file / record size(s) - please note B = Byte' : 'table',
    'Typical file / record access patterns' : 'table',
                    'Which policies against data loss do you need?' : 'table',
             'Needs for data confidentiality / controlled access' : 'table',


}

fullPlots = {
             'Do you need public IPs on the compute nodes?' : 'pie',
             'If yes+ which is the typical fraction of the overall workflow which can be offloaded to accelerators in %? (for example+ in total fraction of operations or total fraction of the workflow time)': 'list',
                 'Do you need root access at any point when executing workflows on the compute nodes?' : 'pie',


}

allhepraPlots={
    'Supported base architectures' : 'table',
    'Supported operating systems' : 'table',
    'Do you need a local/shared disk to be used as area of work for the process (and scratched afterwards)?' : 'table',
    'Do you expect to need accelerators / special hardware?' : 'table',
    'Do you expect to need accelerators / special hardware?':'table',
    'How would you like to have software made available to you?':'table',
    'Do you need access to virtualization software?' : 'table',
    'Network needs on the computing node. Does the node need IP access to/from other nodes?' : 'table',
    'Do you need particular services to be deployed on special machines in the centre in order to operate? (edge services+ proxies+ connectors …)' : 'table',
    'Do you need X11/Wayland/VNC/… graphical access to the nodes?' : 'table',
   

}

fullPlots = {
#    'Do you rely on licensed tools (commercial compilers+ frameworks+ IDEs+ …) directly or as dependencies? List them' : 'wcl',
 'Do you have an agreed software licensing mode?':'pie',
    'Do you adopt FAIR for software principles? (see for example here)' : 'pie',
    'How is your initiative releasing software?' : 'pie',
    'Do you anticipate using other hardware architectures than today? Which ones?' : 'wcl',
    'How much will your software take advantage of multi-core processors?' : 'pie',
    'How much will you take advantage if vector/SIMD CPU registers?':'pie',
    'How much will you take advantage of GPUs/FPGAs?' : 'pie',
    'Do you have the resources needed to evolve your software as you will need to?' : 'pie',


}
allhepraPlots={
    'Which are the typical programming languages that you use in your initiative?':'table',
    'Please list the main software dependencies in your code'   : 'table',
    'CPU architectures' : 'table',
    'CPU vectorization' : 'table',
    'CPU vectorization' : 'table',
    'GPU Accelerator'   : 'table',
    'What is the driving force behind the architecture / accelerators decisions?' : 'table',
    'Do support heterogeneous computing? (executing software on different platforms+ possibly including accelerators)' : 'table',
    'Do you think that software performance will be an issue for you in the next decade?' : 'table',


    
    }

fullPlots = {
    'Do people enter your field with the right software skills? (for example+ at undergrad / PhD / PostDoc / Staff levels?)' : 'pie',
    'Do you feel researchers developing and maintaining software and managing the computing infrastructures receive appropriate recognition in your institution / initiative?' : 'pie',
}

allhepraPlots = {
    'Who designs and maintains the software in your initiative? (analysis+ reconstruction+ simulation+ ...)':'table',
    'Who designs and maintains the computing tools needed by your initiative? (operations+ monitoring+ accounting+ deployment+ WMS and data management+ ...)' : 'table',
    'On which categories could you get training?' : 'table',



}

fullPlots = {
    'Which type(s) of resources does your e-Infrastructure provide today?':'table',
                'Is the centre part of a larger e-infrastructure?':'table',
                'Which are the main mechanisms to get access to your infrastructure?' : 'table',
                'Do you allow users to deploy services on login / edge nodes?' : 'table',
                'Resource allocation methods' : 'table',
                'Which access patterns to the system you support?' : 'table',
                'How long are typical resource allocations? (project / grant length)' : 'table',
                'How long can the single processes be executed for?'    : 'table',
                'Which base system architecture is your centre supporting?' : 'table',
                'Which GPGPU architectures are you supporting?' : 'table',
                'Which is the typical # of physical cores you have per motherboard for the latest hardware procured (exclude HT)' : 'pie',
                'Which is the typical # of GPUs you have per motherboard for the latest hardware procured' : 'pie',
                'Which is the typical memory per core you deploy+ in GB? Please note 1 GB = 1 GigaByte' : 'table',
                'Do your nodes have a local “scratch disk” in GB per core? Please note 1 GB = 1 GigaByte' : 'pie',
                'Do you have system to system fast intercommunication (MPI+ …)?' : 'pie',
                'Which type of network connection(s) are available between storage nodes? Please note Gbps = GigaBits per second' : 'pie',
                'Which type of network connection(s) are available to sources / destinations outside the centre (WAN)? Please note Gbps = GigaBits per second' : 'pie',
                'Which type of network connection(s) are available between storage and compute nodes? Please note Gbps = GigaBits per second' : 'pue',
                'Which type(s) of resources does your e-Infrastructure provide today?' : 'pie',
                'Which routing options are available from your compute nodes? OUTGOING CONNECTIONS' : 'table',
                'Which routing options are available from your compute nodes? INCOMING CONNECTIONS' : 'table',
                'Does your centre use / support data management tools to move / access / manage data?' : 'table',
                'Specify the data management tool(s) your site uses and put a link to its documentation if available?': 'wcl',
                'How do you manage disk-based storage?' : 'table',
                'How do you manage tape-based storage?' : 'table',
                'Protocols to access the storage systems+ from internal hosts (for example compute nodes)':'table',
                'Protocols to access the storage systems+ from external hosts (for example storage to storage geographical transfers)' : 'table',
                'Which is the total aggregate capacity for writing to storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'pie',
                'Which is the total aggregate capacity for reading from storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'pie',
                'Which of the following features do you support?' : 'table',
                'Is carbon/energy footprint a relevant factor when designing / operating your centre?' : 'pie',
                'If yes: how do you address it?' : 'table',
                'Have you considered deploying more efficient / different architectures in order to improve power optimization?' : 'table',

}




#second file             
#allhepraPlots = {}
#fullPlots = {
#    'Which authorization and authentication methods do you support?' : 'table',
#    'Which authorization and authentication technical solutions do you support?' : 'table',
#    'Is your AAI federated via trust networks (edugain+ for example)?' : 'pie',
#    'Is your centre (also) operating on sensitive data?' : 'pie',
#    'If yes+ how do you operate it?' : 'table',
#    'Which quantum emulation stacks are you supporting?' : 'table',
#    'Which quantum hardware solution have you deployed?' : 'table',
#    'How do you support access to quantum hardware?' : 'table',#
#}  

allhepraPlots = {}
fullPlots = { 
    'Please quantify the size of your centre Number of CPU cores:Amount':'list',
    'Please quantify the size of your centre Number of CPU cores:Amount':'list',
 'Please quantify the size of your centre Nukber of GPU boards:Amount':'list',
 'Please quantify the size of your centre Installed disk (PB) - not including scratch disks on the nodes:Amount':'list',
'Please quantify the size of your centre Installed tape (PB):Amount':'list',
'Please quantify the size of your centre Total Power used (including cooling) in MW:Amount':'list',
'Please quantify the size of your centre Total surface for IT resources in squared meters:Amount':'list',
'Please quantify the size of your centre (if applicable) Total number of deployable standard racks:Amount':'list',


  }
#allpies!
fullPlots   = {
    'Is your data self-describing?' : 'barh',
    'How much will your software take advantage of multi-core processors?' : 'barh',
    'Are your data indexed / retrievable via Persistent Identifiers (PIDs)?' : 'barh',
    'On behalf of whom are you submitting the survey?':'barh',
    'How do you handle metadata?' : 'barh',
    'Do you use data movers?' : 'barh',
    'Do you use a Data Management solution to handle data ingestion / transfer / access?' : 'barh',
    'Which is the typical bandwidth with which new data enters the computing infrastructure? (if collected in bursts+ average over ~ 1 month period during operation periods) - please note B = Bytes': 'barh',
    'Which is the typical bandwidth needed from your storage systems (aggregate over the infrastructure)? (if served in bursts+ average over ~ 1 month during operation periods) - please note B = Bytes': 'barh',
    'Are you (ALSO) manager of an infrastructure? (computing centre+ a federated infrastructure+ a data centre+ ...)': 'barh',
    'On which timescale are these needs evaluated / requested? (for example+ requests are submitted year by year+ every 5 years+ ...)':'barh',
    'Duration':'barh',
    'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'barh',
    'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'barh',
    'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'barh',
    'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'barh',
    'Do your processes require access to external (remote) services (data sources+ accounting+ monitoring+ management+. ..)?':'barh',
    'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'barh',
    'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'barh',
    'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'barh',
    'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'barh',
    'How many total files / records are expected in your global storage systems?' : 'barh',
    'Do you handle data respecting FAIR Principles? (see for example here)' : 'barh',
    'Do you need public IPs on the compute nodes?' : 'barh',
    'Do you need root access at any point when executing workflows on the compute nodes?' : 'barh',
    'Do you have an agreed software licensing mode?':'barh',
    'Do you adopt FAIR for software principles? (see for example here)' : 'barh',
    'How is your initiative releasing software?' : 'barh',
    'How much will your software take advantage of multi-core processors?' : 'barh',
    'How much will you take advantage if vector/SIMD CPU registers?':'barh',
    'How much will you take advantage of GPUs/FPGAs?' : 'barh',
    'Do you have the resources needed to evolve your software as you will need to?' : 'barh',
    'Do people enter your field with the right software skills? (for example+ at undergrad / PhD / PostDoc / Staff levels?)' : 'barh',
    'Do you feel researchers developing and maintaining software and managing the computing infrastructures receive appropriate recognition in your institution / initiative?' : 'barh',
    'Which is the typical # of physical cores you have per motherboard for the latest hardware procured (exclude HT)' : 'barh',
    'Which is the typical # of GPUs you have per motherboard for the latest hardware procured' : 'barh',
    'Do your nodes have a local “scratch disk” in GB per core? Please note 1 GB = 1 GigaByte' : 'barh',
    'Do you have system to system fast intercommunication (MPI+ …)?' : 'barh',
    'Which type of network connection(s) are available between storage nodes? Please note Gbps = GigaBits per second' : 'barh',
    'Which type of network connection(s) are available to sources / destinations outside the centre (WAN)? Please note Gbps = GigaBits per second' : 'barh',
    'Which type(s) of resources does your e-Infrastructure provide today?' : 'barh',
    'Which is the total aggregate capacity for writing to storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'barh',
    'Which is the total aggregate capacity for reading from storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'barh',
    'Is carbon/energy footprint a relevant factor when designing / operating your centre?' : 'barh',
}
#fullPlots={'Is your AAI federated via trust networks (edugain+ for example)?' : 'barh',
#    'Is your centre (also) operating on sensitive data?' : 'barh',
#}
print ("here tommaso -------------------------")
for plot in fullPlots:

    if fullPlots[plot] == 'barh':
        print ("HETE BARH")
        extractBars(theSurvey,plot)
    if fullPlots[plot] == 'list':
        printList(theSurvey,plot)
    if fullPlots[plot] == 'bar':
        barplot2(theSurvey,plot)
    if fullPlots[plot] == 'table':
        print ("PLOT!!!!", plot)
        tableplot(theSurvey,plot)
    if fullPlots[plot] == 'hist':
        histogram(theSurvey,plot)
    if fullPlots[plot] == 'pie':
        pieplot(theSurvey,plot)
    if fullPlots[plot] == 'wcl':
        wclplot(theSurvey,plot)


for plot in allhepraPlots:
    if allhepraPlots[plot] == 'bar':
        barplot3Slices(sliceAll,sliceHEP,sliceRA,plot,'All','HEP', "RA")
    if allhepraPlots[plot] == 'table':
        tableplot3(theSurvey,sliceHEP,sliceRA,plot,'All','HEP', "RA")
