# -----------------------------
# Inputs
# -----------------------------
  estop_ok = True
  start_pb = False
  stop_pb = False
  cycle_done = False
  AI_Turbidity_raw = 0   # unsigned 16-bit style value

# -----------------------------
# Internal bits / latched states
# -----------------------------
  RUN_LATCH = False
  WASTE_MODE = False

# -----------------------------
# Settings
# -----------------------------
  TURBIDITY_THRESHOLD = 30000


def run_scan(estop_ok, start_pb, stop_pb, cycle_done, AI_Turbidity_raw):
    global RUN_LATCH
    global WASTE_MODE

    # system health
    SYSTEM_OK = estop_ok

    # start/stop latch logic
    if not SYSTEM_OK or stop_pb:
        RUN_LATCH = False
    elif SYSTEM_OK and start_pb:
        RUN_LATCH = True

    # turbidity check
    dirty = AI_Turbidity_raw < TURBIDITY_THRESHOLD
    clean = AI_Turbidity_raw >= TURBIDITY_THRESHOLD

    # waste mode logic
    if not SYSTEM_OK or not RUN_LATCH:
        WASTE_MODE = False
    elif dirty:
        WASTE_MODE = True
    elif clean:
        WASTE_MODE = False

    # outputs
    mixer_motor = RUN_LATCH
    solenoid_waste = WASTE_MODE
    solenoid_clean = RUN_LATCH and clean
    rerun_timer = RUN_LATCH and cycle_done and dirty

    return {
        "SYSTEM_OK": SYSTEM_OK,
        "RUN_LATCH": RUN_LATCH,
        "WASTE_MODE": WASTE_MODE,
        "dirty": dirty,
        "clean": clean,
        "mixer_motor": mixer_motor,
        "solenoid_waste": solenoid_waste,
        "solenoid_clean": solenoid_clean,
        "rerun_timer": rerun_timer
    }


# example test scans
test_scans = [
    {"estop_ok": True, "start_pb": True,  "stop_pb": False, "cycle_done": False, "AI_Turbidity_raw": 22000},
    {"estop_ok": True, "start_pb": False, "stop_pb": False, "cycle_done": True,  "AI_Turbidity_raw": 22000},
    {"estop_ok": True, "start_pb": False, "stop_pb": False, "cycle_done": True,  "AI_Turbidity_raw": 34000},
]

for i, scan in enumerate(test_scans, 1):
    result = run_scan(
        scan["estop_ok"],
        scan["start_pb"],
        scan["stop_pb"],
        scan["cycle_done"],
        scan["AI_Turbidity_raw"]
    )

    print(f"\nScan {i}")
    for key, value in result.items():
        print(f"{key}: {value}")
