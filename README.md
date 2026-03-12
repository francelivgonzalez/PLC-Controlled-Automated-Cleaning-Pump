# PLC-Controlled-Automated-Cleaning-Pump
This project recreates in Python an automated cleaning pump system originally developed in PLC ladder logic for my job, allowing the logic to be shared and presented on GitHub.

PLC-Controlled Automated Cleaning Pump System


**Overview**
This project is a Python replication of an automated cleaning pump system that I originally developed in PLC ladder logic for my job. Since ladder logic is not easy to showcase on GitHub, I recreated the control logic in Python so I could document the project and show how the system works in a format that is easier to read and share.

This project came from a real issue in a vinyl manufacturing environment. When liquid is transferred using a pump, there is always a risk that leftover residue from a previous batch can contaminate the next one if the pump is not fully cleaned. In a process where color and consistency matter, even small contamination can lead to quality issues later on and result in additional recovery costs. Downtime is also a factor because the facility operates 24/7, and there are times when operator availability is limited. If someone has to step away from the rest of production to focus on this process, it can slow operations down and contribute to further downtime.

Another issue is that when a process depends too much on human judgment, mistakes can happen. A person may not always catch contamination at the right time, or the decision to stop or continue may vary from one operator to another. Because of that, I wanted to design a system that could reduce that manual dependence and make the process more consistent.


**Purpose**
The purpose of this project was to take out the middle man as much as possible and create a system that could make decisions based on preset parameters and sensor readings instead of relying only on someone to monitor it manually.

The idea was for the system to:
- detect whether the liquid met acceptable conditions
- determine whether contamination was still present
- know when to stop, start, or reroute flow
- repeat the cleaning cycle if needed
- continue running only when the readings showed that conditions were acceptable

This helps make the process more reliable, repeatable, and less dependent on manual intervention.


**Real-World Application**
This logic was inspired by a real production need. In vinyl manufacturing, pumps may be used between different batches, and if any leftover material remains in the line, it can affect the next batch’s color or quality. Since these issues may not always be obvious right away, contamination can create bigger problems later in production.

The goal of this system was to automate that decision-making process by using readings from the system and comparing them against preset limits. Instead of waiting on someone to decide whether the process looked clean enough, the system itself could evaluate the readings and respond accordingly.


**Why Python**
This project was originally built in ladder logic, but because ladder logic cannot really be presented well on GitHub, I recreated it in Python. The Python version is meant to reflect the same control idea and logic flow, while making the project easier to explain, document, and share.

It is not meant to replace the original PLC implementation in production. It is simply a GitHub-friendly representation of the original control logic.

What the System Does

The control logic follows a simple process:
- Start when safe conditions are met.
- Monitor the system readings.
- Compare those readings to preset thresholds.
- If contamination is detected, reroute or repeat the cycle.
- If acceptable conditions are detected, continue the process.
- Stop when unsafe conditions or stop commands occur.


**Final Note**
This project represents a real control concept that was originally applied in an industrial setting. I recreated it in Python to document the logic and show how industrial automation ideas can be translated into software for presentation and portfolio purposes.
