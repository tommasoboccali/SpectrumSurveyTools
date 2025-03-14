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


def dictforbarH(theSlicedSurvey, theString):
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
    print ("DICT for the PLOT Using Query:",stringQ, "\n", plotdict)      
# I need to sort it by value
    plotdict = dict(sorted(plotdict.items(), key=lambda item: item[1], reverse=True))
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

def barplotH(theSlicedSurvey, theString):
    import matplotlib.pyplot as plt
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    plotdict=dictforbar(theSlicedSurvey, theString)
    print ("DICT for the PLOT using Query:",theString, "\n",plotdict)     

    x = [key for key in plotdict.keys()]   
    y = [value for value in plotdict.values()]
    
    fig , ax = plt.subplots()
    width = 0.75
    ind = np.arange(len(y))
    y_norm = [float(i)/sum(y) for i in y]
    bars = ax.barh(x, y_norm, width, color="blue")
    ax.bar_label(bars)
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(x, minor=False)
    plt.title('title')
    plt.xlabel('x')
    plt.ylabel('y')      
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
    print ("KEY",i)

#
# start doing easy plots
#

#tableplot(theSurvey,'Which are the categories which better describe your role(s)?')

#NEEDED FOR FIRST FILE
sliceRA = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Observational Radio Astronomy (RA)'])
sliceHEP = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Experimental High Energy Physics (HEP)'])

sliceAll = theSurvey

#sliceMultinode = slicer(theSurvey,'Granularity of job submission',['Multi node'])

#printList(sliceMultinode,'Which is/are your scientific domain(s) of expertise (if applicable)?')

#input("Press Enter to continue...")


print ("PLOTTING!!!!!!")

#tableplot3(theSurvey,sliceHEP,sliceRA,'Which are the categories which better describe your role(s)?','All','HEP', "RA")


#full plots

#barplot(theSurvey,'Which are the categories which better describe your role(s)?')
#wclplot(theSurvey,"Describe in a few words what is your activity")


#barplot3Slices(sliceAll,sliceHEP,sliceRA, 'Which are the categories which better describe your role(s)?','All','HEP', "RA")

#input("Press Enter to continue...")

#sliced plots

#barplot(sliceRA,'Which are the categories which better describe your role(s)?')

#histogram(theSurvey,'What is the team size (in number of collaborators) of the initiative?')

#types = ['bar','pie','wcl', 'hist']
#all the plots in total and in HEP and RA projections

fullPlots = {
    'On behalf of whom are you submitting the survey?':'barH',
    'Are you (ALSO) manager of an infrastructure? (computing centre+ a federated infrastructure+ a data centre+ ...)': 'barH',
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
           'Duration':'barH',
           'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'barH',
           'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'barH',
           'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'barH',
           'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'barH',
           
           
           }

#over .....

fullPlots = {'Do your processes require access to external (remote) services (data sources+ accounting+ monitoring+ management+. ..)?':'barH',
             'Please give it a short name (e.g. "reconstruction at CMS") for identification purposes':'wcl',
             'Memory needed per core (if you know the answer per node+ assume ~ 100 core nodes and thus divide by 100) - please note GB = GigaByte':'barH',
             'Local scratch disk per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note GB = GigaByte':'barH',
             'Network I/O within the centre (if you know the answer per node+ assume 100 cores nodes+ and divide by 100) - please note MB = MegaByte':'barH',
             'Geographical Network I/O per core (if you know the answer per node+ assume 100 cores nodes+ and divide by 100). This is relevant for example for data downloading from a distant centre before/during the execution+ and data uploading at the end. Please note 1 MB = 1 MegaByte':'barH',
           }

fullPlots = {'Total expected volume to be handled (including everything: data from instruments+ simulations+ analysis samples) - in PB (PetaBytes)': 'list',
            'Please specify which formats are you using (for example+ CSV+ XLS+ ROOT+ HDF5+ FITS+ ...)' : 'wcl',
'How many total files / records are expected in your global storage systems?' : 'barH',
             'Do you handle data respecting FAIR Principles? (see for example here)' : 'barH',
             
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
             'Do you need public IPs on the compute nodes?' : 'barH',
             'If yes+ which is the typical fraction of the overall workflow which can be offloaded to accelerators in %? (for example+ in total fraction of operations or total fraction of the workflow time)': 'list',
                 'Do you need root access at any point when executing workflows on the compute nodes?' : 'barH',


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
 'Do you have an agreed software licensing mode?':'barH',
    'Do you adopt FAIR for software principles? (see for example here)' : 'barH',
    'How is your initiative releasing software?' : 'barH',
    'Do you anticipate using other hardware architectures than today? Which ones?' : 'wcl',
    'How much will your software take advantage of multi-core processors?' : 'barH',
    'How much will you take advantage if vector/SIMD CPU registers?':'barH',
    'How much will you take advantage of GPUs/FPGAs?' : 'barH',
    'Do you have the resources needed to evolve your software as you will need to?' : 'barH',


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
    'Do people enter your field with the right software skills? (for example+ at undergrad / PhD / PostDoc / Staff levels?)' : 'barH',
    'Do you feel researchers developing and maintaining software and managing the computing infrastructures receive appropriate recognition in your institution / initiative?' : 'barH',
}

