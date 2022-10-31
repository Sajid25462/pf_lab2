def time_func(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(hours, "Hour", minutes, "Minute", seconds, "Second")

seconds = int(input("Write the time in seconds: "))
time_func(seconds)
    
