#                          TIME CALCULATOR

""" Hello Everyone! Today we will be working on a Important application Program TIME CALCULATOR, Now, Lets Understand the Logic behind this Program, The main objective of this program is to calculate the time after adding a given duration to a specified starting time."""

""" It considers AM/PM, handles time carry-over, and optionally adjusts the day of the week based on the input. The resulting time is presented in a formatted manner with the option to indicate "next day" or "days later" if applicable."""

# Now, Lets define an function "add_time" with three parameters in it, "start", "duration" and "day_of_week" with a default value of "False".
def add_time(start,duration,day_of_week=False):

# Days of the Week Index and Array :
    days_of_the_week_index={"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}

    days_of_the_week_array= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
# Now, Let's parse through the duration to split "hours" and "minutes" with ":" sign
    duration_tuple = duration.partition(":")
    duration_hours=int(duration_tuple[0]) # Indexing [0] represents "Hours"
    duration_minutes=int(duration_tuple[2]) # Indexing [2] represents "Minutes"

# Let's parse through the "Start Time" 
    start_tuple = start.partition(":") #Splits the start time at ":" into a tuple
    start_minutes_tuple = start_tuple[2].partition(" ") #Splits the remaining part at " " (space)
    start_hours = int(start_tuple[0]) #Extracts hours from the start time
    start_minutes = int(start_minutes_tuple[0]) #Extracts minutes from the start time
    am_or_pm = start_minutes_tuple[2] #Determines whether it's AM or PM
    am_and_pm_flip = {"AM": "PM", "PM": "AM"} #It is a Flipper used when AM flips to PM or PM changes to AM

    """ Here, We Know that, A Day consists of total 24Hours. So, Let's give that with the function "amount_of_days". To find the amount of days divide duration hours with 24 ( to get hours ) """

    amount_of_days = int(duration_hours / 24)

  # Hence, start_minutes is completed, Now Let's find out the end_minutes, it should display end_hours and end_minutes after the Code is executed.

    end_minutes = start_minutes + duration_minutes
    if(end_minutes >= 60):
      start_hours += 1
      end_minutes = end_minutes % 60
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12) #Here, We get AM after 12 Hrs of a Day and PM after another 12Hours of a Day. So, The amount_of_am_pm_flips should change accordingly after 12Hours, so we divide it by 12.
  
    end_hours = (start_hours + duration_hours) % 12


  # LETS FORMAT THE TIMING : 
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours=12 if end_hours == 0 else end_hours
    if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1
    
    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm
  
  # DAY OF THE WEEK HANDLING :
    returnTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm
    if(day_of_week):
      day_of_week = day_of_week.lower()
      index=int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7 #  This, Is the main logic code that formats the Output.
      new_day = days_of_the_week_array[index]
      returnTime += ", " + new_day
  # Now, Lets Add "next day" or "days later".Here, Lets Check the amount_of_days to determine whether to add "next day" or "days later".
    if(amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif(amount_of_days > 1):
      return returnTime + " (" + str(amount_of_days) + " days later)"
      
  # Finally, Now Let's Return the formatted time with the appropriate day and "next day" or "days later". I am adding extra Examples to the "main.py" file using "add_time function" to make it more clear and understandable. 
    return returnTime

# Hence, The Time Calculator is Successfully executed and well Explained.