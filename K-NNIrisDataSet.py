### Course: CS 4267
### Student Name: Devin Ogle
### Student Id: 000756886
### Assignment #: 1
### Due Date: September 16, 2019
### Signature: ??
### Score: ??
##
###IMPORTANT NOTES:
##    # Split each the data for each species 50/50
##        # 50%: training data
##        # 50%: test data
##        # Note Status: Complete 8-29-2019
##    
##    #Add functionality to calculate distance using four points
##       # Note Status: Complete 8-29-2019
##
##    # current line causing error:
##        # ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']
##    
##
##
### following code takes data from iris.data and loads it into sampleData
##count = 0
##with open('C:/Users/Dogle/Documents/Class/iris.data')  as ins:
##    sampleData = []
##    for line in ins:
##        count = count + 1
##        temp = line.replace('\n', '')
##        temp = temp.split(',')
##        sampleData.append(temp)
##
##sampleData.remove(sampleData[len(sampleData)-1])# remove empty element from array
##
### take half of the data for each species in sampleData and put it in a testingDataArray and trainingDataArray respectivly
##
##testingDataArray = []
##trainingDataArray = []
##
##for x in range( 0, 25): # adding half of Iris-setosa data to testingDataArray
##    testingDataArray.append( sampleData[x] )
##    
##for x in range( 50, 75): # adding half of Iris-versicolor data to testingDataArray
##    testingDataArray.append( sampleData[x] )
##    
##for x in range( 100, 125): # adding half of Iris-virginica data to testingDataArray
##    testingDataArray.append( sampleData[x] )
##     
##for x in range( 25, 50): # adding half of Iris-setosa data to trainingDataArray
##    trainingDataArray.append( sampleData[x] )
##    
##for x in range( 75, 100): # adding half of Iris-versicolor data to testingDataArray
##    trainingDataArray.append( sampleData[x] )
##    
##for x in range( 125, 150): # adding half of Iris-virginica data to testingDataArray
##    trainingDataArray.append( sampleData[x] )
##
##for x in range( 0, len(trainingDataArray) ): #appending space on end of each line in trainingDataArray to hold distances
##    trainingDataArray[x].append('')
##
###print(trainingDataArray)
##
###Implement K-NN Algo to solve: Iris Data set and data set of our choice
##
### Step 1: Determine parameter K= number of nearest neighbors
##k = 3 # usually odd, can be my choice.
##
##
##
###var
##distanceArray = []
##
### print(distanceArray)
##
### Step 2: Calculate the distance between the query-instance and all the training examples.
### calulates distance and appends distance to end of each element, distance can be located using...
### trainingDataArray[0][5]
##def calMinDistance (trainingDataArray, distanceArray, queryInstance):
##    count = 0
##    for line in trainingDataArray:
##
##            # queryInstance will be X2,Y2,Z2
##            # trainingDataArray will be X1, Y1, Z1
##            x = intermidiateDistanceOperation( line[0] ,queryInstance[0] )
##            y = intermidiateDistanceOperation( line[1] ,queryInstance[1] )
##            z = intermidiateDistanceOperation( line[2] ,queryInstance[2] )
##            w = intermidiateDistanceOperation( line[3] ,queryInstance[3] )
##
##            
##            distance = (x + y + z) # sum all vars
##            distance = distance ** 0.5 # square root sum of all values
##
##            #add value to distanceArray
##            trainingDataArray[count][5] = distance 
##            count = count + 1
##    
##            # print(distance)
##
### returns value = ( X2 - X1)^2
##def intermidiateDistanceOperation ( value1, value2):
##
##    # convert string values to float
##    v1 = float( value1 )
##    v2 = float( value2 )
##    
##    temp = v2 - v1
##    temp = temp ** 2 # square value
##
##    return temp
##
##    
##    
##
##
##
##
### Step 3: Sort the distance and determine nearest neighbors based on the k-th minimum distance.
##
##def sortDistanceArray(dataArray):
##    tempArray = dataArray;
##    for cursor in range( 0, len(tempArray) ):
##        for element in range( 0, len(tempArray) ):
##            tempElement = float( tempArray[cursor][5] )
##            tempCursor = float( tempArray[element][5] )
##
##            if tempElement < tempCursor: # element is less then cursor, swap them
##                temp = tempArray[cursor]
##                tempArray[cursor] = tempArray[element]
##                tempArray[element] = temp
##    return tempArray
##
### input should be an alreay sorted trainingDataArray, pushes first three elements from trainingDataArray into...
### the a tempArray
### returns array of nearest neighbors
##def findNearest( dataArray ) :
##    tempArray = []
##    tempArray.append( dataArray[0] )
##    tempArray.append( dataArray[1] )
##    tempArray.append( dataArray[2] )
##
##    return tempArray
##
##    
### Step 4: Gather the category Y of the nearest neighbors.
### Step 5: Use simple majority of the category of nearest neighbors as the prediction value of the query distance.
##
##def determineCatagory( dataArray ):
##    setosaCount = 0
##    versicolorCount = 0
##    virginicaCount = 0
##
##
##    
##    for x in range( 0, len(dataArray) ):
##        
##        if dataArray[x][4] == 'Iris-setosa':
##            setosaCount = setosaCount + 1
##            
##        if dataArray[x][4] == 'Iris-versicolor':
##            versicolorCount = versicolorCount + 1
##            
##        if dataArray[x][4] == 'Iris-virginica':
##            virginicaCount = virginicaCount + 1
##
##    # print counts to console            
##    print( 'Counts: ','\n  setosaCount:', setosaCount, '\n  versicolorCount:', versicolorCount, '\n  virginicaCount:', virginicaCount )
##
##    if ( setosaCount > versicolorCount and setosaCount > virginicaCount ): # if setosaCount is largest
##        print( 'Guess: Iris-setosa!')
##        
##    if ( versicolorCount > setosaCount and versicolorCount > virginicaCount ): # if versicolorCount is largest
##        print( 'Guess: Iris-versicolor!')
##        
##    if ( virginicaCount > setosaCount and virginicaCount > versicolorCount ): # if virginicaCount is largest
##        print( 'Guess: Iris-virginica!')
##        
##    if ( virginicaCount == setosaCount and virginicaCount == versicolorCount ): # if all are equal
##        print( 'Cannot be determined')
##
##def runProgram( trainingData, distanceArray,  testData ):
##    tempArray = []
##    count=0
##    for line in testData:
##
##        #reset values
##        tempTrainingData = trainingData
##        tempDistanceData = distanceArray
##        tempTestData = testData
##        tempArray = []
##        
##        # adding values to tempArray
##        tempArray.append( line[0] )
##        tempArray.append( line[1] )
##        tempArray.append( line[2] )
##        tempArray.append( line[3] )
##        print( '==============================')
##        print( '\nInput Data: ', tempArray )
##
##        calMinDistance( tempTrainingData , tempDistanceData, tempArray )
##        tempDistanceData = sortDistanceArray( tempTrainingData )
##        neighborArray = findNearest( tempDistanceData )
##        determineCatagory ( neighborArray )
##    
##        print( 'Correct answer: ', line[4] )
##        print( '\n==============================')
##
##
##runProgram( trainingDataArray, distanceArray, testingDataArray )



