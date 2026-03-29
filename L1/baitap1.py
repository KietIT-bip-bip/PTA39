# input
input_time = input("")



#ham cat hh/mm/ss
def split_time(input_time):
    try:
        time_list = input_time.split(":")
        hour = int(time_list[0])
        minute = int(time_list[1])
        second = int(time_list[2])
        return hour, minute, second #tuple
    except :
        print(" invalid time format")
        return None
# ham kiem tra hop le
def validate_time(hour=None, minute=None, second=None):
    if hour == None or minute == None or second == None:
        return "Khong hop le"

    # kiem tra gio (0 -> 23)
    if hour < 0 or hour > 23:
        return "Khong hop le"

    # kiem tra phut (0 -> 59)
    if minute < 0 or minute > 59:
        return "Khong hop le"

    # kiem tra giay (0 -> 59)
    if second < 0 or second > 59:
        return "Khong hop le"

    return "Hop le"  # nhung truong hop khac deu hop le


# output
print(validate_time(*split_time(input_time)))

#output
