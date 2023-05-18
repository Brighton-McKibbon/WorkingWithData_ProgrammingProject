#ENDG 233, Block 6
#Brighton McKibbon
#Code gives the user two options that both calculate and find different information about a country's population and threatened species.
#Each option calculates a statistic about population, and about threatened species.
#They both also give the user the option to see a graph showing the population of a country as well as a bar graph showing the threatened species in the same country. 
#Modules imported: Numpy, Matplotlib, and Math

import numpy as np
import matplotlib.pyplot as plt
import math

class Country_Info:
    """Creates a Country_Info object
    Attributes:
    Takes in a 2D array containing country information, a list of the titles correlating to columns of the array, and a country index.
    This information is used to create the following attributes.
    country_name: Name of the found/chosen country.
    region: UN region relating to the found/chosen country.
    sub_region: UN region relating to the found/chosen country.
    sq_km: Area of the found/chosen country in square kilometers.
    """
    def __init__(self, country_data, country_labels, country_index):
        self.country_name = country_data[country_index][country_labels.index('Country')]        #setting the country name to the row of country_data correlating to the country_index and the column whose index correlates to the index on the country_labels list with the value 'Country'. 
        self.region = country_data[country_index][country_labels.index('UN Region')]            #setting the region to the row of country_data correlating to the country_index and the column whose index correlates to the index on the country_labels list with the value 'UN Region'. (Repeated with the next two lines just using 'UN Sub-Region' and 'Sq-Km')
        self.sub_region = country_data[country_index][country_labels.index('UN Sub-Region')]
        self.sq_km = country_data[country_index][country_labels.index('Sq Km')]
    
    def print_info(self):
        """Instance method that prints a contry's name, region, subregion, and area.
        No parameters
        No returns
        """
        #printing the information related to the found/chosen country.
        print()
        print('Country\'s Info:')
        print('Country:\t\t\t', self.country_name)
        print('UN Sub-Region:\t\t\t', self.sub_region)
        print('UN Region:\t\t\t', self.region)
        if self.sq_km == '':                    #if there is not a value for the square kilometers of a country replace it with Unknown. 
            self.sq_km = 'Unknown'
        print('Area in Kilometers Squared:\t', self.sq_km)
        print()

def int_array_creation(imported_array):
    """removes the first row and first column of a full array of imported data and changes the values in the array from strings to integers.
    Arguments:
    imported_array = a 2D array imported from a cvs file
    Returns:
    returns a new array containing integer values of the data from the imported array excluding the first row and column.
    """
    new_array = imported_array[1:, 1:]      #creating a new array without the first row (containing the cvs file header) and first column (containing the list of countries)
    new_array = new_array.astype(int)       #changing all elements of the new array to integers
    return new_array

def print_menu():
    """prints a menu of options to the user.
    No arguments
    No returns 
    """
    print()
    print('Command Menu: Choose of the the following calculations.')
    print('1: Find the max, min, and average human population in a country of your choosing through a year range you select. As well as, the average threatened species in the chosen country.')
    print('2: Find the average population in a given year as well as the country with the highest or lowest population in that year. You will also be given the total number of threatened species in the country.')
    print('q: To quit the program.\n')

def species_plot(species_data, species, country_index, country):
    """creates a bar plot of the different types of threatened species according to the country found/chosen.
    Arguments:
    species_data = 2D array containing data about the number of threatened species in each country (integers).
    species = list containing header of the imported threatened species data (strings).
    country_index = an index value that relates to the found/chosen country.
    country = the name of the found/chosen country.
    Returns:
    returns True. 
    """
    plt.bar(species, species_data[country_index, :], color = ['red', 'blue', 'orange', 'magenta', 'green', 'yellow', 'cyan'])   #creating a bar graph the types of species on the x-axis and the number of threatenes species in the country on the y-axis. List of colours is provided so that each bar has a different color, extra colours are included incase other species types are added to imported data. 
    plt.ylabel('Number of Threatened Species')      #setting the y axis label
    plt.xlabel('Groupings of Threatened Species')   #setting x axis label
    plt.title(f'Threatened Species in {country}')   #titling the graph with 'Threatened Species in' the found/chosen country. 
    return True