# Course: CS 4267
# Student Name: Devin Ogle
# Student Id: 000756886
# Assignment #: 1
# Due Date: September 16, 2019
# Signature: ??
# Score: ??

#IMPORTANT NOTES:
    # Split each the data for each species 50/50
        # 50%: training data
        # 50%: test data
        # Note Status: Complete 8-29-2019
    
    #Add functionality to calculate distance using four points
       # Note Status: Complete 8-29-2019

    # current line causing error:
        # ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']

    
##===============================================================================================
##===============================================================================================
##    ADDING GUI AND PERFORMANCE METRICS
##===============================================================================================
##===============================================================================================

# following code takes data from iris.data and loads it into sampleData
count = 0
with open('C:/Users/Dogle/Documents/Class/iris.data')  as ins:
    sampleData = []
    for line in ins:
        count = count + 1
        temp = line.replace('\n', '')
        temp = temp.split(',')
        sampleData.append(temp)

sampleData.remove(sampleData[len(sampleData)-1])# remove empty element from array

# take half of the data for each species in sampleData and put it in a testingDataArray and trainingDataArray respectivly

testingDataArray = []
trainingDataArray = []

for x in range( 0, 25): # adding half of Iris-setosa data to testingDataArray
    testingDataArray.append( sampleData[x] )
    
for x in range( 50, 75): # adding half of Iris-versicolor data to testingDataArray
    testingDataArray.append( sampleData[x] )
    
