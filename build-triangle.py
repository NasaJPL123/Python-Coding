import numpy as np
import pandas as pd

# ── Step 1: Load claims data ──────────────────────────────────────────
claims = pd.read_csv("triangle-data.csv")

# ── Step 2: Build incremental triangle ───────────────────────────────
incremental = claims.pivot_table(
    index="accident_period",
    columns="lag_months",
    values="paid_amount",
    aggfunc="sum"
)

# ── Step 3: Build cumulative triangle ────────────────────────────────
cumulative = incremental.cumsum(axis=1)

print("=== INCREMENTAL TRIANGLE ===")
print(incremental.round(0))
print()
print("=== CUMULATIVE TRIANGLE ===")
print(cumulative.round(0))