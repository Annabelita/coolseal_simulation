import matplotlib.pyplot as plt
import numpy as np
import random
import math
import os

'''
****
Plotten von Funktionen EXP2
****
'''

def plotSomeWalk(plotname, logName):
    #pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), logName)
    with open(logName) as f:
        count = 0
        while True:
            line = f.readline()
            if line:
                if line.startswith("ENDE"):
                    break;
                if line.startswith("<"):
                    forget, array = line.split("[")
                    array = "[" + array
                    array = eval(array)
                    plt.plot(10, np.min(array), color="red")
                    x_axis = np.arange(len(array))
                    randomColor = lambda: random.randint(0, 255)
                    randomColor = '#{:02x}{:02x}{:02x}'.format(randomColor(), randomColor(), randomColor())

                    if count == 1:
                        plt.plot(x_axis, array, 's-', color="#CDCBC8", label="Agent" + str(count))
                    else:
                        plt.plot(x_axis, array, 's-', color="#CDCBC8", label="Agent" + str(count))
                    #plt.plot(x_axis, array, 's-', color=randomColor, label="Agent" + str(count))
                    '''
                    plt.plot(x_axis, array, 's-', color=randomColor, label="Agent" + str(count))
                    '''
                    plt.plot(9, array[len(array)-1], 'o-', color="red", linewidth=4.0)
                    count += 1



        '''
        pos1_x = [2, 2]
        pos1_y = [-2, 20]
        plt.plot(pos1_x, pos1_y, 'o-', color="red", linewidth=4.0)

        pos2_x = [5, 5]
        pos2_y = [-2, 20]
        plt.plot(pos2_x, pos2_y, 'o-', color="red", linewidth=4.0)
        '''



        plt.legend(loc=1, prop={'size': 10})

        plt.title(plotname, fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=10)
        plt.tick_params(axis='y', which='major', labelsize=10)
        plt.xlabel('Runden', fontsize=20)
        plt.ylabel('Gebote', fontsize=20)
        plt.grid(True)
        plt.tight_layout()

        plt.savefig('exp1_5Agenten_10Tasks')
        plt.show()

plotSomeWalk("Final cfp", "/Users/Annabella/Desktop/SoSe_2019/Agententechnologie/Hausaufgaben/HA01/AOT_Hausaufgabe_1/src/HA02_AOT/Logs/EXP1/EXP1_Task43_5Agents.txt")

''' EXPERIMENT 3'''
'''
def plotSomeWalk(plotname):
    tasklist = [5, 7, 7, 5, 5, 5, 7, 7, 3, 3, 7, 7, 7, 3, 5, 5, 7, 3, 5, 5, 3, 3, 3, 3, 0, 6, 4, 2, 1, 6, 9, 8, 9, 0, 9, 2, 8, 1, 8, 4, 6, 8, 9, 1, 8, 8, 2, 0, 4, 2, 0, 0, 8, 1, 0, 1, 1, 0, 0, 2, 8, 4, 1, 1, 4, 6, 6, 2, 6, 6, 4, 6, 4, 4, 2, 2, 9, 9, 9, 9]
    roundlist = [0, 0, 1, 1, 2, 3, 2, 3, 0, 1, 4, 5, 6, 2, 4, 5, 7, 3, 6, 7, 4, 5, 6, 7, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 2, 2, 2, 3, 3, 4, 6, 3, 5, 4, 5, 6, 7, 4, 7, 3, 6, 7, 4, 3, 4, 5, 5, 6, 5, 7, 6, 7, 6, 7, 4, 5, 6, 7]

    colorlist = []
    for i in range(3):
        randomColor = lambda: random.randint(0, 255)
        randomColor = '#{:02x}{:02x}{:02x}'.format(randomColor(), randomColor(), randomColor())
        colorlist.append(randomColor)

    print(colorlist)


    count = 0
    for task in tasklist:
        if task == 0:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 1:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 2:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 3:
            plt.plot(count, task, 'o-', color=colorlist[0])
        if task == 4:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 5:
            plt.plot(count, task, 'o-', color=colorlist[1])
        if task == 6:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 7:
            plt.plot(count, task, 'o-', color=colorlist[2])
        if task == 8:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        if task == 9:
            plt.plot(count, task, 'o-', color="#CDCBC8")
        count += 1
    #plt.plot(tasklist, roundlist, 'o-', color=randomColor)
    #plt.legend(loc=1, prop={'size': 10})

    plt.title(plotname, fontsize=20)
    plt.tick_params(axis='x', which='major', labelsize=10)
    plt.tick_params(axis='y', which='major', labelsize=10)
    plt.xlabel('Runde', fontsize=20)
    plt.ylabel('Task', fontsize=20)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('exp3_5Agenten_10Tasks_3Premium')
    plt.show()

plotSomeWalk("Exp. 3: 5 Agenten, 10 Tasks")
'''

