import winsound, time, os, datetime, re



# Steps to build Alarm clock Project: 
# Step 1: Create get_time()
def get_time():
    while True:
        # Get the time from the user
        user_time = input('What time do you want to wake up: ')
        
        # Check if user enteres in the correct way --> Hours:Minutes:Seconds with regex
        colons = re.findall(':', user_time)
        if colons != [':', ":"]:
            time.sleep(1)
            print('Invalid time! Time must be typed like this: (00:00:00)')
            time.sleep(1)
            print('Try again.')
            time.sleep(1)
        # Return 
        else:
            hours, minutes, seconds = map(int, user_time.split(':'))
            if 0<= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                return hours, minutes, seconds
            
            else:
                print('Invalid numbers!')
                time.sleep(1)

            
# Step 2: Create check_time(target_time)
def check_time(target_time):
    # Take hours, minutes, and seconds 
    hours, minutes, seconds = target_time
    
    print(f'Alarm set for {hours}:{minutes}:{seconds}')

    while True:
        SYSTEM_TIME = datetime.datetime.now()
        HOURS = SYSTEM_TIME.strftime('%H')
        MINUTES = SYSTEM_TIME.strftime('%M')
        SECONDS = SYSTEM_TIME.strftime('%S')
        
        current = SYSTEM_TIME.replace(microsecond=0)
        target_time = SYSTEM_TIME.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        # Check if target_time not in the past
        if target_time < current:
            target_time += datetime.timedelta(days=1)
            time.sleep(1)
            print('You cannot enter a time in the past! The alarm will ring tomorrow.')
            return False
            
        else:
            print(f'{HOURS}:{MINUTES}:{SECONDS}')
            # Check if target_time == sys time:
            if int(HOURS) == hours and int(MINUTES) == minutes and int(SECONDS) == seconds:
                return True
            time.sleep(1)
            os.system('cls')
            

# Step 3: Create ring_alarm()
def ring_alarm():
    while True:

        # Check if check_time == true, ring the alarm
        print('\nWake Up ⌚...')
        for _ in range(3):
            winsound.Beep(1500, 700)
            winsound.Beep(1000, 700)
            winsound.Beep(1200, 700)
        choice = input("\nType 'Snooze' to delay 5 minutes or 'Stop' to end alarm: ").capitalize()
        if choice == 'Stop':
            break
        elif choice == 'Snooze':
            print('😴 Snoozing for 5 minutes...')
            time.sleep(5)
            os.system('cls')
            print('\nAlarm ringing again!')
        else:
            print('❌ Invalid choice! Alarm continues...')
            time.sleep(1)

# Step 4: Create main()
def main():
    os.system('cls')
    print('\n=== Alarm Clock ===')
    user_time = get_time()
    is_true = check_time(user_time)


    if is_true:
        time.sleep(1)
        ring_alarm()
        print('\n✅ Alarm stopped! Have a great day')

if __name__ == '__main__':
    main()