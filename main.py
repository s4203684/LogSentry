# Prompt for context before analysis begins
separator = "=" * 36
print(separator)
print("      This is LogSentry v0.1")
print("   Created by Aminur Rashid Sohag")
print(separator)

analyst_name = input("Analyst name: ")
log_file = input("Log file to analyse: ")

print(f"Ready. Analyst {analyst_name} will analyse the {log_file} file")

failed_attempts = int(input("How many failed logins: "))
successful_logins = int(input("How many successful logins: "))
observation_window = int(input("Over how many minutes these logins were observed: "))

observation_window_hours = observation_window // 60
observation_window_min = observation_window % 60

total_events = failed_attempts + successful_logins
if (failed_attempts == 0 and successful_logins == 0):
    failure_rate = 0
else:
    failure_rate = (failed_attempts/total_events)*100
attempt_rate = (failed_attempts/observation_window)
risk_score = (failed_attempts*2)+(successful_logins*5)


print("--- Analysis summary ---")
print(f"Failed Attempts:     {failed_attempts}")
print(f"Successful Logins:  {successful_logins}")
print(f"Observation Window: {observation_window_hours} hours {observation_window_min} minutes")
print(f"Total events:       {total_events}")
print(f"Failure Rate:       {failure_rate:.1f}%")
print(f"Attempt Rate:       {attempt_rate:.2f} failed/min")
print(f"Risk Score:         {risk_score}")
print(f"{separator}")