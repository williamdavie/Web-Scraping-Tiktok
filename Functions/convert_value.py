

#data recieved from webscrape comes back in format 12.1K or 1.3M, we want 12100 and 1300000

def convert_value(string):
    list_format = [*string]
    if 'K' in list_format:
        final_list = list_format[0:list_format.index('K')]
        final_value = float(''.join(final_list)) * 1000
    elif 'M' in list_format:
        final_list = list_format[0:list_format.index('M')]
        final_value = float(''.join(final_list)) * 1000000
    else:
        try:
            final_value = float(string)

        except:
            final_value = 0
    
    return final_value


#take a duration of format 00:00/00:10 and return 10

def convert_time(string):
    list_format = [*string]
    final_list = list_format[list_format.index('/')+4:len(list_format)]

    return float(''.join(final_list))



    
