"""
Main to execute Simulator code
@author Andrej Savinov, Annabella Kadavanich, Isabel Schmuck
"""
from src.simulator import *
import logging
from src.logData import *
import time


# Create simulator object
simulator = Simulator()
simulator.show_start_screen()
counter = 0
log = 'log.txt'
open(log, 'w').close()
while True:
    if counter == SIMULATIONROUNDS:
        break
    log = "log.txt"

    logging.basicConfig(filename=log, level=logging.DEBUG, format='%(message)s')
    logging.info('---------------------- START OF SIMULATION ----------------------------')
    #logging.basicConfig(filename=log, level=logging.DEBUG, format='%(asctime)s %(message)s',
    #                    datefmt='%d/%m/%Y %H:%M:%S')
    logging.info('Simulation started.')
    simulator.new()
    simulator.run(WALK)
    #simulator.show_log_screen()
    counter +=1
logging.info('ENDE')

if WALK ==  2:
    bestPercentage, bestStep = plotSomeWalk(log, 110, 1000, '#4E87CF', '#043A7E', False)
else:
    bestPercentage, bestStep = plotSomeWalk(log, 100, 400, '#4E87CF', '#043A7E', False)
createPDF(log, bestPercentage, bestStep)