for x in range( 100, 125): # adding half of Iris-virginica data to testingDataArray
    testingDataArray.append( sampleData[x] )
     
for x in range( 25, 50): # adding half of Iris-setosa data to trainingDataArray
    trainingDataArray.append( sampleData[x] )
    
for x in range( 75, 100): # adding half of Iris-versicolor data to testingDataArray
    trainingDataArray.append( sampleData[x] )
    
for x in range( 125, 150): # adding half of Iris-virginica data to testingDataArray
    trainingDataArray.append( sampleData[x] )

for x in range( 0, len(trainingDataArray) ): #appending space on end of each line in trainingDataArray to hold distances
    trainingDataArray[x].append('')

#print(trainingDataArray)

#Implement K-NN Algo to solve: Iris Data set and data set of our choice

# Step 1: Determine parameter K= number of nearest neighbors
k = 3 # usually odd, can be my choice.



#var
distanceArray = []

# print(distanceArray)

# Step 2: Calculate the distance between the query-instance and all the training examples.
# calulates distance and appends distance to end of each element, distance can be located using...
# trainingDataArray[0][5]
def calMinDistance (trainingDataArray, distanceArray, queryInstance):
    count = 0
    for line in trainingDataArray:

            # queryInstance will be X2,Y2,Z2
            # trainingDataArray will be X1, Y1, Z1
            x = intermidiateDistanceOperation( line[0] ,queryInstance[0] )
            y = intermidiateDistanceOperation( line[1] ,queryInstance[1] )
            z = intermidiateDistanceOperation( line[2] ,queryInstance[2] )
            w = intermidiateDistanceOperation( line[3] ,queryInstance[3] )

            
            distance = (x + y + z + w) # sum all vars
            distance = distance ** 0.5 # square root sum of all values

            #add value to distanceArray
            trainingDataArray[count][5] = distance 
            count = count + 1
    
            # print(distance)

# returns value = ( X2 - X1)^2
def intermidiateDistanceOperation ( value1, value2):

    # convert string values to float
    v1 = float( value1 )
    v2 = float( value2 )
    
    temp = v2 - v1
    temp = temp ** 2 # square value

    return temp

    
    




# Step 3: Sort the distance and determine nearest neighbors based on the k-th minimum distance.

def sortDistanceArray(dataArray):
    tempArray = dataArray;
    for cursor in range( 0, len(tempArray) ):
        for element in range( 0, len(tempArray) ):
            tempElement = float( tempArray[cursor][5] )
            tempCursor = float( tempArray[element][5] )

            if tempElement < tempCursor: # element is less then cursor, swap them
                temp = tempArray[cursor]
                tempArray[cursor] = tempArray[element]
                tempArray[element] = temp
    return tempArray

# input should be an alreay sorted trainingDataArray, pushes first three elements from trainingDataArray into...
# the a tempArray
# returns array of nearest neighbors
def findNearest( dataArray ) :
    tempArray = []
    tempArray.append( dataArray[0] )
    tempArray.append( dataArray[1] )
    tempArray.append( dataArray[2] )

    return tempArray

    
# Step 4: Gather the category Y of the nearest neighbors.
# Step 5: Use simple majority of the category of nearest neighbors as the prediction value of the query distance.

# takes in three closest data points and determines test query's class bases on them.
# returns string of guess
def determineCatagory( dataArray ):
    setosaCount = 0
    versicolorCount = 0
    virginicaCount = 0



    # print( 'Testing dataArray: ', dataArray)   
    for x in range( 0, len(dataArray) ):
        
        if dataArray[x][4] == 'Iris-setosa':
            setosaCount = setosaCount + 1
            
        if dataArray[x][4] == 'Iris-versicolor':
            versicolorCount = versicolorCount + 1
            
        if dataArray[x][4] == 'Iris-virginica':
            virginicaCount = virginicaCount + 1

    # print counts to console            
    # print( 'Counts: ','\n  setosaCount:', setosaCount, '\n  versicolorCount:', versicolorCount, '\n  virginicaCount:', virginicaCount )

    if ( setosaCount > versicolorCount and setosaCount > virginicaCount ): # if setosaCount is largest
        # print( 'Guess: Iris-setosa!')
        return 'Iris-setosa'
        
    if ( versicolorCount > setosaCount and versicolorCount > virginicaCount ): # if versicolorCount is largest
        # print( 'Guess: Iris-versicolor!')
        return 'Iris-versicolor'

    if ( virginicaCount > setosaCount and virginicaCount > versicolorCount ): # if virginicaCount is largest
        # print( 'Guess: Iris-virginica!')
        return 'Iris-virginica'
    
    if ( virginicaCount == setosaCount and virginicaCount == versicolorCount ): # if all are equal
        # print( 'Cannot be determined')
        return 'NA'
    