#allhepraPlots = {
#    'Who designs and maintains the software in your initiative? (analysis+ reconstruction+ simulation+ ...)':'table',
##    'Who designs and maintains the computing tools needed by your initiative? (operations+ monitoring+ accounting+ deployment+ WMS and data management+ ...)' : 'table',
#    'On which categories could you get training?' : 'table',
#}

#fullPlots = {
  #  'Which type(s) of resources does your e-Infrastructure provide today?':'table',
      #          'Is the centre part of a larger e-infrastructure?':'table',
     #           'Which are the main mechanisms to get access to your infrastructure?' : 'table',
    #            'Do you allow users to deploy services on login / edge nodes?' : 'table',
   #             'Resource allocation methods' : 'table',
  #              'Which access patterns to the system you support?' : 'table',
 #               'How long are typical resource allocations? (project / grant length)' : 'table',
#                'How long can the single processes be executed for?'    : 'table',
            #    'Which base system architecture is your centre supporting?' : 'table',
           #     'Which GPGPU architectures are you supporting?' : 'table',
          #      'Which is the typical # of physical cores you have per motherboard for the latest hardware procured (exclude HT)' : 'barH',
         #       'Which is the typical # of GPUs you have per motherboard for the latest hardware procured' : 'barH',
        #        'Which is the typical memory per core you deploy+ in GB? Please note 1 GB = 1 GigaByte' : 'table',
       #         'Do your nodes have a local “scratch disk” in GB per core? Please note 1 GB = 1 GigaByte' : 'barH',
      #          'Do you have system to system fast intercommunication (MPI+ …)?' : 'barH',
     #           'Which type of network connection(s) are available between storage nodes? Please note Gbps = GigaBits per second' : 'barH',
    #            'Which type of network connection(s) are available to sources / destinations outside the centre (WAN)? Please note Gbps = GigaBits per second' : 'barH',
   #             'Which type of network connection(s) are available between storage and compute nodes? Please note Gbps = GigaBits per second' : 'pue',
  #              'Which type(s) of resources does your e-Infrastructure provide today?' : 'barH',
 #               'Which routing options are available from your compute nodes? OUTGOING CONNECTIONS' : 'table',
#                'Which routing options are available from your compute nodes? INCOMING CONNECTIONS' : 'table',
            #    'Does your centre use / support data management tools to move / access / manage data?' : 'table',
           #     'Specify the data management tool(s) your site uses and put a link to its documentation if available?': 'wcl',
          #      'How do you manage disk-based storage?' : 'table',
         #       'How do you manage tape-based storage?' : 'table',
        #        'Protocols to access the storage systems+ from internal hosts (for example compute nodes)':'table',
       #         'Protocols to access the storage systems+ from external hosts (for example storage to storage geographical transfers)' : 'table',
      #          'Which is the total aggregate capacity for writing to storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'barH',
     #           'Which is the total aggregate capacity for reading from storage in your centre (summed over the storage systems if you have many) - Please note 1 GB = 1 GigaByte' : 'barH',
    #            'Which of the following features do you support?' : 'table',
   #             'Is carbon/energy footprint a relevant factor when designing / operating your centre?' : 'barH',
  #              'If yes: how do you address it?' : 'table',
 #               'Have you considered deploying more efficient / different architectures in order to improve power optimization?' : 'table',
#
#}




#second file             
#allhepraPlots = {}
#fullPlots = {
#    'Which authorization and authentication methods do you support?' : 'table',
#    'Which authorization and authentication technical solutions do you support?' : 'table',
#    'Is your AAI federated via trust networks (edugain+ for example)?' : 'barH',
#    'Is your centre (also) operating on sensitive data?' : 'barH',
#    'If yes+ how do you operate it?' : 'table',
#    'Which quantum emulation stacks are you supporting?' : 'table',    'Which quantum hardware solution have you deployed?' : 'table',
#    'How do you support access to quantum hardware?' : 'table',#
#}  

#allhepraPlots = {}
#fullPlots = { 
#    'Please quantify the size of your centre Number of CPU cores:Amount':'list',
#    'Please quantify the size of your centre Number of CPU cores:Amount':'list',
# 'Please quantify the size of your centre Nukber of GPU boards:Amount':'list',
# 'Please quantify the size of your centre Installed disk (PB) - not including scratch disks on the nodes:Amount':'list',
#'Please quantify the size of your centre Installed tape (PB):Amount':'list',
#'Please quantify the size of your centre Total Power used (including cooling) in MW:Amount':'list',
#'Please quantify the size of your centre Total surface for IT resources in squared meters:Amount':'list',
#'Please quantify the size of your centre (if applicable) Total number of deployable standard racks:Amount':'list',


 # }


for plot in fullPlots:
    pprint.pprint("TOMMASO"+plot)
    if fullPlots[plot] == 'list':
        printList(theSurvey,plot)
    if fullPlots[plot] == 'bar':
        barplot2(theSurvey,plot)
    if fullPlots[plot] == 'barH':
        barplotH(theSurvey,plot)
    if fullPlots[plot] == 'table':
        print ("PLOT!!!!", plot)
        tableplot(theSurvey,plot)
    if fullPlots[plot] == 'hist':
        histogram(theSurvey,plot)
    if fullPlots[plot] == 'wcl':
        wclplot(theSurvey,plot)


