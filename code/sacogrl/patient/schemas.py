from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass(frozen=True)
class PatientMonth:
    patient_id: str
    month: int
    age: float
    sex: int
    race_group: int
    region: int
    t_stage: int
    grade: int
    cis: int
    tumor_count: float
    tumor_history: int
    eau_risk: int
    cueto: float
    eortc: float
    cumulative_g3_ae: float
    molecular_axis: int
    action: int
    rfs_event: float
    ae_event: float
    adherence: float
    weight: float


@dataclass(frozen=True)
class TrajectoryBatch:
    states: np.ndarray
    actions: np.ndarray
    rewards: np.ndarray
    next_states: np.ndarray
    dones: np.ndarray
    groups: np.ndarray
    weights: np.ndarray


FIELD_ORDER = (
    "age",
    "sex",
    "race_group",
    "region",
    "t_stage",
    "grade",
    "cis",
    "tumor_count",
    "tumor_history",
    "eau_risk",
    "cueto",
    "eortc",
    "cumulative_g3_ae",
    "molecular_axis",
)


def row_to_patient_month(row: Mapping[str, Any]) -> PatientMonth:
    return PatientMonth(
        patient_id=str(row.get("patient_id", "0")),
        month=int(row.get("month", 0)),
        age=float(row.get("age", 70.0)),
        sex=int(row.get("sex", 0)),
        race_group=int(row.get("race_group", 0)),
        region=int(row.get("region", 0)),
        t_stage=int(row.get("t_stage", 1)),
        grade=int(row.get("grade", 1)),
        cis=int(row.get("cis", 0)),
        tumor_count=float(row.get("tumor_count", 1.0)),
        tumor_history=int(row.get("tumor_history", 0)),
        eau_risk=int(row.get("eau_risk", 2)),
        cueto=float(row.get("cueto", 4.0)),
        eortc=float(row.get("eortc", 4.0)),
        cumulative_g3_ae=float(row.get("cumulative_g3_ae", 0.0)),
        molecular_axis=int(row.get("molecular_axis", 0)),
        action=int(row.get("action", 0)),
        rfs_event=float(row.get("rfs_event", 0.0)),
        ae_event=float(row.get("ae_event", 0.0)),
        adherence=float(row.get("adherence", 1.0)),
        weight=float(row.get("weight", 1.0)),
    )


def rows_to_months(rows: Iterable[Mapping[str, Any]]) -> list[PatientMonth]:
    return [row_to_patient_month(row) for row in rows]