def check_country_input(countries):
    """asks for the user to enter a country name and checks that the input is valid, if it is not valid it asks for another input.
    gives the option to return to the while loop in the main function.
    Arguments:
    countries = a 1 dimensional array countaining country names as strings.
    Returns:
    if the input is 'Quit' or 'quit' returns False
    otherwise returns a string of the inputted country name
    """
    print()
    print('Choose a country from the following list:\n', countries)     #printing the created array of the countries in the data.
    print('Proper spelling is important for this program to run properly. If the input you enter does not match a country in the list you will be asked to re-enter the country\'s name.')
    print('If you have selected the wrong option enter Quit or quit to return to the Command Menu.\n')
    
    country_choice = input('Enter the country name here: ')
    while country_choice != 0:                      #creating a while loop to confirm the user enters a valid input that runs as long as the user input doesn't = 0. The input can never = 0 so the loop will run until it reaches a break statement.
        if country_choice == 'Quit' or country_choice == 'quit':    #leaves the function, returning False, if the user inputs 'Quit' or 'quit'. 
            return False
        elif country_choice not in countries:         #if the input is not in the countries array the user is told their input is not valid and asked for a new one.
            print('There is no data for a country with that name. Please try again.')
            country_choice = input('Enter the country name here: ')
        else: 
            break                                   #while loop breaks once a valid country is entered.
    return country_choice

