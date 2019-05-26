# Fentahun Reta
# Analyzing the world population, the population of each country and their GDP by reading
# from the given data file.



def main():

    # open the files for the redaing by each line
    file_name = raw_input('please enter a file name: ')  
    infile = open(file_name, 'r')           
    # initialization for count number of country 
    total_num_county = 0
    total_world_popn = 0     
    total_GDP  = 0           
    total_GDP_per_capita = 0  
    highest_popn = 0
    lowest_popn = 1e15       # the lowest population that is initializa by big number in order to get
                              # the country with lowest GDP
    highest_GDP = 0           
    smallest_GDP = 1e15 # the lowest GDP per capita of the country that is initializa by big number
    highest_GDP_percapita = 0 
    lowest_GDP_percapita = 1e15  
    ## initialize all the names of country with highest and lowest with in the population and GDP
    highest_name_popn = ''  
    lowest_name_popn = ''              
    name_highest_GDP = ''              
    name_smallest_GDP = ''             
    highest_name_GDP_percapita = ''   
    lowest_name_GDP_percapita = ''     
#initialize list of rich country (with GDP per capita > 3 * average GDP per capita)
 # and very poor country with in the GDP per canpita < 2.5 % of all the average
    list_rich_countries = []   
    list_poor_countries = []      
    
    # The read in the first line 
    line = infile.readline()
    
    
    while line != '':
        gdp_data = line.split(',')  # splits a line into a string array
        row =line.split(',')     # split commoa separated lists in the line
        country_name = gdp_data[0]     # the first element of the line country name
        country_popn = int(gdp_data[1]) # the second element of the line country population to int
        country_GDP = float(gdp_data[2]) # the third element of the line country is the GDP 
        
        country_GDP_per_capita = country_GDP/country_popn 
# The total number of countries poppulation and GDP
        total_num_county += 1              
        total_world_popn += country_popn   
        total_GDP +=country_GDP            
        
 # total GDP per capita of the country
        total_GDP_per_capita += country_GDP_per_capita   
# The country that have the highest population
        if country_popn > highest_popn:         
            highest_popn = country_popn
            highest_name_popn = country_name
            
        # The country that havelowest population   
        if country_popn < lowest_popn:        
            lowest_popn = country_popn
            lowest_name_popn = country_name

        # Tell the country that have the highest GDP   
        if country_GDP > highest_GDP:         
            highest_GDP = country_GDP
            name_highest_GDP = country_name

        # Tell the country that have the smallest GDP    
        if country_GDP < smallest_GDP:
            smallest_GDP = country_GDP
            name_smallest_GDP = country_name
            
            
        # Tell the country that have the highest GDP per capita    
        if country_GDP_per_capita > highest_GDP_percapita:
            highest_GDP_percapita = country_GDP_per_capita
            highest_name_GDP_percapita = country_name

        # Tell the country that have the lowest GDP per capita 
        if country_GDP_per_capita < lowest_GDP_percapita:
           lowest_GDP_percapita = country_GDP_per_capita
           lowest_name_GDP_percapita = country_name
      
        line = infile.readline()
        # the average GDP percapital
    average_GDP_per_capita = (total_GDP_per_capita)/(total_num_county)  
# Then close the file 
    infile.close() 
    
    # After that read the file again to fill in the lists of rich and very poor country
     
    infile = open(file_name, 'r')
     
    line = infile.readline()
    while line !='':
        gdp_data = line.split(',') # Then splits a line into a string array
        
        country_name = gdp_data[0]
        country_popn = int(gdp_data[1]) 
        country_GDP = float(gdp_data[2])
        
        country_GDP_per_capita = country_GDP/country_popn  
        
        # the rich countries that have GDP > 3*
        if (average_GDP_per_capita)*3 < country_GDP_per_capita:
            list_rich_countries.append(country_name)

         # very poor countries that have average_GDP_per_capita GDP < 0.025*
        if country_GDP_per_capita < (average_GDP_per_capita)*0.025:
            list_poor_countries.append(country_name)

        line = infile.readline()
    # then close the file
    infile.close() 
    # print out the information for the user 
    print('\nThe total number of countries listed are: ',total_num_county)
    print('\nThe total number of population in the world is: ' + format(total_world_popn, ',.0f'))
    print('\nCountry with highest population is: ' + format(highest_popn, ',.0f'))
    print('\nCountry with lowest population is:  ' + str(lowest_popn))
    
    print('\nCountry with greatest GDP is: ' + name_highest_GDP + ', ' + format(highest_GDP, ',.2f'))
    print('\nCountry with smallest GDP is:' + name_smallest_GDP + ', ' + format(smallest_GDP, ',.2f'))
    print('\nThe name of the country with highest GDP per capita is: ' + highest_name_GDP_percapita + ', ' + format(highest_GDP_percapita, ',.2f'))
    print('\nThe name of the country with lowest GDP per capita is: ' + str(lowest_name_GDP_percapita) + ', ' + format(lowest_GDP_percapita, ',.2f'))
    print('\nAverage "GDP per capita" of all the countries: ' + format(average_GDP_per_capita, ',.2f') +'\n')
    print('List of rich countries, with a GDP per capita > 3 *(the average GDP_per_capita) = ',list_rich_countries)
    print('\nList of very poor countries, with a GDP per capita < 2.5% of the average GDP_per_capita = ', list_poor_countries)


main()  # running the program
