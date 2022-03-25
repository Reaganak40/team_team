#CptS 451 - Spring 2022
# https://www.psycopg.org/docs/usage.html#query-parameters

#  if psycopg2 is not installed, install it using pip installer :  pip install psycopg2  (or pip3 install psycopg2) 
import json
import psycopg2

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'

def insert2BusinessTable():
    #reading the JSON file
    with open('./yelp_business.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_business = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            try:
                cur.execute("INSERT INTO Business (y_business_id, y_business_name, y_rating, y_review_count, y_checkin_count, y_tip_count, y_open_status, y_city, y_state, y_zipcode, y_latitude, y_longitude)"
                       + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                         (data['business_id'],cleanStr4SQL(data["name"]), data["stars"], 0, 0, 0, [False,True][data["is_open"]], data["city"], data["state"], data["postal_code"], data["latitude"], data["longitude"] ) )              
            except Exception as e:
                print("Insert to businessTABLE failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_business +=1

        cur.close()
        conn.close()

    print(count_line_business)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2UserTable():
    
    with open('./yelp_user.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_users = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            try:
                cur.execute("INSERT INTO Users (y_user_id, y_tip_like_count, y_tip_count, y_avg_stars, y_num_fans, y_user_name, y_vote_count, y_date_joined, y_longitude, y_latitude)"
                       + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                         (data['user_id'], 0, data["tipcount"], data["average_stars"], data["fans"], cleanStr4SQL(data["name"]), 0, data["yelping_since"], 0, 0 ) )              
            except Exception as e:
                print("Insert to Users table failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_users +=1

        cur.close()
        conn.close()

    print(count_line_users)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2CheckinTable():
    
    with open('./yelp_checkin.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_check_in = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            dates = data['date'].split(',')
            for date in dates:
                try:
                    cur.execute("INSERT INTO Check_In (y_business_id, y_check_in_time)"
                        + " VALUES (%s, %s)", 
                            (data['business_id'], date) )              
                except Exception as e:
                    print("Insert to Check_In table failed!",e)
                conn.commit()
                # optionally you might write the INSERT statement to a file.
                # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
                #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
                # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_check_in +=1

        cur.close()
        conn.close()

    print(count_line_check_in)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2TipTable():
    
    with open('./yelp_tip.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_tip = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            try:
                cur.execute("INSERT INTO Tip (y_date, y_tip_text, y_user_id, y_business_id)"
                       + " VALUES (%s, %s, %s, %s)", 
                         (data['date'], data["text"], data["user_id"], data["business_id"]) )              
            except Exception as e:
                print("Insert to Tip table failed!", e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_tip +=1

        cur.close()
        conn.close()

    print(count_line_tip)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2CategoriesTable():
    
    with open('./yelp_business.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_categories = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            
            categories = data['categories'].split(',')
            for category in categories:
                try:
                    cur.execute("INSERT INTO Categories (y_category_name, y_business_id)"
                        + " VALUES (%s, %s)", 
                            (category, data['business_id']) )              
                except Exception as e:
                    print("Insert to Categories table failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_categories +=1

        cur.close()
        conn.close()

    print(count_line_categories)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2FriendsWithTable():
    
    with open('./yelp_user.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_friendswith = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            
            friends = data['friends']
            for friend in friends:
                try:
                    cur.execute("INSERT INTO Friends_With (y_user_id_friender, y_user_id_friended)"
                        + " VALUES (%s, %s)", 
                            (data['user_id'], friend) )              
                except Exception as e:
                    print("Insert to Friends_With table failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_friendswith +=1

        cur.close()
        conn.close()

    print(count_line_friendswith)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2BusinessHoursTable():
    #reading the JSON file
    with open('./yelp_business.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_business = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            hours = data['hours']
            for day_hours in list(hours.items()):
                open_time = day_hours[1].split('-')[0]
                close_time = day_hours[1].split('-')[1]

                open_hour = open_time.split(":")[0]
                open_minute = open_time.split(":")[1]
                if (len(open_hour) < 2):
                    open_hour = "0" + open_hour
                if (len(open_minute) < 2):
                    open_minute = "0" + open_minute
                open_time = open_hour + ":" + open_minute + ":" + "00"

                close_hour = close_time.split(":")[0]
                close_minute = close_time.split(":")[1]
                if (len(close_hour) < 2):
                    close_hour = "0" + close_hour
                if (len(close_minute) < 2):
                    close_minute = "0" + close_minute
                close_time = close_hour + ":" + close_minute + ":" + "00"

                try:
                    cur.execute("INSERT INTO Business_Hours (y_day, y_Opening_time, y_closing_time, y_business_id)"
                        + " VALUES (%s, %s, %s, %s)", 
                            (day_hours[0], open_time, close_time, data['business_id']) )              
                except Exception as e:
                    print("Insert to Business_Hours TABLE failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_business +=1

        cur.close()
        conn.close()

    print(count_line_business)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

def insert2AttributesTable():
    #reading the JSON file
    with open('./yelp_business.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business_out.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line_business = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            #TODO: update the database name, username, and password
            conn = psycopg2.connect("dbname='milestone2test' user='postgres' host='localhost' password='Password'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            attributes = data["attributes"]
            f_dict = flatten_dictionary(attributes)

            for attribute_data in f_dict:
                attribute_name = attribute_data.split(' : ')[0][1:-1]
                attribute_value = attribute_data.split(' : ')[1][1:-1]

                try:
                    cur.execute("INSERT INTO Attribute (y_attribute_name, y_attribute_value, y_business_id)"
                        + " VALUES (%s, %s, %s)", 
                            (attribute_name, attribute_value, data['business_id']) )              
                except Exception as e:
                    print("Insert to Attribute TABLE failed!",e)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            # sql_str = ("INSERT INTO businessTable (business_id, name, address, state, city, zipcode, latitude, longitude, stars, numCheckins, numTips, is_open)"
            #           + " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, {9}, {10}, {11})").format(data['business_id'],cleanStr4SQL(data["name"]), cleanStr4SQL(data["address"]), data["state"], data["city"], data["postal_code"], data["latitude"], data["longitude"], data["stars"], 0 , 0 , [False,True][data["is_open"]] )            
            # outfile.write(sql_str+'\n')

            line = f.readline()
            count_line_business +=1

        cur.close()
        conn.close()

    print(count_line_business)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()

# creates a list of dictionary pairs, no matter how many nested dictionaries exist
def flatten_dictionary(d):
    _list = []
    for key in d:
        if is_nested_dict(d[key]):
            _list += flatten_dictionary(d[key])
        else:
            _list.append("'{}' : '{}'".format(key, d[key]))
    return _list

# Returns true if the given parameter is a dictionary
def is_nested_dict(d):
    _elem = d
    for key in d:
        try:
            _elem = d[key]
        except:
            return False
    return True 

insert2BusinessTable()
insert2UserTable()
insert2CheckinTable()
insert2TipTable()
insert2CategoriesTable()
insert2FriendsWithTable()
insert2BusinessHoursTable()
insert2AttributesTable()