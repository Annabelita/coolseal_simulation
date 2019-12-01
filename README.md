# Overview
This project implements a simulation of simple reactive agents. We used swarm intelligence (Ant-Colony-Optimization) to solve a NP hard problem
(given certain parameters). The full results are available in our research paper. 

<br>
<br>

# Requisitions

* Python 3.6 oder higher
* Pycharm IDEA
* pip install pygame --upgrade 
* pip install numpy --upgrade
* Other packages: matplotlib, reportlab

<br>
<br>

# Project Installation

```
git clone
```
the project onto your desktop.

Make sure to have all libraries install _(either through pip install or in install in your VM through Project Interpreter)_

<br>
<br>

# Starting the Simulation

* Start PyCharm
* Run __main.py__ in __src/main__.
* Parameters can be changed in __settings.py__.
* During the simulation a __log.txt__ file is created.
* After succesful execute a PDF file is created, summarizing and automatically analysing the log file. This file also contains a summary plot.
* To end the simulation press __Escape (ESC)__.
* To pause the simulation press __Space/Spacebar__. 
* To re-start the simulation press __Space/Spacebar__ again.
* To create new houses during runtime __left-click__ with your cursor in a arbitrary street field (black field).


<br>
<br>

# Changing the Simulation Environment



* Changing the area: Edit __area.txt__.
* The field is limited to 34x26 fields (adapted to a window size of 1024x786px)
* The visible are is limited to 34x26 fields. The other fields build the frame of the simulation world.
*  __H__ represents a house. (Houses can't be passed by agents)
* __A__ represents the start position of an agent. (for each start position **ANT_AMOUNT** (see settings.py) are created).
* __E__ represents a black street than can be passed by agents.
* __All other symbols will not create a valid area!!!__

<img src="https://github.com/Annabelita/coolseal_simulation/blob/master/readmeImg/area.png" width="400">


<br>
<br>

# Log Files


* Important: The Simulation must not be stopped manually => This will create infinit loops during the automatic analysis.
* After termination the log is analysed automatically.
* The Analysis report is saved in __sr/Results__.
* Ever valid log.txt file ends with a row containing the word __"ENDE"__.


<img src="https://github.com/Annabelita/coolseal_simulation/blob/master/readmeImg/log.png" width="500">


<br>
<br>

# Videos
* Simulation __videos__ are available in our research paper.

<br>
<br>

### log.txt
Documents....
* ... start params: Exploration-Algorithm, Amount of agents
* ... % of colored streets per 10 time frames.
* ... dying agents and amount of remaining agents.
* ... after simulation end: Area colored succesfully? (yes/no). Duration in seconds. 

<br>
<br>

### Automated Analysis (PDF)
Documents ...
* ... Aggregation of the maximum amount of steps as well as the percentage of colored streets for each simulation. 
* ... Returns the maximum percentage of colored streets as well as how many steps the "best path" required.
* ... average amount of steps.
* ... average percentage of colored streets of all simulations. 
* ... a plot containing all paths. The best path is highlighted (see our research paper for the definition of the "best path")


Example: Best Path is marked green

<img src="https://github.com/Annabelita/coolseal_simulation/blob/master/readmeImg/best_path.png" width="400">

<br>
<br>

# Folder structure
* __src/Analysis/logFiles__: contains all __log.txt__ files
* __src/Analysis/Plots__: contains all plots
* __src/Results__: contains all PDF reports
* At the beginning of each simulation the __log.txt__ file is overwritten. If you want to save this file please rename it before you re-run the simulation!
* Naming of the logfile: __ExplorationAlgorithm-#Agents-Startposition__
* Startpositions: __or == upper right__, __ul = lower left__, __ol = upper left__, __or = upper right__
* _Example: SimpleWalk-1-or means the algorithm was SimpleWalk, there was 1 Agents and the start position was the upper right corner_

<br>
<br>

# Further Analysis

## Comparison of SimpleWalk and RandomWalk

x-axis: Amount of steps

y-axis: percentage of colored streets

<img src="https://github.com/Annabelita/coolseal_simulation/blob/master/readmeImg/algorithms.png" width="500">

<br>
<br>


## Comparison of different amount of agents

x-axis: Amount of steps

y-axis: percentage of colored streets

<img src="https://github.com/Annabelita/coolseal_simulation/blob/master/readmeImg/comparison.png" width="500"> 