def human_pop_calc(countries, pop_data, species_data, country_data, years, species, country_labels, sorted_years):
    """calculates and prints the mean, min, and max population given an input country and a range of years.
    prints the information about the chosen country
    plots two figures; one containing the population of the years for the chosen country with vertical lines identifying the start and end of the selected range, the other showing the number of threatened species for each of the different type.
    Arguments:
    countries = a 1 dimensional array countaining country names as strings.
    pop_data, species_data, country_data = 2D arrays containing population numbers (int), number of theatened species (int), and information about each country in the data (str), respectively.
    years, species, country_labels = lists containing the years, types of species, and labels for the country information contained in the arrays that are passed through the funtion (str elements), respectively. Indices correlate to those in the arrays.
    sorted_years =  a list containing the elements in years ordered from lowest to highest value.
    No returns
    """
    print('You have chosen option 1: Find the max, min, and average human population in a country of your choosing through a year range you select. As well as, the average threatened species in the chosen country.')
    country_choice = check_country_input(countries)             #calling the function to get a valid country from the user.
    if country_choice == False:                                 #if the country_choice returns False, the codes leaves this function returning False to the main function.
        return False
    country_index = list(countries).index(country_choice)       #finding the index for the user chosen country.
    print()
    print(f'Enter a range of years from {sorted_years[0]} - {sorted_years[-1]} you would like to find the average population for. The first you enter should be less in value than the second.') #asking the user to enter a range of years within the range covered in the imported data. 
    year1 = input('Enter the first year here: ')
    year2 = input('Enter the second year here: ') 

    while year1 != 0:           #creating a while loop to confirm the user inputs a valid input that runs as long as the user input doesn't = 0. The input can never = 0 so the loop will run until it reaches a break statement.
        if ((year1 in years) and (year2 in years)) and (int(year1) <= int(year2)):  #if year1 is smaller than year2 and they are both in the list of years, set index1 and index2 = to the value of their respective indices in years.
            index1 = years.index(year1)
            index2 = years.index(year2)
            break               #loop breaks if two valid years are entered.
        else:                   #else the user is told 1+ of their years are not valid and are asked to reenter their years.
            print(f'One or more of the years you provided are not between {sorted_years[0]} and {sorted_years[-1]}. Or the first year entered is larger than the second. Please retry.')
            year1 = input('Enter the first year here: ')
            year2 = input('Enter the second year here: ')  

    print()
    print('*---------------------------------------------------------------------------------------------------*\n')
    print('Calculating Results (all numbers will be rounded down to the nearest whole).....')
    country_info = Country_Info(country_data, country_labels, country_index)    #creating an County_Info class object.
    country_info.print_info()                                                   #calling the print_info instance method on the created object.
    print('Population Data for {} from {} to {}:'.format(country_choice, year1, year2))         #printing a title for the calculated data below that includes the user entered country and years.
    print('Average Population:\t\t\t{}'.format(math.floor(np.mean(pop_data[country_index, range(index1, (index2 + 1))]))))      #calculating and printing the average population within the provided year range
    print('Maximum Population:\t\t\t{}'.format(math.floor(np.max(pop_data[country_index, range(index1, (index2 + 1))]))))       #calculating and printing the maximum population within the provided year range
    print('Minimum Population:\t\t\t{}'.format(math.floor(np.min(pop_data[country_index, range(index1, (index2 + 1))]))))       #calculating and printing the minimum population within the provided year range
    print('Average Number of Threatened Species:\t{}\n'.format(math.floor(np.mean(species_data[country_index, :]))))            #calculating and printing the average threatened species in the chosen country
    print('*---------------------------------------------------------------------------------------------------*\n')

    #asking the user if they want to see a graph of information about the chosen country
    print(f'Would you like to see a graph of the population information for {country_choice}?')
    print(f'A graph of the population of {country_choice} will pop up on your screen as well as a second graph showing the threatened species in {country_choice}.')
    print('To continue with the program you must close both graphs.')
    graphing_selection = input('Enter yes or no: ')
    print()
    while graphing_selection != 0:          #creating a while loop to confirm the user inputs a valid input that runs as long as the user input doesn't = 0. The input can never = 0 so the loop will run until it reaches a break statement.
        if graphing_selection == 'yes':     #if the user enters 'yes' to wanting a graph of the information for the chosen country, two figures are created and shown.
            figure1 = species_plot(species_data, species, country_index, country_choice)        #calling the function to create a plot based on the threatened species data for the chosen country
            figure2 = 2
            plt.figure(2)                   #plotting figure2 so that years is on the x-axis and the country population is on the y-axis.
            plt.plot(years, pop_data[country_index], 'k-', label = 'Population of {}'.format(country_choice))   #set color of the line to black and include a label for the legend
            plt.title('Population of {} from {} - {}'.format(country_choice, sorted_years[0], sorted_years[-1]))      #creating a title for the figure that includes the name of the chosen country as well as the first and last year contained in the data set.
            plt.xlabel('Years')             #labelling the x-axis
            plt.ylabel('Population')        #labelling the y-axis
            plt.xticks(sorted_years)               #setting the xticks to only occur at the values in years
            plt.axvline(year1, label = 'Start year you selected', linewidth = 0.5, color = 'cyan')      #creating 2, labeled 0.5 point size, cyan, vertical lines on the graph that fall on the two years the user entered.
            plt.axvline(year2, label = 'End year you selected', linewidth = 0.5, color = 'cyan')
            plt.legend(shadow = True)       #creaing a legend that includes the labels for the population line and 2 vertical lines.
            plt.show()                      
            break       #loop breaks if the user enters 'yes'
        elif graphing_selection == 'no':
            break       #loop breaks if the user enters 'no'
        else:           #if the user enters an invalid input, they are told it is invalid and asked to enter another.
            print('The input you have entered does not match the above options. Please try again.')
            graphing_selection = input('Enter yes or no: ')

