import numpy as np

from sacogrl.patient.schemas import PatientMonth


class SyntheticCohort:
    def __init__(self, patients: int, months: int, seed: int = 1337) -> None:
        self.patients = patients
        self.months = months
        self.rng = np.random.default_rng(seed)

    def build(self) -> list[PatientMonth]:
        rows: list[PatientMonth] = []
        for patient in range(self.patients):
            age = float(self.rng.normal(70.0, 10.0))
            sex = int(self.rng.integers(0, 2))
            race = int(self.rng.choice([0, 1, 2, 3, 4], p=[0.66, 0.13, 0.12, 0.06, 0.03]))
            region = int(self.rng.integers(0, 4))
            t_stage = int(self.rng.choice([0, 1, 2], p=[0.35, 0.45, 0.20]))
            grade = int(self.rng.choice([0, 1], p=[0.22, 0.78]))
            cis = int(self.rng.binomial(1, 0.25))
            tumor_count = float(self.rng.poisson(2.0) + 1)
            tumor_history = int(self.rng.binomial(1, 0.35))
            molecular = int(self.rng.choice([0, 1, 2, 3], p=[0.42, 0.24, 0.28, 0.06]))
            ae_load = 0.0
            for month in range(self.months):
                risk = 0.22 + 0.08 * t_stage + 0.05 * cis + 0.03 * tumor_history
                action = int(self.rng.integers(0, 5))
                ae = float(self.rng.binomial(1, min(0.10 + 0.05 * (action == 0), 0.45)))
                ae_load += ae
                rfs = float(self.rng.binomial(1, max(0.0, 0.72 - risk + 0.02 * (action in (1, 2)))))
                adherence = float(max(0.0, 1.0 - 0.08 * ae_load + 0.03 * (action in (1, 2))))
                rows.append(
                    PatientMonth(
                        str(patient),
                        month,
                        age,
                        sex,
                        race,
                        region,
                        t_stage,
                        grade,
                        cis,
                        tumor_count,
                        tumor_history,
                        2 + int(t_stage > 0),
                        4.0 + risk * 8.0,
                        3.0 + risk * 7.0,
                        ae_load,
                        molecular,
                        action,
                        rfs,
                        ae,
                        adherence,
                        1.0,
                    )
                )
        return rows
