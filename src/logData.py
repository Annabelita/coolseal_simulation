from os import path

from src.settings import *
import matplotlib.pyplot as plt
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import numpy as np
import math


'''
********
LogData.py erstellt die log.txt Datei und wertet sie automatisch als PDF aus
*********
'''




'''
********
Helper Functions -> Für Winkelmaß 
*********
'''

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))








'''
********
Plotten von Funktionen 

showAngle=True wenn das Winkelmaß berechnet werden soll
path: Datei Name der log.txt Datei
lim_y, lim_x: Maximal Werte der (x,y) Werte in den Plots
plotColor: Farbe der Pfade
plotColorBEST: Farbe des 'Best Path'
****
'''
def plotSomeWalk(pathToLog, lim_y, lim_x, plotColor, plotColorBEST, showAngle=True):
    pfad = path.join(path.dirname(path.abspath(__file__)), pathToLog)
    print(pfad)
    with open(pfad) as f:
        step_values = []
        percentage_values = []
        max_percentage = 0
        step_max = 0

        vectors = []
        x_axis = (350, 0)

        simulation_count = 1
        while True:
            line = f.readline()
            if line:
                if line.startswith("Step"):
                    x, y = line.split('--------')
                    forget, step = x.split(':')
                    forget, percentage = y.split(':')
                    step_values.append(float(step))
                    percentage_values.append(float(percentage[:-2]))
                    vectors.append((float(step), float(percentage[:-2])))

                if line.startswith("Walk"):
                    forget, walkName = line.split(':')

                if line.startswith("Amount of ants"):
                    forget, anzahlAgenten = line.split(':')
                    anzahlAgenten = anzahlAgenten.replace(' ', '')
                    anzahlAgenten = anzahlAgenten.replace('\n', '')



                if line.startswith("---------------------- END OF SIMULATION"):
                    if max_percentage < np.max(percentage_values):
                        max_percentage = np.max(percentage_values)

                        MAX_step = np.max(step_values)
                        step_max = step_values
                        percentage_max = percentage_values


                    if max_percentage == np.max(percentage_values):
                        if MAX_step >= np.max(step_values):
                            MAX_step = np.max(step_values)
                            max_percentage = np.max(percentage_values)
                            step_max = step_values
                            percentage_max = percentage_values



                    if simulation_count == 1:
                        if showAngle:
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor)
                        elif pathToLog=='SimpleWalk-1-ul' or pathToLog=='mDFS-1-ul':
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor, label='unten links')
                        elif pathToLog=='SimpleWalk-1-ur' or pathToLog=='mDFS-1-ur':
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor, label='unten rechts')
                        elif pathToLog=='SimpleWalk-1-ol' or pathToLog=='mDFS-1-ol':
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor, label='oben links')
                        elif pathToLog=='SimpleWalk-1-or' or pathToLog=='mDFS-1-or':
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor, label='oben rechts')
                        else:
                            plt.plot(step_values, percentage_values, 'o-', color=plotColor, label=walkName)
                    else:
                        plt.plot(step_values, percentage_values, 'o-', color=plotColor)

                    step_values = []
                    percentage_values = []
                    simulation_count += 1



                if simulation_count == SIMULATIONROUNDS+1:
                    if pathToLog!='SimpleWalk-1-ul' and pathToLog!='SimpleWalk-1-ur' and pathToLog!='SimpleWalk-1-or' and pathToLog!='SimpleWalk-1-ol':
                        plt.plot(step_max, percentage_max, 's-', color=plotColorBEST, label='Bester Pfad')
                    bestPercentage = (lim_x/2, lim_y-10, f'max percent {percentage_max[len(percentage_max) - 1]}')
                    bestStep = (lim_x/2, lim_y-10, f'max step {step_max[len(step_max) - 1]}')

                    if showAngle:
                        x = [0]
                        x.append(step_max[len(step_max) - 1])
                        y = [0]
                        y.append(percentage_max[len(percentage_max) - 1])
                        v = (float(step_max[len(step_max) - 1]), float(percentage_max[len(percentage_max) - 1]))
                        max_angle = angle(v, x_axis)
                        max_angle = "{:.2f}".format(max_angle)
                        forget, max_angle = str(max_angle).split('.')
                        plt.plot(x, y, 's-', color='red', label=f'Winkel: {max_angle} Grad', ms=5)


                    plt.legend(loc=4, prop={'size': 15})
                    if anzahlAgenten == '1':
                        name = f'{walkName} {anzahlAgenten} Agent'
                    else:
                        name = f'{walkName} {anzahlAgenten} Agenten'
                    name = name.replace('\n', '')
                    plt.title(name, fontsize=20)
                    plt.tick_params(axis='x', which='major', labelsize=10)
                    plt.tick_params(axis='y', which='major', labelsize=10)
                    plt.ylim(0, lim_y)
                    plt.xlim(0, lim_x)
                    plt.xlabel('Schritte', fontsize=20)
                    plt.ylabel('Färbungsgrad in %', fontsize=20)
                    plt.grid(True)
                    plt.tight_layout()
                    pathToLog = 'Analysis/Plots/log.png'
                    placeToSave = path.join(path.dirname(path.abspath(__file__)), pathToLog)
                    plt.savefig(placeToSave)
                    plt.show()

                    return percentage_max[len(percentage_max) - 1], step_max[len(step_max) - 1]







