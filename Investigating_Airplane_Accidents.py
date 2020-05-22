# opening AviationData.txt file
aviation_list = []
with open('AviationData.txt', 'r') as file:
    aviation_data = file.readlines()
    for line in aviation_data:
        aviation_list.append(line.strip('\n').split(' | '))
# print(aviation_list[1])

# performing search for accident number 'LAX94LA336'
def code_search(code):
    lax_code = []
    for row in aviation_list:
        for item in row:
            if item == code:
                lax_code.append(row)
    return lax_code
lax_code = code_search('LAX94LA336')
# print(lax_code)

# performing linear search (O(n)) for searching 'LAX94LA336'
lax_code = []
for line in aviation_list:
    if 'LAX94LA336' in line:
        lax_code.append(line)
# print(lax_code)

# performing binary search (O(log(n))) for searching 'LAX94LA336'
import bisect
sorted_aviation_list = sorted(aviation_list, key=lambda row: row[2])
sorted_aviation_list[:2]
sorted_accident_numbers = [row[2] for row in sorted_aviation_list]
# print(sorted_accident_numbers[:10])
index_lax = bisect.bisect_left(sorted_accident_numbers, 'LAX94LA336')
# print(sorted_aviation_list[index_lax])

# storing data as a list of dictionaries
aviation_dict_list = []
keys = aviation_data[0].split(' | ')
for line in aviation_data[1:]:
    splitted_dict_lines = dict(zip(keys, line.split(' | ')))
    aviation_dict_list.append(splitted_dict_lines)
# print(aviation_dict_list[:2])

# search accident number 'LAX94LA336' in dictionary
lax_dict = []
for dict_ in aviation_dict_list:
    if 'LAX94LA336' in dict_.values():
        lax_dict.append(dict_)
# print(lax_dict)

# counting accidents that occured in each U.S. state
from collections import Counter
states = []
for dict_ in aviation_dict_list:
    # parsing the state by splitting the 'Location' field and extracting state
    if dict_['Country'] == 'United States' and ',' in dict_['Location']:
        state = dict_['Location'].split(',')[1].strip(' ')
        if len(state) == 2:
            states.append(state)  
states_accidents = Counter(states)
# print(states_accidents)

# states with the most accidents
# print(states_accidents.most_common(5))


def worst_month_accidents(data):
    months = []
    change_month = {"01":"January",
                    "02":"February",
                    "03":"March",
                    "04":"April",
                    "05":"May",
                    "06":"June",
                    "07":"July",
                    "08":"August",
                    "09":"September",
                    "10":"October",
                    "11":"November",
                    "12":"December"}
    
    for x in range(0, len(data)):
        month = data[x]['Event Date'][0:2]
        try:
            month = change_month[month]
        except KeyError:
            month = data[x]['Event Id'][4:6]
            month = change_month[month]
        if data[x]['Event Date'] != '':
            year = data[x]['Event Date'][-4:]
        else:
            year = data[x]['Event Id'][0:4]
        months.append(month + ' ' + year)
        
    worst_months = Counter(months)
    return worst_months, worst_months.most_common(3)

month_count_accidents, worst_3_months_acc = worst_month_accidents(aviation_dict_list)
# print(worst_3_months_acc)


def worst_month_injuries(data):
    injuries_by_month = {}
    change_month = {"01":"January",
                    "02":"February",
                    "03":"March",
                    "04":"April",
                    "05":"May",
                    "06":"June",
                    "07":"July",
                    "08":"August",
                    "09":"September",
                    "10":"October",
                    "11":"November",
                    "12":"December"}
    for x in range(0, len(data)):
        injuries = 0
        month = data[x]['Event Date'][0:2]
        try: 
            month = change_month[month]
        except KeyError:
            month = data[x]['Event Id'][4:6]
            month = change_month[month]
        if data[x]['Event Date'] != '':
            year = data[x]['Event Date'][-4:]
        else:
            year = data[x]['Event Id'][0:4]
        month = month + ' ' + year
        fatal = data[x]['Total Fatal Injuries']
        serious = data[x]['Total Serious Injuries']
        # Skip the blanks        
        if fatal:
            injuries += int(fatal)
        if serious:
            injuries += int(serious)
        injuries_by_month[month] = injuries
        injuries_by_month = Counter(injuries_by_month)        
        
    return injuries_by_month, injuries_by_month.most_common(3)
           
month_count_injuries, worst_3_months_inj  = worst_month_injuries(aviation_dict_list)
# print(worst_3_months_inj)