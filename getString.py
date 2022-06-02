def distCoordinates(lon1, lat1, lon2, lat2):    # calculates the airial distance between two coordinates
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r #    ##      #

def parser(string):
    query = string[0:3]   #divides the string to its elements
    length_dis_lat = string[3:5]
    if (length_dis_lat[0]) == 0:
        length_dis_lat = length_dis_lat[1]
    dis_lat = string[5:5+int(length_dis_lat)]
    length_date_long = string[5+int(length_dis_lat):5+int(length_dis_lat)+2]
    if (length_date_long[0] == 0):
        length_date_long = length_date_long[1]
    long = string[5+int(length_dis_lat)+2:5+int(length_dis_lat)+2+int(length_date_long)]
    string = query+"@"+length_dis_lat+"@"+dis_lat+"@"+length_date_long+"@"+long  #joins the elements into strings
    list1 = string.split("@")   #converts the string to list
    print(list1)
    if list[0] == "100":  #the query is validate disabled tag
        validate()
    elif list1[0] == "101": #the query is send open parks
        listPark = get_all_open_parkings()
        openPark = []
        for i in listPark:
            if (abs(distCoordinates(lat, long, i[0], i[1])) <= 0.5):  #if the coordinate is less than 0.5 km from the user's location
                openPark.append(i)




















if __name__ == '__main__':
    getString("10003123061234567898")