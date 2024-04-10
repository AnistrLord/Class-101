import time 

def countdown_timer(seconds):
    while seconds > 0 :
        mins = int(seconds/60)
        secs = int(seconds%60)
        time.sleep(1)
        timer = f"{mins}:{secs}"
        print(timer)
        seconds -= 1
    
    print("time UP !!")

seconds= input("Enter the time in No of Seconds :")
countdown_timer(int(seconds))