'''
********
Erstellt eine automatische Auswertung der log.txt
path: Name der log.txt ohne Dateiendung
****
'''

def createPDF(pathToLog, bestPercentage, bestStep):
    pfad = path.join(path.dirname(path.abspath(__file__)), pathToLog)
    print(pfad)
    list_maxStep = []
    list_maxPercentage = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', fontName='Times', fontSize=20))
    styles.add(ParagraphStyle(name='Justify-Bold', fontName='Times-Bold'))
    bold_style = styles['Justify-Bold']
    normal_style = styles['Justify']

    styleN = styles['Normal']
    styleH = styles['Heading1']
    story = []

    pathToLog = 'Results/log.pdf'
    pdf = path.join(path.dirname(path.abspath(__file__)), pathToLog)
    pdf_name = pdf
    doc = SimpleDocTemplate(
        pdf_name,
        pagesize=letter,
        bottomMargin=.4 * inch,
        topMargin=.6 * inch,
        rightMargin=.8 * inch,
        leftMargin=.8 * inch)


    with open(pfad, "r") as txt_file:
        step_values = []
        percentage_values = []
        max_percentage = 0
        count = 1
        countHouse = 0

        text_content = 'Aggregation der Log-Ergebnisse'
        P = Paragraph(text_content, styleH)
        story.append(P)


        while True:
            line = txt_file.readline()

            if line.startswith('New House'):
                countHouse +1


            if line.startswith("Step"):
                x, y = line.split('--------')
                forget, step = x.split(':')
                forget, percentage = y.split(':')
                step_values.append(float(step))
                percentage_values.append(float(percentage[:-2]))

            if line.startswith("Walk"):
                forget, walkName = line.split(':')

            if line.startswith("Amount of ants"):
                forget, anzahlAgenten = line.split(':')
                anzahlAgenten = anzahlAgenten.replace(' ', '')
                anzahlAgenten = anzahlAgenten.replace('\n', '')

            if 'END OF SIMULATION' in line:
                percentage_max = np.max(percentage_values)
                step_max = np.max(step_values)
                list_maxPercentage.append(percentage_max)
                list_maxStep.append(step_max)

                percentage_values = []
                step_values = []

                text_content = 'Simulation ' + str(count) + ' ------ Färbunsgrad: ' + str(percentage_max) + '%, Schritte: ' + str(step_max)
                count += 1
                P = Paragraph(text_content, styleN)
                story.append(P)

            if line.startswith("ENDE"):

                text_content = '-----------------------------------------'
                P = Paragraph(text_content, styleN)
                story.append(P)

                # calculate average
                avgPercentage = np.average(list_maxPercentage)
                avgStep = np.average(list_maxStep)

                text_content = 'Zusammenfassung:'
                P = Paragraph(text_content, styleH)
                story.append(P)

                text_content = 'Der beste Pfad färbt ' + str(round(bestPercentage, 2)) + '% der Fläche und benötigt ' + str(bestStep) + ' Schritte.'
                P = Paragraph(text_content, styleH)
                story.append(P)

                text_content = 'Im Durchschnitt wurde ' + str(round(avgPercentage, 2)) + '% der Fläche gefärbt.'
                P = Paragraph(text_content, styleH)
                story.append(P)

                text_content = 'Im Durchschnitt wurden hierfür ' + str(round(avgStep, 2)) + ' Schritte benötigt.'
                P = Paragraph(text_content, styleH)
                story.append(P)

                text_content = 'Es wurden ' + str(countHouse) + ' Häuser manuell eingefügt.'
                P = Paragraph(text_content, styleH)
                story.append(P)

                text_content = '-----------------------------------------'
                P = Paragraph(text_content, styleN)
                story.append(P)


                pathToLog = 'Analysis/Plots/log.png'
                img = path.join(path.dirname(path.abspath(__file__)), pathToLog)
                story.append(Image(img, 400, 350))
                break


    doc.build(
        story,
    )






