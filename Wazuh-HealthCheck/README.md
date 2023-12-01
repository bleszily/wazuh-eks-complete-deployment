# Wazuh-HealthCheck
<<<<<<< HEAD
----------------HealthCheck Configuration for Wazuh Master---------
=======
----------HealthCheck Configuration for Wazuh Master--------------------
>>>>>>> fd49527c727f0a1f32ded1bb09a68e4e59b47d68
- First the below command to verify the processes
	ps -aux | grep 'var/ossec/bin/wazuh-*'
	
- Second line of the bash script set a host variable and use that to tell which manager in the cluster is having health issues (which interface)
	ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}'
	
- The Statement for each Process
	- use pgrep (pgrep wazuh-authd) to validate the process ID of the wazuh-authd process. 
	- if a value is returned for the process ID, create a json file with "key=host" and "value=$host (the ip of the host)" and set the health state of the process name to "healthy:yes" 
	- use echo to write the json output into a health.json file in /tmp
	- if no process ID is returned, the else block of the code is executed to;
		- attempt a restart of the process by;
			- set the json to the affected host, set the health status field to "attempting_restart" and write the line into the /tmp/health.json file.
		- run the command "service wazuh-manager restart" to restart the service
		- Sleep for 5mins for the service to restart before checking its state again using the "pgrep wazuh-authd" command
		- if process ID is found, write the new state into the /tmp/health.json file
		- if no process ID, write the new healthy state to the file.
		
- Move all scripts to the server (/opt/health-check) and;
	- make the bash script executable
	- Execute the script
	- check the /tmp directory for the health.json file
		- Identify affected host in the cluster
		- Identify the processes
		- Identify their health status
		
- Simulate a failure
	- Identify a process and kill it
		- ps -aux | grep 'var/ossec/bin/wazuh-*'
		- kill -9 PID
	- Run the script again and watch the self healing capability (Identify failed state)
	
- Send the output of the command to Kibana
	- Modify the /var/ossec/etc/ossec.conf file with the automation template
		- nano /var/ossec/etc/ossec.conf
		- Copy the healthcheck_ossec.conf file and add it to the last line of the ossec.conf file in the wazuh manager
		- the woodle script will run every 30 seconds (we can set it to seconds, days, weeks) to collect the recent health status and send it to Kibana
		- THe script sends the output to the /tmp/health.json file
		- It runs on start_up also (each restart
		- look at the last lines of the log to see if it picks the /tmp/health.json file
			- tail -f /var/ossec/logs/ossec.log
			- view the output of the /tmp/health.json file for new entry
			
- Create a rule to collect the output of the scripts
	- COllect an output in the /tmp/health.json file and check using the rule-test tool in the dashboard (no rule at the moment)
	- Copy the first 4 blocks of codes in healthcheck_rules.xml file
	- In the rule, we set the type, and search for any match with healthy within the output of /tmp/health.json file.
	- it will fire becuase the healthy field exist in every log that goes into the /tmp/health.json
	- if healthy field is present with attempting restart, we know if it being restarted.
	- If no, it is in a failed state.
	
- Checking
	- on the dashboard, go to modules, then, security events, filter for events related to restarting the manager