'''
def plotSomeWalk(data, plotname):
    for entry in data:
        x_axis = np.arange(len(entry))
        randomColor = lambda: random.randint(0, 255)
        randomColor = '#{:02x}{:02x}{:02x}'.format(randomColor(), randomColor(), randomColor())
        plt.plot(x_axis, entry, 's-', color=randomColor)

    plt.legend(loc=4, prop={'size': 15})


    plt.title(plotname, fontsize=20)
    plt.tick_params(axis='x', which='major', labelsize=10)
    plt.tick_params(axis='y', which='major', labelsize=10)
    plt.xlabel('TODO X ACHSE', fontsize=20)
    plt.ylabel('TODO Y ACHSE', fontsize=20)
    plt.grid(True)
    plt.tight_layout()
    #pathToLog = 'src/HA02_AOT/Plots'
    #placeToSave = os.path.join(os.path.dirname(os.path.abspath(__file__)), pathToLog)
    plt.savefig('exp1_100Agenten_50Tasks')
    plt.show()

plotSomeWalk()
'''

''' EXPERIMENT 1 '''
''' TASK: 49 '''
list = [
[8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 5.0],
[8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 2.0],
[14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 4.0],
[7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
[13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 1.0],
[6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0],
[6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 4.0],
[6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 7.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
[11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 2.0],
[9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 6.0],
[13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 4.0],
[16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 1.0],
[21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 5.0],
 [18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 6.0],
[5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.0],
 [15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 7.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 4.0],
 [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 8.0],
 [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 7.0],
 [13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 3.0],
 [12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 4.0],
 [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.0],
 [15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 2.0],
[12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 5.0],
 [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 5.0],
[14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 3.0],
 [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
[8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 2.0],
[18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 3.0],
 [14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 4.0],
 [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 7.0],
[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
 [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 2.0],
 [13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 5.0],
[9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 3.0],
[5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 2.0],
 [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 7.0],
 [19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 4.0],
 [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 4.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 6.0],
 [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 3.0],
 [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 5.0],
[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0],
[11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 2.0],
 [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 1.0],
 [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 4.0],
 [12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 4.0],
[7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 3.0],
 [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0],
[18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 4.0],
[17.0, 17.0, 17.0, 17.0, 17.0, 17.0, 17.0, 17.0, 17.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 4.0],
[14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 4.0],
[15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 3.0],
[18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 4.0],
 [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 6.0],
[12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 8.0],
 [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 2.0],
[16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 3.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.0],
[16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 1.0],
[9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 4.0],
[14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 6.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 4.0],
[12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 2.0],
[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 2.0],
[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 5.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 8.0],
 [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 4.0],
 [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 2.0],
[16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 3.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.0],
[12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 7.0],
[13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 2.0],
[9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 2.0],
 [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 5.0],
 [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.0],
[7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 3.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
[20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 8.0],
 [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 5.0],
 [12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 4.0],
 [11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 5.0],
 [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 3.0],
 [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0],
 [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 2.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 3.0],
[12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 3.0],
 [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 3.0],
 [21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 5.0],
[9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 5.0],
[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 6.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0],
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 5.0]
]

#plotSomeWalk(list, 'Exp. 1, 100 Agenten, 50 Tasks')
''' ENDE EXPERIMENT 1 '''