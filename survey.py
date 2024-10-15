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


def dictforbar(theSlicedSurvey, theString):
    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
            answer = i[stringQ]
            if answer == "":
                print ("EMPTY ANSWER", i['\ufeffYour name'])
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
        plotdict['N/A']=plotdict['']
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
        plotdict['N/A']=plotdict['']
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
            if answer == "":
                print ("EMPTY ANSWER", i['\ufeffYour name'])
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
        plotdict['N/A']=plotdict['']
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

    utabdictall = dictfortable(theSliceAll,'Which are the categories which better describe your role(s)?')
    utabdict1 = dictfortable(theSlicedSurvey1,'Which are the categories which better describe your role(s)?')
    utabdict2 = dictfortable(theSlicedSurvey2,'Which are the categories which better describe your role(s)?')

    
    tabdictall = {key: value for key, value in sorted(utabdictall.items())}
    tabdict1 = {key: value for key, value in sorted(utabdict1.items())}
    tabdict2 = {key: value for key, value in sorted(utabdict2.items())}
    

    from plotly.subplots import make_subplots

    limits = [100,20,20]

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

    tabdict = dictfortable(theSurvey,'Which are the categories which better describe your role(s)?')


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
    limits = [100,20,20]
    fig = go.Figure(data=[go.Table(columnwidth=limits,header=                           
        dict(values=['Which are the categories which better describe your role(s)?', 'Answers', 'Fraction (%)']),
                 cells=dict(values=[headerline,cellsline,fractions])
    )])
    fig.show()


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
headerline=True
theSurvey=[]

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for row in reader:
#        for key in row:
#             print(key, "->", row[key])
        print (row['\ufeffYour name'])
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
        

#
# start doing easy plots
#

#tableplot(theSurvey,'Which are the categories which better describe your role(s)?')

sliceRA = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Observational Radio Astronomy (RA)'])
sliceHEP = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Experimental High Energy Physics (HEP)'])
sliceAll = theSurvey


print ("PLOTTING!!!!!!")

tableplot3(theSurvey,sliceHEP,sliceRA,'Which are the categories which better describe your role(s)?','All','HEP', "RA")


#full plots

#barplot(theSurvey,'Which are the categories which better describe your role(s)?')
#wclplot(theSurvey,"Describe in a few words what is your activity")


barplot3Slices(sliceAll,sliceHEP,sliceRA, 'Which are the categories which better describe your role(s)?','All','HEP', "RA")

input("Press Enter to continue...")

#sliced plots

#barplot(sliceRA,'Which are the categories which better describe your role(s)?')

#histogram(theSurvey,'What is the team size (in number of collaborators) of the initiative?')

#types = ['bar','pie','wcl', 'hist']
#all the plots in total and in HEP and RA projections

fullPlots = {
    'Which are the categories which better describe your role(s)?':'table',
    'Describe in a few words what is your activity':"wcl",
    'Which is/are your scientific domain(s) of expertise (if applicable)?':"table",
    'On behalf of whom are you submitting the survey?':'pie',
    

#over .....
}

allhepraPlots = {
    'Which are the categories which better describe your role(s)?':'table',
    'Describe in a few words what is your activity':"wcl",
    'Which is/are your scientific domain(s) of expertise (if applicable)?':"table",
    'On behalf of whom are you submitting the survey?':'pie',
    'Provide a short name for your initiative / use case / centre (for our indexing) (for example+ data analysis at ATLAS)': 'wcl',
    'Are you (or the initiative you represent) ALSO a user of computing facilities in your scientific activity? (as a researcher+ as a programmer+ as a manager)': 'pie',
    'Please select your areas of expertise+ for which you can answer technical questions:':'table',
    'Which initiative / centre? (for example: The CMS Experiment at CERN or the CINECA HPC Centre)': 'wcl',
    'What is the team size (in number of collaborators) of the initiative?': 'hist',
    'Are you (ALSO) manager of an infrastructure? (computing centre+ a federated infrastructure+ a data centre+ ...)': 'pie',
#AAI
    'Authentication and Authorization supported method(s) [this includes Workload and Storage management]':'wcl',
    'Technical solutions supported for AA':'wcl',
    'Which AA tools do you support or make use of?':'wcl',

#over .....
}

for plot in fullPlots:
    if fullPlots[plot] == 'bar':
        barplot2(theSurvey,plot)
    if fullPlots[plot] == 'table':
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