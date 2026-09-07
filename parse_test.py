log_lines = [
    "Nov 12 09:41:23 web01 sshd[4821]: Failed password for invalid user admin from 203.0.113.45 port 51234 ssh2",
    "Nov 12 09:41:27 web01 sshd[4823]: Failed password for root from 203.0.113.45 port 51240 ssh2",
    "",
    "Nov 12 09:42:02 web01 sshd[4830]: Accepted password for root from 203.0.113.45 port 51255 ssh2",
    "Nov 12 09:42:11 web01 sshd[4831]: Accepted password for deploy from 10.0.4.12 port 44120 ssh2",
    "Nov 12 09:41:27 web01 sshd[4823]: Failed password for aminur from 203.0.113.45 port 51240 ssh2",
    "   ",
    "Nov 12 09:44:01 web01 sshd[4850]: Accepted password for chroot-svc from 10.0.4.12 port 44200 ssh2",
    "Nov 12 09:43:10 web01 sshd[4840]: Connection closed by 203.0.113.45 port 51260 [preauth]",
]

critical_count = 0
high_count = 0
medium_count = 0
low_count = 0
info_count = 0
unknown_count = 0
line_count = 0
internal_count = 0
external_count =  0
alerts = []

print("======Event Details======")
for log_number, log_line in enumerate(log_lines, start=1):
    if not log_line.strip():
        continue
    info = log_line.split()
    line_count +=1

    timestamp = f"{info[0]} {info[1]} {info[2]}"
    hostname = info[3]

    process_name = info[4].split("[")[0]
    process_id = info[4].split("[")[1]
    clean_process_id = int(process_id.strip("]:"))

    user = info[-6]
    source_ip = info[-4]
    port = int(info[-2])
    is_failed_login = "Failed password" in log_line

    is_root = user == "root"
    is_invalid_user = "invalid user" in log_line
    is_successful_login = "Accepted password" in log_line

    
    if is_successful_login and is_root:
        event_type = "SUCCESSFUL_LOGIN"
        severity = "CRITICAL"
        critical_count +=1
        alert =f"{severity}: {user} logged in successfully from {source_ip}"
        alerts.append(alert)
  
    elif is_failed_login and is_root:
        event_type = "FAILED_LOGIN"
        severity = "HIGH"
        high_count +=1
        alert =f"{severity}: failed {user} login from {source_ip}"
        alerts.append(alert)
    
    elif is_failed_login and is_invalid_user:
        event_type = "FAILED_LOGIN"
        severity = "MEDIUM"
        medium_count +=1
  
    elif is_failed_login:
        event_type = "FAILED_LOGIN"
        severity = "LOW"
        low_count +=1

   
    elif is_successful_login:
        event_type = "SUCCESSFUL_LOGIN"
        severity = "INFO"
        info_count +=1
  
    else:
        event_type = "UNKNOWN"
        severity = "UNKNOWN"
        unknown_count +=1
  
    print(f"[{log_number:>2}] {severity:<8} {event_type:<17} {user:<12} {source_ip}", end="")

    is_internal = source_ip.startswith(("10.", "192.168."))
    if is_internal:
        print("(internal)")
        internal_count +=1
    else:
        print("(external)")
        external_count +=1

print("=========================")

print("----- Summary -----")
print(f"Lines processed : {line_count}")
print(f"Critical        :{critical_count}")
print(f"High            :{high_count}")
print(f"Medium          :{medium_count}")
print(f"Low             :{low_count}")
print(f"Info            :{info_count}")
print(f"Unknown         :{unknown_count}")
print(f"Internal Source :{internal_count}")
print(f"External Source :{external_count}")
print("--------------------")
print("--- Alerts ---")
for alert in alerts:
    print(alert)
print("-------")
