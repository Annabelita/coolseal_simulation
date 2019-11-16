"""
Defines simulator environment
@author Andrej Savinov, Annabella Kadavanich, Isabel Schmuck
"""
import sys
import random
from src.sprites import *
from os import path
import logging
import numpy as np
import time


class Simulator:
    # Constructor
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_area()


    # FOR LOGGING:
    def getWalkTypForLog(self, flag):
        if flag == 0:
            logging.info("Walk: RandomWalk")
        elif flag == 1:
            logging.info("Walk: SimpleWalk")
        elif flag == 2:
            logging.info("Walk: Multiple Depth First Search")

    # Loop to run the simulator
    def run(self,walk):
        self.running = True
        self.pause = False
        #loglist = np.arange(0,1000,10)
        #loglist.tolist()
        start = time.clock()

        while self.running:

            # Update simulationstep
            self.simulationStep += 1
            # Wait for FPS amount
            self.dt = self.clock.tick(FPS)
            # Process user input
            self.events()
            # Process sprite events and simulation events
            flag = self.update(walk)
            # -------------------------- LOGGING -------------------------------
            if self.simulationStep == 1:
                self.getWalkTypForLog(flag)
                logging.info(f'Amount of ants: {len(self.ants)}')
                logging.info('\n')

            #if self.simulationStep in loglist:
            logging.info(self.calculateColoredPercent())



            # ------------------------------------------------------------------
            # Draw everything onto the screen
            self.draw()
            # Check if all streets are colored
            if self.isAllColored():
                self.running = False
                end = time.clock();
                logging.info('End of Simulation.')
                logging.info('Status: All streets colored!')
                logging.info(f'Total duration: {end-start}s.')
                logging.info('---------------------- END OF SIMULATION ----------------------------')
                logging.info('\n\n\n\n')
                break

            if len(self.ants) == 0:
                end = time.clock()
                self.running = False
                logging.info('End of Simulation. All ants dead.')
                logging.info('Status: Not all streets could be colored completely.')
                logging.info(f'{self.calculateResultInPercent()}% of the streets were colored.')
                logging.info(f'Total duration: {end-start}s.')
                logging.info('---------------------- END OF SIMULATION ----------------------------')
                logging.info('\n\n\n\n')

        print(self.calculateColoredPercent())


    # Update sprites and simulation process
    def update(self,walk):
        # ------------------------ CHOOSE YOUR WALK HERE ----------------------------
        if walk == 0:
            self.randomWalk()
            flag = 0
        elif walk == 1:
            self.simpleWalk()
            flag = 1
        elif walk == 2:
            self.multipleDFS()
            flag = 2
        # --------------------------------------------------------------------------
        #print(self.calculateColoredPercent())
        self.all_sprites.update()
        return flag



    # creates a new ant on a rando, black field (stage == 0)
    def createNewRandomAnt(self):
        l = []
        color = ANT
        for street in self.streets:
            if street.getStage() == 0:
                l.append(street)
        if l == []:
            for street in self.streets:
                if street.getStage() == 1:
                    l.append(street)
            color = TURQUOISE;

        if l == []:
            for street in self.streets:
                if street.getStage() == 2:
                    l.append(street)
            color = WATERMELON;

        if l == []:
            self.running = False



        randomStreet = random.choice(l)

        x = randomStreet.x
        y = randomStreet.y

        antNew = Ant(self, x, y)
        # TODO: Color only new created ant differently
        antNew.image.fill(color)


    # All ants in ant_list will perform a random walk
    def randomWalk(self):
        for currentAnt in self.ants:
            nearbyStreets = self.getNearbyStreets(currentAnt)

            # Color current street standing on
            for street in self.streets:
                 if street.position == currentAnt.position:
                     self.colorStreet(street)

            # Remove all Stage_2 streets from the list
            for street in nearbyStreets[:]:
                if street.getStage() == StreetStage_2:
                    #print("DURING: ",street.getStage())
                    nearbyStreets.remove(street)

            # If list is empty after cleaning, kill ant
            if not nearbyStreets:
                currentAnt.kill()
                currentAnt = None
                #print("DEAD")
                logging.info('########################### Ant died!')
                logging.info(f'########################### remaining ants: {len(self.ants)}')

                #self.createNewRandomAnt()
                continue

            # Select random street
            selectedStreet = random.choice(nearbyStreets)

            sx, sy = selectedStreet.position
            currentAnt.move(sx,sy)

    # All ants will perform a simple walk (choose streets next to them to paint)
    def simpleWalk(self):
        for currentAnt in self.ants:
            nearbyStreets = self.getNearbyStreets(currentAnt)
            selectedStreet = self.streetSelector(nearbyStreets)

            # Color current street standing on
            for street in self.streets:
                if street.position == currentAnt.position:
                    self.colorStreet(street)

            # If in a dead end, kill ant
            if selectedStreet == None:
                currentAnt.kill()
                currentAnt = None
                #print("DEAD")
                logging.info('########################### Ant died!')
                logging.info(f'########################### remaining ants: {len(self.ants)}')

                #self.createNewRandomAnt()
                continue

            # TODO: cx, cy just for testing, can be removed
            cx, cy = currentAnt.position
            sx, sy = selectedStreet.position
            #print(f"Ant position: X={cx} Y={cy}")
            #print(f"Street position: X={sx} Y={sy}")
            currentAnt.move(sx,sy)

    # Multiple Depth First Search as presented in: Brick&Mortar: an on-line multi-agent exploration algorithm by Ettore Ferranti, Niki Trigoni, Mark Levene
    def multipleDFS(self):
        for currentAnt in self.ants:
            nearbyStreets = self.getNearbyStreets(currentAnt)
            selectedStreet = None
            if currentAnt.moved == False:
                streetMove = self.streetSelector(nearbyStreets)
                currentAnt.move(streetMove.x, streetMove.y)
                currentAnt.moved = True

            for street in self.streets:
                if street.position == currentAnt.position:
                    # First if in Algorithm
                    if street.getStage() == StreetStage_0:
                        self.colorStreet(street)
                        street.setID(currentAnt.getID())
                        #If we are at the Start of our Simulation
                        if currentAnt.getLastPos() == None:
                            currentAnt.setLastPos(currentAnt.position)
                        else:
                            street.setParentPos(currentAnt.getLastPos())
                            #print("#############################################################")
                            #print("ANT LAST POS: ",currentAnt.getLastPos())
                            #print("ANT CURRENT POS: ", currentAnt.position)
                            #print("Streets PARENT POS: ",street.getParentPos())
                            currentAnt.setLastPos(currentAnt.position)
                    # Second if in Algorithm
                    if self.getMinStage(nearbyStreets) == 0:
                        selectedStreet = self.streetSelector(nearbyStreets)
                        currentAnt.move(selectedStreet.x,selectedStreet.y)
                    else:
                        if street.getID() == currentAnt.getID():
                            self.colorStreet(street)
                            if(street.getParentPos() == None):
                                currentAnt.kill()
                                currentAnt = None
                                # print("DEAD")
                                logging.info('########################### Ant died!')
                                logging.info(f'########################### remaining ants: {len(self.ants)}')
                                # self.createNewRandomAnt()
                                break
                            x, y = street.getParentPos()
                            currentAnt.setLastPos((x,y))
                            currentAnt.move(x,y)
                        else:
                            selectedStreet = self.streetSelector(nearbyStreets)
                            if selectedStreet == None:
                                currentAnt.kill()
                                currentAnt = None
                                # print("DEAD")
                                logging.info('########################### Ant died!')
                                logging.info(f'########################### remaining ants: {len(self.ants)}')
                                # self.createNewRandomAnt()
                                break
                            currentAnt.move(selectedStreet.x, selectedStreet.y)

    # Brick&Mortar Algorithm by Ettore Ferranti, Niki Trigoni, Mark Levene as presented in: Brick&Mortar: an on-line multi-agent exploration algorithm
    def brickMortar(self):
        for currentAnt in self.ants:
            nearbyStreets = self.getNearbyStreets(currentAnt)

            # Without a proper pathfinding algorithm to check if there is a path from A to B (according to Paper) this wont work properly
            # But since our ants have a limited memory , it is not possible to let them use a proper pathfinding algorithm,
            # since they won't be reactive anymore (Memory and processing ouf pathfinding would be too high)
            # So brick&Mortar fails in this case
            # Marking Step
            for street in self.streets:
                if street.position == currentAnt.position:
                    if self.isNotBlocking(street,currentAnt):
                        self.colorStreetToStage(street,StreetStage_2)
                    else:
                        self.colorStreetToStage(street,StreetStage_1)

            # Navigation Step
            stage0Streets = []
            for street in nearbyStreets:
                if street.getStage() == StreetStage_0:
                    stage0Streets.append(street)

            stage1Streets = []
            for street in nearbyStreets:
                if street.getStage() == StreetStage_1:
                    stage1Streets.append(street)

            x, y = (0,0)
            if len(stage0Streets) != 0:
                selectedStreet = None
                maxBlock = None
                for street in stage0Streets:
                    if selectedStreet == None:
                        selectedStreet = street
                        maxBlock = self.getNearbyBlockingAmount(street)
                    elif self.getNearbyBlockingAmount(street) > maxBlock:
                        selectedStreet = street
                        maxBlock = self.getNearbyBlockingAmount(street)

                x,y = selectedStreet.position
            # TODO ADD AVOIDANCE
            elif len(stage1Streets) != 0:
                selectedStreet = random.choice(stage1Streets)
                x,y = selectedStreet.position

            else:
                currentAnt.kill()
                currentAnt = None
                print("DEAD")
                logging.info('########################### Ant died!')
                logging.info(f'########################### remaining ants: {len(self.ants)}')
                continue

            currentAnt.move(x, y)

    # Check if the given street is not blocking path between any stage_0/1 streets around
    def isNotBlocking(self, currentStreet, currentAnt):
        nearbyStreets = self.getNearbyStreets(currentAnt)

        # Go trough all nearbyStreets of the currentAnt and check if they can be accessed trough a different path
        for streetToCheck in nearbyStreets:
            blockList = []
            # Ignore stage_2 Streets, they are finished
            if streetToCheck.getStage() == StreetStage_2:
                continue
            # Go trough all nearbyStreets of the streetToCheck and check their status,
            # to find if its possible to access the StreetToCheck from another path
            else:
                nearbyStreetsToCheck = self.getNearbyStreets(streetToCheck)
                for street in nearbyStreetsToCheck:
                    if street.position == currentStreet.position:
                        continue
                    elif street.getStage() == StreetStage_2:
                        blockList.append(True)
                    elif street.getStage() == StreetStage_0 or street.getStage() == StreetStage_1:
                        blockList.append(False)
            # Check if its possible to access the StreetToCheck
            if True in blockList:
                if False in blockList:
                    continue
                else:
                    return False

        # All streets around are already painted or no nearbyStreet gets blocked
        return True

    # Returns the number of all non StreetStage_2/House nearbystreets for given street
    def getNearbyBlockingAmount(self,curStreet):
        areaHouses = []
        amount = 0

        for house in self.houses:
            areaHouses.append(house.position)

        for street in self.streets:
            if (street.position == (curStreet.x-1,curStreet.y) and curStreet.x - 1 != -1 and (curStreet.x - 1, curStreet.y) in areaHouses) or \
                    (street.position == (curStreet.x-1,curStreet.y) and curStreet.x - 1 != -1 and street.getStage() == StreetStage_2):
                amount += 1
            if (street.position == (curStreet.x, curStreet.y - 1) and curStreet.y - 1 != -1 and (curStreet.x, curStreet.y - 1) in areaHouses) or \
                    (street.position == (curStreet.x, curStreet.y - 1) and curStreet.y - 1 != -1 and street.getStage() == StreetStage_2):
                 amount += 1
            if (street.position == (curStreet.x + 1, curStreet.y) and curStreet.x + 1 != 32 and (curStreet.x + 1, curStreet.y) in areaHouses) or \
                    (street.position == (curStreet.x + 1, curStreet.y) and curStreet.x + 1 != 32 and street.getStage() == StreetStage_2):
                amount += 1
            if (street.position == (curStreet.x, curStreet.y + 1) and curStreet.y + 1 != 24 and (curStreet.x, curStreet.y + 1) in areaHouses) or \
                    (street.position == (curStreet.x, curStreet.y + 1) and curStreet.y + 1 != 24 and street.getStage() == StreetStage_2):
                amount += 1
        return amount

    # Selects the best street from a list to paint
    def streetSelector(self, nearbyStreets):
        #print(f"All nearby streets: {nearbyStreets}")
        selectedStreet = None
        minStage = self.getMinStage(nearbyStreets)

        # All streets are Stage 2
        if minStage == None:
            return None

        # Remove all streets which dont have the min stage
        for street in nearbyStreets[:]:
            if street.getStage() != minStage:
                nearbyStreets.remove(street)

        # Select a random street
        selectedStreet = random.choice(nearbyStreets)

        return selectedStreet

    # Gets the smallest Stage for given streets
    def getMinStage(self,nearbyStreets):
        minStage = 2

        # Select lowest stage
        for street in nearbyStreets:
            if street.getStage() < minStage:
                minStage = street.getStage()

        # Stage = 2 means no possible street found
        if minStage == 2:
            minStage = None

        return minStage

    # Calculates the percentage of colored streets
    def calculateColoredPercent(self):
        if self.streetsColored == 0:
            return f"Step: {self.simulationStep} -------- Percentage of colored Streets: 0.00%"
        else:
            percent = (round(((self.streetsColored * 1.0) / self.amountToColor),2)*100)
            percent = float('{0:.2f}'.format(percent))

            return f"Step: {self.simulationStep} -------- Percentage of colored Streets: {percent}%"

        # Calculates the result percentage of colored streets
    def calculateResultInPercent(self):
        percent = round(((self.streetsColored * 1.0) / self.amountToColor), 2) * 100
        return percent

    # Pause the simulator
    def pauseSimulator(self):
        while self.pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_SPACE:
                        self.pause = False

    # Draw everything needed for the start / at the end of each run loop
    def draw(self):
        #self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.ants.draw(self.screen)
        self.startingPos.draw(self.screen)
        pg.display.flip()

    # Draw grid for the simulator
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))





        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    # Catch all events
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            # Create House at Position and delete Street
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                x, y = (int)(x/TILESIZE), (int)(y/TILESIZE)
                for street in self.streets:
                    if street.position == (x,y):
                        street.kill()
                        street = None
                        self.streetsColored += 2
                        self.streetsToColor -= 2
                House(self, x, y, house_2IMG)
                logging.info("New House at y: " + str(y) + ", x: " + str(x))
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_SPACE:
                    self.pause = True
                    self.pauseSimulator()
                if event.key == pg.K_DELETE:
                    self.removeAnt()


    #removes single ant from simulation
    def removeAnt(self):
        for currAnt in self.ants:
            currAnt.kill()
            logging.info("Ant was removed from field!")
            break


    # Colors the given street and updates streets stage
    def colorStreetToStage(self,street,stageToSet):
        stage = street.getStage()
        if stage == StreetStage_0:
            if stageToSet == StreetStage_1:
                street.setStage(StreetStage_1, street_1IMG)
                self.streetsToColor -= 1
                self.streetsColored += 1
            elif stageToSet == StreetStage_2:
                street.setStage(StreetStage_2, street_2IMG)
                self.streetsToColor -= 2
                self.streetsColored += 2
        elif stage == StreetStage_1:
            if stageToSet == StreetStage_1:
                pass
            elif stageToSet == StreetStage_2:
                street.setStage(StreetStage_2, street_2IMG)
                self.streetsToColor -= 1
                self.streetsColored += 1
        else:
            return "Not possible"

    # Colors the given street and updates streets stage
    def colorStreet(self,street):
        stage = street.getStage()
        if stage == StreetStage_0:
            street.setStage(StreetStage_1,street_1IMG)
            self.streetsToColor -= 1
            self.streetsColored +=1
        elif stage == StreetStage_1:
            street.setStage(StreetStage_2,street_2IMG)
            self.streetsToColor -= 1
            self.streetsColored += 1
        else:
            return "Not possible"

    # Gets the adjacent streets for the current ant
    def getNearbyStreets(self,curAnt):
        areaHouses = []
        nStreets = []

        for house in self.houses:
            areaHouses.append(house.position)

        for street in self.streets:
            if street.position == (curAnt.x-1,curAnt.y) and curAnt.x - 1 != -1 and (curAnt.x - 1, curAnt.y) not in areaHouses:
                nStreets.append(street)
            if street.position == (curAnt.x, curAnt.y - 1) and curAnt.y - 1 != -1 and (curAnt.x, curAnt.y - 1) not in areaHouses:
                 nStreets.append(street)
            if street.position == (curAnt.x + 1, curAnt.y) and curAnt.x + 1 != 32 and (curAnt.x + 1, curAnt.y) not in areaHouses:
                nStreets.append(street)
            if street.position == (curAnt.x, curAnt.y + 1) and curAnt.y + 1 != 24 and (curAnt.x, curAnt.y + 1) not in areaHouses:
                nStreets.append(street)

        return nStreets

    # Check if all streets are colored
    def isAllColored(self):
        if self.streetsToColor == 0:
            return True
        else:
            return False

    # Close the simulator
    def quit(self):
        pg.quit()
        sys.exit()

    # Initialize everything needed for the simulator
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.houses = pg.sprite.Group()
        self.ants = pg.sprite.Group()
        self.streets = pg.sprite.Group()
        self.startingPos = pg.sprite.Group()
        self.streetsToColor = 0
        self.streetsColored = 0
        self.simulationStep = 0
        antID = 0

        for y, line in enumerate(self.area):
            for x, character in enumerate(line):
                if character == 'H':
                    House(self, x - 1, y - 1, house_1IMG)
                elif character == 'E':
                    Street(self, x - 1, y - 1)
                    self.streetsToColor += 2
                elif character == 'A':
                    StartingPosition(self, x - 1, y - 1)
                    for i in range(0,ANT_AMOUNT):
                        Ant(self, x - 1, y - 1, antID)
                        antID +=1

        self.amountToColor = self.streetsToColor


    # Load area for the simulator
    def load_area(self):
        simulator_folder = path.dirname(__file__)
        self.area = []
        with open(path.join(simulator_folder, 'area.txt'), 'rt') as i:
            for line in i:
                self.area.append(line)

    # Show the starting screen
    def show_start_screen(self):
        pass

    # Visualize all Import information
    def show_log_screen(self):
        pass
