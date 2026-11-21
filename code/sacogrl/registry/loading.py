from pathlib import Path

import pandas as pd

from sacogrl.patient.schemas import PatientMonth, rows_to_months
from sacogrl.registry.synthetic import SyntheticCohort


class RegistryLoader:
    def __init__(self, path: str | Path | None, patients: int = 128, months: int = 36) -> None:
        self.path = Path(path) if path else None
        self.patients = patients
        self.months = months

    def load(self) -> list[PatientMonth]:
        if self.path is not None and self.path.exists():
            frame = pd.read_csv(self.path)
            return rows_to_months(frame.to_dict(orient="records"))
        return SyntheticCohort(self.patients, self.months).build()
