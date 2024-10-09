import csv
import pprint 


def slicer(theSurvey, theQuestion, theAnswers):

    #returns only the part of the survey whse lines match question = one of the answers
    # theSurvey is the list of dictionaries
    # theQuestion is the key of the dictionary to be matched
    # theAnswers is a list of strings to be matched

    slicedSurvey=[]
    for row in theSurvey:
        answers = row[theQuestion].split('; ')
        print ("the answers in this row",answers)
        for a in theAnswers:
            if a  in answers:
                slicedSurvey.append(row)
                print ("MATCHED")


    print ("Slicing returned ",len(slicedSurvey)," entries", "out of ",len(theSurvey))
    return slicedSurvey



def pieplot(theSlicedSurvey, theString):
            
    import matplotlib.pyplot as plt
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
        answer = i[stringQ]
    #    print ('Answer:',answer)
        answers = answer.split(';')
        for j in answers:
 #           print (j)
            if j in plotdict.keys():
                plotdict[j]=plotdict[j]+1
            else:
                plotdict[j]=1

    print ("DICT for the PLOT Using Query:",stringQ, "\n", plotdict)      

    plt.pie([float(plotdict[v]) for v in plotdict], labels=[str(k) for k in plotdict], autopct='%1.1f%%')
    plt.title(stringQ)

    plt.show() 

    return


def barplot(theSlicedSurvey, theString):
            
    import matplotlib.pyplot as plt
    import numpy as np

    # 1 - 'Which are the categories which better describe your role(s)?'

    stringQ = theString
    plotdict = {}

    for i in theSlicedSurvey:
        answer = i[stringQ]
    #    print ('Answer:',answer)
        answers = answer.split(';')
        for j in answers:
 #           print (j)
            if j in plotdict.keys():
                plotdict[j]=plotdict[j]+1
            else:
                plotdict[j]=1

    print ("DICT for the PLOT using Query:",stringQ, "\n",plotdict)     

     
    plt.bar(*zip(*plotdict.items()))
    plt.title(stringQ)
    plt.xticks(rotation=30, ha='right')

    plt.show() 



    return

def wclplot(theSlicedSurvey, theString):
    import matplotlib.pyplot as plt
    import numpy as np
    from wordcloud import WordCloud

    # 1 - 'Which are the categories which better describe your role(s)?'

    stringQ = theString

    text = ""

    for i in theSlicedSurvey:
        answer = i[stringQ]
        text = text + str(answer)
    
    print ("TEXT for the WORDCLOUD using Query",stringQ,"\n",text)      

    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(stringQ)      
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
#        print (row['\ufeffYour name'])
        theSurvey.append    (row)

print ("Finished reading the file, read  entries:"  + str(len(theSurvey)))       

# save it as json file
import json
with open('survey.json', 'w') as f:
    json.dump(theSurvey, f)
print ("Finished writing the file")

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(theSurvey[0])
        

#
# start doing easy plots
#

print ("PLOTTING!!!!!!")

#full plots

#barplot(theSurvey,'Which are the categories which better describe your role(s)?')
#wclplot(theSurvey,"Describe in a few words what is your activity")

#sliceRA = slicer(theSurvey,'Which is/are your scientific domain(s) of expertise (if applicable)?',['Observational Radio Astronomy (RA)'])

#sliced plots

barplot(sliceRA,'Which are the categories which better describe your role(s)?')


#types = ['bar','pie','wcl']
#all the plots in total and in HEP and RA projections

fullPlots = {'Which are the categories which better describe your role(s)?':"bar",
             'Describe in a few words what is your activity':"bar",
             'Which is/are your scientific domain(s) of expertise (if applicable)?':"bar",
             'Describe in a few words what is your activity':"wcl",
             'On behalf of whom are you submitting the survey?':'pie',
             'Provide a short name for your initiative / use case / centre (for our indexing) (for example+ data analysis at ATLAS)': 'wcl',
             'Are you (or the initiative you represent) ALSO a user of computing facilities in your scientific activity? (as a researcher+ as a programmer+ as a manager)': 'pie',
             'Please select your areas of expertise+ for which you can answer technical questions:':'bar'}

for plot in fullPlots:
    if fullPlots[plot] == 'bar':
        barplot(theSurvey,plot)
    if fullPlots[plot] == 'pie':
        pieplot(theSurvey,plot)
    if fullPlots[plot] == 'wcl':
        wclplot(theSurvey,plot)