'''
********
Muss kommentiert bleiben 
-> Wurde nur benutzt um die logs und pdfs zu erzeugen 
****
'''

'''
plotSomeWalk('Analysis/logFiles/randomWalk-allCorners-4.txt', 70, 300, '#4E87CF', '#043A7E', False)
plotSomeWalk('Analysis/logFiles/SimpleWalk-1-ul.txt', 50, 400, 'red', 'red', False)
plotSomeWalk('Analysis/logFiles/SimpleWalk-1-ol.txt', 50, 400, 'green', 'green', False)
plotSomeWalk('Analysis/logFiles/SimpleWalk-1-ur.txt', 50, 400, 'brown', 'brown', False)
plotSomeWalk('Analysis/logFiles/SimpleWalk-1-or.txt, 50, 400, 'blue', 'blue', False)
plotSomeWalk('Analysis/logFiles/SimpleWalk-BestCorners-2.txt', 100, 350, '#55C592', '#046639')
plotSomeWalk('Analysis/logFiles/SimpleWalk-BestCorners-4.txt', 100, 350, '#55C592', '#046639')
plotSomeWalk('Analysis/logFiles/SimpleWalk-BestCorners-6.txt', 100, 350, '#55C592', '#046639')
plotSomeWalk('Analysis/logFiles/SimpleWalk-BestCorners-8.txt', 100, 350, '#55C592', '#046639')


plotSomeWalk('Analysis/logFiles/mDFS-1-ol.txt', 110, 1000, '#55C592', '#046639', False)
plotSomeWalk('Analysis/logFiles/mDFS-1-or.txt', 110, 1000, '#55C592', '#046639', False)
plotSomeWalk('Analysis/logFiles/mDFS-1-ul.txt', 110, 1000, '#55C592', '#046639', False)
plotSomeWalk('Analysis/logFiles/mDFS-1-ur.txt', 110, 1000, '#55C592', '#046639', False)




plotSomeWalk('Analysis/logFiles/mDFS-2-ol-ul.txt', 110, 1000, '#55C592', '#046639', False)

plotSomeWalk('Analysis/logFiles/mDFS-2-ol-ur.txt', 110, 1000, '#55C592', '#046639', False)





bestPercentage, bestStep = plotSomeWalk('Analysis/logFiles/mDFS-1-or.txt', 110, 1000, '#55C592', '#046639', False)
createPDF('Analysis/logFiles/mDFS-1-or.txt', bestPercentage, bestStep)



bestPercentage, bestStep = plotSomeWalk('Analysis/logFiles/mDFS-2-or-ul.txt', 110, 1000, '#55C592', '#046639', False)
createPDF('Analysis/logFiles/mDFS-2-or-ul.txt', bestPercentage, bestStep)




bestPercentage, bestStep = plotSomeWalk('Analysis/logFiles/mDFS-4-or-ul.txt', 110, 1000, '#55C592', '#046639', False)
createPDF('Analysis/logFiles/mDFS-4-or-ul.txt', bestPercentage, bestStep)



plotSomeWalk('Analysis/logFiles/mDFS-2-or-ul', 110, 1000, '#55C592', '#046639', False)



createPDF('Analysis/logFiles/mDFS-2-ol-ul.txt')
createPDF('Analysis/logFiles/mDFS-2-ol-ur.txt')
createPDF('Analysis/logFiles/mDFS-2-or-ur.txt')
createPDF('Analysis/logFiles/mDFS-2-or-ul.txt')





createPDF('Analysis/logFiles/simpleWalk-BestCorners-2.txt')
createPDF('Analysis/logFiles/simpleWalk-BestCorners-4.txt')
createPDF('Analysis/logFiles/simpleWalk-BestCorners-6.txt')
createPDF('Analysis/logFiles/simpleWalk-BestCorners-8.txt')


createPDF('randomWalk-allCorners-4.txt')
createPDF('simpleWalk-allCorners-4.txt')


'''#











