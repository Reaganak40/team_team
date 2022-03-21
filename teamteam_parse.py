import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    # We assume that the Yelp data files are available in the current directory. If not, you should specify the path when you "open" the function. 
    with open('.//yelp_business.JSON','r') as f:  
        outfile =  open('.//business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - business info : '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; '{}' ; {} ; {} ; {} ; {}\n".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['business_id']),
                              cleanStr4SQL(data["name"]),
                              cleanStr4SQL(data["address"]),
                              cleanStr4SQL(data["state"]),
                              cleanStr4SQL(data["city"]),
                              cleanStr4SQL(data["postal_code"]),
                              str(data["latitude"]),
                              str(data["longitude"]),
                              str(data["stars"]),
                              str(data["is_open"])) )

            #process business categories
            categories = data["categories"].split(', ')
            outfile.write("      categories: {}\n".format(str(categories)))

            
            # code to process attributes
            # make sure to **recursively** parse all attributes at all nesting levels. You should not assume a particular nesting level. 
            attributes = data["attributes"]
            f_dict = flatten_dictionary(attributes)
            outfile.write("      attributes: [")
            if len(f_dict) != 0:
                last_pair = f_dict[-1]
            else: # If dict is empty add a close bracket
                outfile.write("]\n")
            for pair in f_dict:
                outfile.write("{{{}}}".format(pair))
                if pair == last_pair:
                    outfile.write("]\n")
                else:
                    outfile.write(", ")

                
            # code to process hours data
            hours = data["hours"]
            outfile.write("      hours: [")
            if len(hours) != 0: # get last key to format string at end of for loop
                last_pair = list(hours.keys())[-1]
            else: # If dict is empty add a close bracket
                outfile.write("]\n")
            for day in hours: # hours is a dictionary for day : hours
                pair = "'{}' : '{}'".format(day, hours[day])
                outfile.write("{{{}}}".format(pair))
                if day == last_pair:
                    outfile.write("]\n")
                else:
                    outfile.write(", ")




            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
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

def parseUserData():
    with open ('.//yelp_user.JSON','r') as infile:  
        outfile =  open('.//user.txt', 'w')
        line = infile.readline()
        line_count = 0
        while(line):
            data = json.loads(line)
            outfile.write("{} - user info : '{}' ; '{}' ; '{}' ; {} ; {} ; {} ; {} ; {} ; {}\n".format(
                              str(line_count), # the line count
                              cleanStr4SQL(data['user_id']),
                              cleanStr4SQL(data["name"]),
                              cleanStr4SQL(data["yelping_since"]),
                              str(data["average_stars"]),
                              str(data["cool"]),
                              str(data["fans"]),
                              str(data["funny"]),
                              str(data["useful"]),
                              str(data["tipcount"])) )
            categories = data["friends"]
            outfile.write("      friends: {}\n".format(str(categories)))

            outfile.write("\n")
            line = infile.readline()
            line_count +=1
    print(line_count)
    outfile.close()
    infile.close()


def parseCheckinData():
    with open('.//yelp_checkin.JSON','r') as f:  
        outfile =  open('.//checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - checkin info : '{}' :\n".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['business_id'])) )

            # TO-DO : write your own code to process date data
            dates = data['date'].split(',')
            count_date = 0
            outfile.write('\t')
            for date in dates:
                calendar_date = date.split(' ')[0]
                time = date.split(' ')[1]
                outfile.write("( '{}', '{}', '{}', '{}' )".format(cleanStr4SQL(calendar_date.split('-')[0]), cleanStr4SQL(calendar_date.split('-')[1]), cleanStr4SQL(calendar_date.split('-')[2]), cleanStr4SQL(time)))
                count_date += 1
                if count_date % 20 == 0:
                    outfile.write('\n\t')
                else:
                    outfile.write('\t')

            outfile.write('\n\n')

            line = f.readline()
            count_line +=1

    print(count_line)
    outfile.close()
    f.close()


def parseTipData():
    #read the JSON file
    with open('yelp_tip.JSON', 'r') as f:
        outfile = open('tip.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON object and extract data
        while line:
            data = json.loads(line)
            outfile.write("{} - tip info : '{}' :\n\t".format(
                              str(count_line), # the line count
                              cleanStr4SQL(data['business_id'])) )
            outfile.write(cleanStr4SQL(data['user_id'])+'\t') 
            outfile.write(cleanStr4SQL(data['date'])+'\t')
            outfile.write(str(data['likes'])+'\t')
            outfile.write(str(data['text']))

            outfile.write('\n\n')
            line = f.readline()
            count_line += 1
    outfile.close()
    f.close() 

if __name__ == "__main__":
    parseBusinessData()
    parseUserData()
    parseCheckinData()
    parseTipData()
