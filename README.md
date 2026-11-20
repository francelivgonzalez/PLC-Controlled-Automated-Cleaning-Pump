# PLC-Controlled-Automated-Cleaning-Pump
> Recreating industrial PLC ladder logic in readable Python- automating pump cleaning decisions to eliminate cross-batch contamination and manual guesswork.

A Python simulation of an automated cleaning pump control system originally developed in PLC ladder logic for a 24/7 vinyl manufacturing environment, built to make industrial automation logic readable, testable, and easy to showcase on GitHub.

## What This Project Does

In a 24/7 vinyl manufacturing line, pumps transfer liquids between different batches. If residue remains in the line after a run, even trace contamination can ruin the next batch's color or consistency—causing quality failures, recovery costs, and production downtime. Relying on manual operator checks during busy shifts introduces human error and inconsistent judgment.

This project translates the original PLC control sequence into Python so the system automatically evaluates sensor readings against preset thresholds rather than waiting on manual intervention:
1. **Safety Interlock & Start:** Verifies safe operating conditions before energizing the cleaning sequence.
2. **Continuous Sensor Evaluation:** Compares real-time line readings against preset purity/acceptability thresholds.
3. **Automated Routing & Retries:** Reroutes flow and repeats the cleaning cycle automatically if contamination is still detected, advancing to production readiness only when readings pass—or halting immediately on unsafe conditions or stop commands.

## What I'm Focusing On

- **Eliminating Cross-Batch Contamination:** Catching leftover residue automatically before the next liquid batch enters the line.
- **Reducing Operator Dependency:** Replacing subjective visual checks with repeatable, threshold-driven state transitions.
- **PLC-to-Python Logic Translation:** Mirroring industrial ladder logic rungs, interlocks, and state machines in clean, readable Python.
- **Fail-Safe Stop & Interlock Behavior:** Ensuring any unsafe condition or stop command halts the pump immediately.
- **Portfolio-Ready Documentation:** Presenting real-world manufacturing automation in an accessible software format without exposing proprietary plant code.

## How the Control Logic Is Set Up

- **State & Interlock Checks:** Guards startup and active operation with safety and stop-command checks at every scan cycle.
- **Threshold Comparator:** Evaluates simulated sensor readings against preset acceptable limits to classify clean vs. contaminated states.
- **Flow Routing & Cycle Loop:** Controls pump start/stop states, diverts flow when residue is detected, and loops cleaning cycles until pass criteria are met.
- **Simulation Runner:** Steps through normal, contaminated, and fault/stop scenarios so the control flow can be verified without physical PLC hardware.

## Planned Folder Layout

```text
PLC-Controlled-Automated-Cleaning-Pump/
├── README.md
├── src/
│   ├── controller.py     # Main PLC-style scan loop, interlocks, and state transitions
│   ├── sensors.py        # Simulated line sensor readings and threshold checks
│   └── actuators.py      # Pump and flow-rerouting valve state models
├── configs/
│   └── thresholds.yaml   # Preset acceptability limits and cycle retry parameters
├── tests/
│   └── test_cycles.py    # Clean pass, dirty retry loop, and emergency stop scenarios
└── main.py               # Entry point to run simulated cleaning cycles
