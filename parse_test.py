log_line = "Nov 12 09:44:01 web01 sshd[4850]: Accepted password for chroot-svc from 10.0.4.12 port 44200 ssh2"
# log_line = "Nov 12 09:41:23 web01 sshd[4821]: Failed password for invalid user admin from 203.0.113.45 port 51234 ssh2"
# log_line = "Nov 12 09:41:27 web01 sshd[4823]: Failed password for root from 203.0.113.45 port 51240 ssh2"
# log_line = "Nov 12 09:42:02 web01 sshd[4830]: Accepted password for root from 203.0.113.45 port 51255 ssh2"
# log_line = "Nov 12 09:42:11 web01 sshd[4831]: Accepted password for deploy from 10.0.4.12 port 44120 ssh2"
# log_line = "Nov 12 09:41:27 web01 sshd[4823]: Failed password for aminur from 203.0.113.45 port 51240 ssh2"
# log_line = "Nov 12 09:42:02 web01 sshd[4830]: Accepted password for aminur from 203.0.113.45 port 51255 ssh2"
# log_line = "Nov 12 09:43:10 web01 sshd[4840]: Connection closed by 203.0.113.45 port 51260 [preauth]"
info = log_line.split()

timestamp = f"{info[0]} {info[1]} {info[2]}"
hostname = info[3]

process_name = info[4].split("[")[0]
process_id = info[4].split("[")[1]
clean_process_id = int(process_id.strip("]:"))

user = info[-6]
source_ip = info[-4]
port = int(info[-2])
is_failed_login = "Failed password" in log_line

print(f"Parsed {len(info)} fields")
print(f"timestamp   :{timestamp}")
print(f"Hostname    :{hostname}")
print(f"process     :{process_name} (pid {clean_process_id})")
print(f"User        :{user}")
print(f"Source IP   :{source_ip}")
print(f"Port        :{port}")
print (f"Failed     :{is_failed_login}")


is_root = user == "root"
is_invalid_user = "invalid user" in log_line
is_successful_login = "Accepted password" in log_line

print("======Event Details======")
if is_successful_login and is_root:
    event_type = "SUCCESSFUL_LOGIN"
    severity = "CRITICAL"
  
elif is_failed_login and is_root:
    event_type = "FAILED_LOGIN"
    severity = "HIGH"
    
elif is_failed_login and is_invalid_user:
    event_type = "FAILED_LOGIN"
    severity = "MEDIUM"
  
elif is_failed_login:
    event_type = "FAILED_LOGIN"
    severity = "LOW"
   
elif is_successful_login:
    event_type = "SUCCESSFUL_LOGIN"
    severity = "INFO"
  
else:
    event_type = "UNKNOWN"
    severity = "UNKNOWN"
  

print(f"Event       :{event_type}")
print(f"Severity    :{severity}")
print(f"Source      :{source_ip}", end="")

is_internal = source_ip.startswith(("10.", "192.168."))
if is_internal:
    print("(internal)")
else:
    print("(external)")

print("=========================")