Tiefe = [1,2,3,4,5,6,7]

NegaMax_7_fenString1_Nodes = [32, 1056, 5504, 156596, 276310, 7994756, 11037630]
NegaMax_7_fenString1_Time = [3.3903,26.9838,225.8968,1747.0834,1887.3251,30453.459,76402.4479]
NegaMax_7_fenString2_Nodes = [12, 95, 659, 1718, 7893, 16719, 67649]
NegaMax_7_fenString2_Time = [2.0508, 6.229, 36.9702, 97.7538, 181.4495, 799.95, 1042.1209]
NegaMax_7_fenString3_Nodes = [27, 742, 3811, 79939, 250935, 4100707, 11323186]
NegaMax_7_fenString3_Time = [3.4699, 26.4759, 161.9047, 1248.4382, 1323.8129, 17143.2978, 59954.892]
NegaMax_7_fenString4_Nodes = [17, 482, 2954, 27063, 205874, 2196587, 8322639]
NegaMax_7_fenString4_Time = [2.8579, 19.5155, 118.4368, 431.1015, 2153.8488, 9215.1834, 42332.1145]

NegaScout_7_fenString1_Nodes = [32, 1056, 5632, 62414, 271432, 1949283, 10292516]
NegaScout_7_fenString1_Time = [3.8097, 23.9121, 206.3868, 1211.0946, 4288.8962, 9190.6953, 52699.3884]
NegaScout_7_fenString2_Nodes = [12, 95, 836, 2139, 9880, 16988, 62526]
NegaScout_7_fenString2_Time = [2.1069, 8.6545, 41.5342, 124.9921, 525.9811, 820.8505, 645.262]
NegaScout_7_fenString3_Nodes = [27, 742, 4036, 55682, 210541, 2526166, 8454802]
NegaScout_7_fenString3_Time = [4.3974, 27.7697, 270.1949, 1880.447, 1639.2803, 10974.0973, 43296.5816]
NegaScout_7_fenString4_Nodes = [17, 482, 3274, 20380, 200061, 873262, 8035799]
NegaScout_7_fenString4_Time = [3.0318, 29.442, 162.5562, 565.112, 2184.1562, 4806.0266, 36333.319]

'''
import matplotlib.ticker as plticker

plt.plot(NegaMax_7_fenString1_Nodes, Tiefe, 'blue', label="NegaMax", ms=5)
plt.plot(NegaScout_7_fenString1_Nodes, Tiefe, 'red', label="NegaScout", ms=5)
plt.legend(loc=4, prop={'size': 15})
plt.tick_params(axis='x', which='major', labelsize=10)
plt.tick_params(axis='y', which='major', labelsize=10)
plt.xlabel('Nodes',fontsize=23)
plt.ylabel('Depth',fontsize=23)
loc = plticker.MultipleLocator(base=1500000)
plt.xaxis.set_major_locator(loc)
plt.tick_params(axis='x', which='major', labelsize=23)
plt.tick_params(axis='y', which='major', labelsize=23)
plt.grid(True)
plt.tight_layout()
pathToLog = 'src'
placeToSave = path.join(path.dirname(path.abspath(__file__)), pathToLog)
plt.savefig(placeToSave)
plt.show()
'''