def pop_val_and_species(countries, pop_data, species_data, country_data, years, species, country_labels, sorted_years):
    """calculates and prints the mean population in a user chosen year, finds the country with the highest or lowest population in the chosen year as well as the country's population in that year, and the total threatened species in the country.
    prints the information about the found country
    plots two figures one containing the population of the years for the chosen country with a vertical line identifying the chosen year, the other showing the number of threatened species for each of the different type.
    Arguments:
    countries = a 1 dimensional array countaining country names as strings.
    pop_data, species_data, country_data = 2D arrays containing population numbers (int), number of theatened species (int), and information about each country in the data, respectively.
    years, species, country_labels = lists containing the years, types of species, and labels for the country information contained in the arrays that are passed through the funtion, respectively. Indices correlate to those in the arrays.
    sorted_years =  a list containing the elements in years ordered from lowest to highest value.
    No returns
    """
    print('You have selected option 2: Find the average population in a given year as well as the country with the highest or lowest population in that year. You will also be given the total number of threatened species in that country.\n')
    input_year = input(f'Please enter the year between {sorted_years[0]} and {sorted_years[-1]} you would like to look at the data for (or enter Quit or quit to return to the command menu): ')      #asking the user to input a year in the range of years or quit/Quit to return to the command menu
    while input_year != 0:              #creating a while loop to confirm the user inputs a valid input that runs as long as the user input doesn't = 0, the input can never = 0 so the loop will run until it reaches a break statement.
        if (input_year == 'quit') or (input_year == 'Quit'):        #if the input_year is 'quit' or 'Quit', the codes leaves this function returning False to the main function.
            return False
        elif input_year not in years:     #if the input is not in years the user is told their input is not valid and asked to input another
            print(f'The year you have entered does not fall between {sorted_years[0]} and {sorted_years[-1]}. Please try again.')
            input_year = input(f'Please enter the year between {sorted_years[0]} and {sorted_years[-1]} you would like to look at the data for (or enter Quit or quit to return to the command menu): ')
        elif input_year in years:         #loop breaks once the user inputs a valid year
            break
    print()
    min_or_max = input(f'Would you like to find the country with the highest or lowest population in {input_year}? \nEnter highest or lowest: ')
    while min_or_max != 0:              #creating a while loop to confirm the user inputs a valid input that runs as long as the user input doesn't = 0, the input can never = 0 so the loop will run until it reaches a break statement.
        if min_or_max == 'highest':     #if the user inputs 'highest' finds the highest value within the column of the chosen year. Loop breaks.
            pop_val = np.max(pop_data[:, years.index(input_year)])
            break
        elif min_or_max == 'lowest':    #if the user inputs 'lowest' finds the lowest value within the column of the chosen year. Loop breaks.
            pop_val = np.min(pop_data[:, years.index(input_year)])
            break
        else:                           #if the input is not 'highest' or 'lowest' the user is told their input is not valid and asked to input another
            print('The input you have entered does not match the above options. Please try again.')
            min_or_max = input(f'Enter highest or lowest: ')

    pop_index = np.where(pop_data == pop_val)           #finding the spots where pop_val exists in pop_data. Gives a 2D array with the rows from pop_data where the value occurs in the array at index 0 and the columns in pop_data where the value occurs in the array at index 1.
    #Finding the country with the max/min population value.
    for i in pop_index[1]:      #for each value in the second array in pop_index, if the value of the element is the index correlating to the input_year the country is the country whose index correlates to the value in the first array that is in the same index location as the value in the second array.
        if i == years.index(input_year):
            country = countries[pop_index[0][list(pop_index[1]).index(i)]]
    country_index = list(countries).index(country)      #finding the index that correlates with the found country

    total_threatened = 0 
    for i in species:       #adding all values in the row that correlates to the found country in species data to get the total.
        total_threatened += species_data[country_index][species.index(i)]
    print()     
    print('*---------------------------------------------------------------------------------------------------*\n')
    print('Calculating Results (all numbers will be rounded down to the nearest whole).....\n')
    print(f'The average population, for all of the countries in the database, in {input_year} is {math.floor(np.mean(pop_data[:, years.index(input_year)]))}') #calculating and printing the average population, of all of the countries, in the given year.
    print('The country with the {} population in {} is {}.'.format(min_or_max, input_year, country))        #printing the name of the country with the max/min population in the given year.
    country_info = Country_Info(country_data, country_labels, country_index)        #creating a Country_Info object for the found country
    country_info.print_info()           #calling the print_info instance method of Country_Info.
    print(f'Human Population in {country} in {input_year}:\t{pop_val}')             #printing the human population for the found country in the chosen year
    print(f'Total Threatened Species in {country}:\t{total_threatened}\n')          #printing the total threatened species in the found country.
    print('*---------------------------------------------------------------------------------------------------*\n')

    print('Would you like to see graphs of the information for this country?')
    print(f'Graphs for the population, and threatened species of {country} will pop up on your screen, to continue with the program you must close both graphs.')
    graphing_selection = input('Enter yes or no: ')
    while graphing_selection != 0:          #creating a while loop to confirm the user inputs a valid input that runs as long as the user input doesn't = 0. The input can never = 0 so the loop will run until it reaches a break statement.
        if graphing_selection == 'yes': #creates and shows two figures (almost the same as the figures created in the human_pop_calc function).
            figure1 = species_plot(species_data, species, country_index, country) 
            figure2 = 2
            plt.figure(2)
            plt.plot(years, pop_data[country_index], 'k-', label = 'Population of {}'.format(country))
            plt.title('Population of {} from {} - {}'.format(country, sorted_years[0], sorted_years[-1]))
            plt.xlabel('Years')
            plt.ylabel('Population')
            plt.xticks(sorted_years)
            plt.axvline(input_year, label = 'Selected Year', linewidth = 0.5, color = 'red')    #only one vertival line is created, color is red with a 0.5 point linewidth, label for legend set as 'Selected Year'. 
            plt.legend(shadow = True)           #creating a legend that includes the label for the population data line and the vertical line.
            plt.show()
            break       #loop breaks after the graphs have been closed
        elif graphing_selection == 'no':
            break       #loop breaks if the user enters 'no'
        else:           #else, input is invalid, user is told thier input is invalid and asked for a new one.
            print('The input you have entered does not match the above options. Please try again.')
            graphing_selection = input('Enter yes or no: ')

