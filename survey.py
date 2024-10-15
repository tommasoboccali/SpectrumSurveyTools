import csv
import pprint 


def slicer(theSurvey, theQuestion, theAnswers):

    #returns only the part of the survey whse lines match question = one of the answers
    # theSurvey is the list of dictionaries
    # theQuestion is the key of the dictionary to be matched
    # theAnswers is a list of strings to be matched

    slicedSurvey=[]
    for row in theSurvey:
        print ("ANSWER",row[theQuestion],row[theQuestion].split('; ') )
        answers = row[theQuestion].split('; ')
        print ("the answers in this row",answers)
        for a in theAnswers:
            if a  in answers:
                slicedSurvey.append(row)
                print ("MATCHED")


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
    print ("DICT for the PLOT using Query:",stringQ, "\n",plotdict)     
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
    print ("DICT for the PLOT Using Query:",stringQ, "\n", plotdict)      
    return plotdict

def textforwcl(theSlicedSurvey, theString):
    stringQ = theString

    text = ""

    for i in theSlicedSurvey:
        answer = i[stringQ]
        text = text + " "+ str(answer)
    
    print ("TEXT for the WORDCLOUD using Query",stringQ,"\n",text)      
    return text

def vectforhist(theSlicedSurvey, theString):
    stringQ = theString
    histvect=[]
    
    for i in theSlicedSurvey:
        answer = i[stringQ]
        histvect.append(answer)
    return histvect
        

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

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(theSurvey[0])
        

#
# start doing easy plots
#

print ("PLOTTING!!!!!!")

#full plots

#barplot(theSurvey,'Which are the categories which better describe your role(s)?')
#wclplot(theSurvey,"Describe in a few words what is your activity")

sliceRA = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Observational Radio Astronomy (RA)'])
sliceHEP = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Experimental High Energy Physics (HEP)'])
sliceAll = theSurvey
barplot3Slices(sliceAll,sliceHEP,sliceRA, 'Which are the categories which better describe your role(s)?','All','HEP', "RA")

input("Press Enter to continue...")

#sliced plots

#barplot(sliceRA,'Which are the categories which better describe your role(s)?')

#histogram(theSurvey,'What is the team size (in number of collaborators) of the initiative?')

#types = ['bar','pie','wcl', 'hist']
#all the plots in total and in HEP and RA projections

fullPlots = {
    'Which are the categories which better describe your role(s)?':"bar",
    'Describe in a few words what is your activity':"bar",
    'Which is/are your scientific domain(s) of expertise (if applicable)?':"bar",
    'Describe in a few words what is your activity':"wcl",
    'On behalf of whom are you submitting the survey?':'pie',
    'Provide a short name for your initiative / use case / centre (for our indexing) (for example+ data analysis at ATLAS)': 'wcl',
    'Are you (or the initiative you represent) ALSO a user of computing facilities in your scientific activity? (as a researcher+ as a programmer+ as a manager)': 'pie',
    'Please select your areas of expertise+ for which you can answer technical questions:':'bar',
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
    if fullPlots[plot] == 'hist':
        histogram(theSurvey,plot)
    if fullPlots[plot] == 'pie':
        pieplot(theSurvey,plot)
    if fullPlots[plot] == 'wcl':
        wclplot(theSurvey,plot)