fig1 = plt.figure(1, figsize=(20,12))


ax = fig1.add_subplot(2,1,1)
# TODO
ax.set_title('FEN: tttttttt/8/8/8/8/8/TTTTTTTT_r',fontsize=23)
ax.set_xlabel('Nodes',fontsize=23)
ax.set_ylabel('Depth',fontsize=23)

#x = 17, 482, 2954, 27063, 205874, 2196587, 8322639
#y = 1,2,3,4,5,6,7

ax.get_xaxis().set_major_formatter(
    mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

ax.plot(NegaMax_7_fenString1_Nodes, Tiefe, 'bo', NegaMax_7_fenString1_Nodes, Tiefe, 'black')


ax2 = fig1.add_subplot(2,1,2)
#ax2.set_title('NegaScout tt6/6w1/twtt1tW1/3w1WT1/W1TTWW2/1TW1W3/8 r',fontsize=23)
ax2.set_xlabel('Nodes',fontsize=23)
ax2.set_ylabel('Depth',fontsize=23)



#x2 = 17, 482, 3274, 20380, 200061, 873262, 8035799
#y2 = 1,2,3,4,5,6,7


ax2.get_xaxis().set_major_formatter(
    mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

ax2.plot(NegaScout_7_fenString1_Nodes, Tiefe, 'bo', NegaScout_7_fenString1_Nodes, Tiefe, 'black')


loc = plticker.MultipleLocator(base=1500000)
ax.xaxis.set_major_locator(loc)
ax.tick_params(axis='x', which='major', labelsize=23)
ax.tick_params(axis='y', which='major', labelsize=23)

'''
ax2.xaxis.set_major_locator(loc)
ax2.tick_params(axis='x', which='major', labelsize=23)
ax2.tick_params(axis='y', which='major', labelsize=23)
'''

fig1.tight_layout()
#fig1.xlim(0, 10292516)
fig1.savefig('FenString1_Nodes.png')
fig1.show()

#####
fig1 = plt.figure(1, figsize=(20,12))


ax = fig1.add_subplot(2,1,1)
# TODO
ax.set_title('FEN: tttttttt/8/8/8/8/8/TTTTTTTT_r',fontsize=23)
ax.set_xlabel('Nodes',fontsize=23)
ax.set_ylabel('Depth',fontsize=23)

#x = 17, 482, 2954, 27063, 205874, 2196587, 8322639
#y = 1,2,3,4,5,6,7

ax.get_xaxis().set_major_formatter(
    mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

ax.plot(NegaMax_7_fenString1_Nodes, Tiefe, 'bo', NegaMax_7_fenString1_Nodes, Tiefe, 'black')


ax2 = fig1.add_subplot(2,1,2)
#ax2.set_title('NegaScout tt6/6w1/twtt1tW1/3w1WT1/W1TTWW2/1TW1W3/8 r',fontsize=23)
ax2.set_xlabel('Nodes',fontsize=23)
ax2.set_ylabel('Depth',fontsize=23)



#x2 = 17, 482, 3274, 20380, 200061, 873262, 8035799
#y2 = 1,2,3,4,5,6,7


ax2.get_xaxis().set_major_formatter(
    mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

ax2.plot(NegaScout_7_fenString1_Nodes, Tiefe, 'bo', NegaScout_7_fenString1_Nodes, Tiefe, 'black')


loc = plticker.MultipleLocator(base=1500000)
ax.xaxis.set_major_locator(loc)
ax.tick_params(axis='x', which='major', labelsize=23)
ax.tick_params(axis='y', which='major', labelsize=23)

'''
ax2.xaxis.set_major_locator(loc)
ax2.tick_params(axis='x', which='major', labelsize=23)
ax2.tick_params(axis='y', which='major', labelsize=23)
'''

fig1.tight_layout()
#fig1.xlim(0, 10292516)
fig1.savefig('FenString1_Nodes.png')
fig1.show()








