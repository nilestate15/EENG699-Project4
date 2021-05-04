import helper as hp
import georinex as gr
import numpy as np
import matplotlib.pyplot as plt

# load RINEX observation file (*.21o)
rinex_filename = 'ohdt0250.21o'
obs = gr.load(rinex_filename)

# conversion from RINEX observation date and time to TOW (seconds)
time_tow = [hp.datetime2tow(x.isoformat()) for x in obs.time.data]
# PRNs of satellites
sat_names = obs.sv.data

# plotting code

SEC_PER_DAY = 86400
MEAS_INTERVAL = 15  # sec
L1_LAMBDA = 299792458 / 1575.42e6  # meters


# GPS satellite PRNs vs. Time (week seconds)
plt.figure()
plt.title('PRNs vs Week Second')
for i in sat_names:
    plt.plot(time_tow, obs['L1'].sel(sv=i) / obs['L1'].sel(sv=i) * int(i[1:]), 'o', markersize = 5)
plt.xlabel('Time (week secs)')
plt.ylabel('PRN')
plt.grid(linestyle = '--', linewidth = 0.5)

# GPS satellite PRNs vs. Time (hour of day)
t_hr = np.mod(time_tow, SEC_PER_DAY) / 3600.0

plt.figure()
plt.title('PRNs vs Hour of Day')
for i in sat_names:
    plt.plot(t_hr, obs['L1'].sel(sv=i) / obs['L1'].sel(sv=i) * int(i[1:]), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('PRN')
plt.grid(linestyle = '--', linewidth = 0.5)

# L1 C/A code pseudoranges (C1) vs. Time in GPS Hour of Day
plt.figure()
plt.title('L1 C/A code pseudoranges (C1) vs. Time in GPS Hour of Day')
plt.plot(t_hr, obs['C1'], 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 C/A Pseudorange (m)')
plt.grid(linestyle = '--', linewidth = 0.5)

# L1 Carrier-Phase measurements (L1) vs. time in GPS hour of day
plt.figure()
plt.title('L1 Carrier-Phase measurements (L1) vs. time in GPS hour of day')
plt.plot(t_hr, obs['L1'], 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 C/A Pseudorange (cycles)')
plt.grid(linestyle = '--', linewidth = 0.5)

# Time Derivative of L1 C/A Code Pseudorange (C1) vs. Time in GPS Hour of Day
SV_str = 'G15' 
plt.figure()
plt.title('Time Derivative of L1 C/A Code Pseudorange (C1) vs. Time in GPS Hour of Day')
plt.plot(t_hr[:-1], np.diff(obs['C1'].sel(sv=SV_str))/MEAS_INTERVAL, 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 C/A Code Pseudorange Time Derivative (m/s)')
plt.grid(linestyle = '--', linewidth = 0.5)

# L1 C/A Code Pseudorange (C1) vs. Time in GPS Hour of Day
plt.figure()
plt.title('L1 C/A Code Pseudorange (C1) vs. Time in GPS Hour of Day')
plt.plot(t_hr, obs['C1'].sel(sv=SV_str), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 C/A Code Pseudorange (m)')
plt.grid(linestyle = '--', linewidth = 0.5)

# L1 Carrier-Phase measurement (L1) vs. time in GPS hour of day
plt.figure()
plt.title('L1 Carrier-Phase measurement (L1) vs. time in GPS hour of day')
plt.plot(t_hr, obs['L1'].sel(sv=SV_str), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 Carrier Phase (cycles)')
plt.grid(linestyle = '--', linewidth = 0.5)

# L2 Carrier-Phase Measurements (L2) vs. time in GPS hour of day
plt.figure()
plt.title('L2 Carrier-Phase Measurements (L2) vs. time in GPS hour of day')
plt.plot(t_hr, obs['L2'].sel(sv=SV_str), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L2 Carrier Phase (cycles)')
plt.grid(linestyle = '--', linewidth = 0.5)

# L2 P code pseudorange (P2) vs. time in GPS hour of day
plt.figure()
plt.title('L2 P code pseudorange (P2) vs. time in GPS hour of day')
plt.plot(t_hr, obs['P2'].sel(sv=SV_str), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L2 P Code Psuedorange (m)')
plt.grid(linestyle = '--', linewidth = 0.5)

# all code minus carrier (C1 in cycles - L1) vs time (hour of day)
plt.figure()
plt.title('L1 Code Minus Carrier (All Satellites) vs Time')
for i in sat_names:
    plt.plot(t_hr, obs['C1'].sel(sv=i)/L1_LAMBDA - obs['L1'].sel(sv=i), 'o', markersize = 5)
plt.xlabel('Time (day hrs)')
plt.ylabel('L1 Code Minus Carrier (cycles)')
plt.grid(linestyle = '--', linewidth = 0.5)


plt.show()
print('end')
