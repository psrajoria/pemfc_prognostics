
from pathlib import Path

PROJECT_ROOT = Path(r"C:\Users\prajoria\Desktop\Codes\ÈIS\pemfc_prognostics")

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

FC1_RAW_DIR = RAW_DIR / "FC1_Without_Ripples_Excel"
FC2_RAW_DIR = RAW_DIR / "FC2_With_Ripples_Excel"

PROCESSED_DIR = DATA_DIR / "processed"
FIX_DATA_DIR = PROCESSED_DIR / "fix_data"

OUTPUT_DIR = DATA_DIR / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"
MODEL_DIR = OUTPUT_DIR / "models"

SRC_DIR = PROJECT_ROOT / "src"
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

# Change this to "s" if ageing time in raw files is seconds.
# Keep "h" if it is already hours.
AGEING_TIME_UNIT = "h"

FC1_CHECKPOINTS = [0, 48, 185, 348, 515, 658, 823, 991]
FC2_CHECKPOINTS = [0, 35, 182, 343, 515, 666, 830, 1016]

RUL_THRESHOLDS = [0.035, 0.040, 0.045, 0.050, 0.055]

SELECTED_EIS_FREQS = [0.05, 0.789, 5.18, 505.0]

EIS_COLUMNS = [
    "Frequency_Hz",
    "ReZ_Ohm",
    "ImZ_Ohm",
]

POLARIZATION_COLUMNS = [
    "U1_V",
    "U2_V",
    "U3_V",
    "U4_V",
    "U5_V",
    "Ustack_V",
    "I_A",
    "J_A_cm2",
]

AGEING_COLUMNS = [
    "Time_raw",
    "U1_V",
    "U2_V",
    "U3_V",
    "U4_V",
    "U5_V",
    "Utot_V",
    "J_A_cm2",
    "I_A",
    "TinH2_C",
    "ToutH2_C",
    "TinAIR_C",
    "ToutAIR_C",
    "TinWAT_C",
    "ToutWAT_C",
    "PinAIR_mbara",
    "PoutAIR_mbara",
    "PoutH2_mbara",
    "PinH2_mbara",
    "DinH2_l_min",
    "DoutH2_l_min",
    "DinAIR_l_min",
    "DoutAIR_l_min",
    "DWAT_l_min",
    "HrAIRFC_percent",
]