# compares array of guesses and answers, and determines accuracy
def performanceMetric( trainingData, testData, guessDataArray ):

    arrOfErrors = [];
    index = 0
    wrongCount = 0
    for element in guessDataArray:
        index = index + 1
        if element[0] != element[1]: # if guess does not equal correct answer, increase wrongCount by 1
            arrOfErrors.append( [ testData[index] , element[0] ] )
            wrongCount = wrongCount + 1
            
    print ( '\n------------------------------------------------------------------------------------------' )
    print('Data points of wrong guesses: ')
    for line in arrOfErrors:
        print( '\nInput Data: ', line[0], 'Guess: ', line[1] );
    # determine accuarcy
    accuracy = 1 - ( wrongCount / len( guessDataArray ) )
    print ( '\n------------------------------------------------------------------------------------------' )
    print ( 'Size of data:\n\tTraining: ', len(trainingData), '\n\tTestingData:', len(testingDataArray), '\n\tCorrect Guesses: ', len(testingDataArray) - wrongCount, '\n\tWrong Guesses: ', wrongCount )
    print ( '\nThe model\'s accuracy is (',len(testingDataArray) - wrongCount, '/', len(testingDataArray), '): ', accuracy * 100 )
    print ( '\n------------------------------------------------------------------------------------------' )

    
def runProgram( trainingData, distanceArray,  testData ):

    # vars
    performanceCheckArray = [] # will store values of guesses and correct answers for performance metric
    tempArray = []
    count=0
    
    for line in testData:
        
        #reset values
        tempTrainingData = trainingData
        tempDistanceData = distanceArray
        tempTestData = testData
        tempArray = []
        
        # adding values to tempArray, one line at a time is passed into the following functions
        tempArray.append( line[0] )
        tempArray.append( line[1] )
        tempArray.append( line[2] )
        tempArray.append( line[3] )
        # print( '\nInput Data: ', tempArray )

        calMinDistance( tempTrainingData , tempDistanceData, tempArray )
        tempDistanceData = sortDistanceArray( tempTrainingData )
        neighborArray = findNearest( tempDistanceData )
        guess = determineCatagory ( neighborArray ) 

        # push guess and correct answer into performanceCheckArray in format, [ 'guess', 'correctAnwser']
        temp = [guess, line[4]] # temp array to append into performanceCheckArray
        performanceCheckArray.append( temp )

        # print( 'Guess: ', guess )
        # print( 'Correct answer: ', line[4] )
        # print( '\n==============================')
    performanceMetric(tempTrainingData, testData, performanceCheckArray )
def ui(trainingData, distanceArray):
    menu = 'Menu:\n\tRun data in Iris.data [1]\n\tRun single data point[2]\n\tChoice: '
    choice = input( menu )
    if choice == str(1):
        runProgram( trainingDataArray, distanceArray, testingDataArray )
    if choice == str(2):
        x = input( 'Sepal Length in cm: ' )
        y = input( 'Sepal Width in cm: ' )
        z = input( 'Petal Length in cm: ' )
        w = input( 'Petal Width in cm: ' )
        tempArray = [ x, y, z, w ]

        calMinDistance( trainingData , distanceArray, tempArray )
        tempDistanceData = sortDistanceArray( trainingData )
        neighborArray = findNearest( tempDistanceData )
        guess = determineCatagory ( neighborArray )
        print ( '\n------------------------------------------------------------------------------------------' )
        print('\nInput Data:', tempArray, '\nClosest neighbors:\n\t',neighborArray[0], '\n\t', neighborArray[1], '\n\t', neighborArray[2], '\n\nGuess: ', guess )
        print ( '\n------------------------------------------------------------------------------------------' )
while( 1==1):
    ui(trainingDataArray, distanceArray)
# runProgram( trainingDataArray, distanceArray, testingDataArray )