def main():
    #importing all of the data contained in three cvs files as strings into 2D numpy arrays.
    full_country_data = np.genfromtxt('Country_Data.csv', 'str', delimiter = ',')
    full_pop_data = np.genfromtxt('Population_Data.csv', 'str', delimiter = ',') 
    full_species_data = np.genfromtxt('Threatened_Species.csv', 'str', delimiter = ',')

    #creating lists and 1 dimensional arrays whose indices can be used to look up data in 2D arrays 
    countries = full_country_data[1:, 0]                    #creating a 1 dimensional array containing the names of the countries. Taking the first column of all but the first row of the full_country_data.
    
    country_labels = list(full_country_data[0, :])          #creating a list of the headers of the full_country_data by calling just the first row, all columns.
    pop_data_header = full_pop_data[0, 1:]                  #creating an array containing the first row and all columns other than the first from the full population data
    header_string = ' '.join(pop_data_header)               #joining the array to create a string with spaces
    header_string = header_string.replace('Pop', '-1')      #replacing all instances of 'Pop' with '-1' so that all parts of the string are able to be converted to integers in the following list comprehension. 
    years = [i for i in (header_string.split(' ')) if (int(i) >= 0)]   #creating a list that contains only the elements of a list version of header_string that are greater than or equal to 0. The header_string contains only the years correlating to the data and -1, years are always > 0 so all necessary years will be included in the list.
    sorted_years = sorted(years)                            #creating a sorted list of years that can be used for range labellin. Elements in years are sorted from lowest to highest value.
    species = list(full_species_data[0, 1:])                #creating a list containing the header of full_species_data, calling just the first row, all columns but the first.

    country_data = full_country_data[1:, :]                 #creating a 2D array from full_country_data removing the first row
    pop_data = int_array_creation(full_pop_data)            #calling the function to create an array containing only int values from the full_pop_data array
    species_data = int_array_creation(full_species_data)    #calling the function to create an array containing only int values from the full_species_data array

    print_menu()
    menu_choice = str(input('Enter the number correspoding to your menu selection here: '))
    print()
    while menu_choice != 'q':               #creating a while loop that runs as long at the user input does not equal 'q'. The loop breaks as soon as the user enters q, and proceeds to the rest of the main function.
        if menu_choice == '1':              #if the user enters a '1' the human_pop_calc funtion is called, then the print_menu function is called and the user is asked for another input.
            human_pop_calc(countries, pop_data, species_data, country_data, years, species, country_labels, sorted_years)
            print_menu()
            menu_choice = str(input('Enter the number correspoding to your menu selection here: '))
            print()
        elif menu_choice == '2':            #if the user enters a '2' the pop_val_and_species funtion is called, then the print_menu function is called and the user is asked for another input.
            pop_val_and_species(countries, pop_data, species_data, country_data, years, species, country_labels, sorted_years)
            print_menu()
            menu_choice = str(input('Enter the number correspoding to your menu selection here: '))
            print()
        else:                               #if the user does not input a '1', '2', or 'q', they are told their input was invalid the print_menu function is called and they are asked for another input.
            print('Your selection is invalid, please try again.')
            print_menu()
            menu_choice = str(input('Enter the number correspoding to your menu selection here: '))
            print()
    print('Thank you. Goodbye.\n') #prints once the while loop is broken

if __name__ == '__main__':
    main()