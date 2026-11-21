from enum import IntEnum


class ScheduleAction(IntEnum):
    FULL_DOSE = 0
    ONE_THIRD_DOSE = 1
    PAUSE_THREE_MONTHS = 2
    PAUSE_SIX_MONTHS = 3
    SUBSTITUTE = 4


ACTION_NAMES = {
    ScheduleAction.FULL_DOSE: "continue_full_dose",
    ScheduleAction.ONE_THIRD_DOSE: "continue_one_third_dose",
    ScheduleAction.PAUSE_THREE_MONTHS: "pause_three_months",
    ScheduleAction.PAUSE_SIX_MONTHS: "pause_six_months",
    ScheduleAction.SUBSTITUTE: "substitute_intravesical_agent",
}

SOC_MONTHLY_PATTERN = (
    ScheduleAction.FULL_DOSE,
    ScheduleAction.FULL_DOSE,
    ScheduleAction.FULL_DOSE,
    ScheduleAction.ONE_THIRD_DOSE,
    ScheduleAction.FULL_DOSE,
    ScheduleAction.PAUSE_THREE_MONTHS,
)


def soc_action(month: int) -> ScheduleAction:
    if month < 0:
        raise ValueError("month must be non-negative")
    return SOC_MONTHLY_PATTERN[month % len(SOC_MONTHLY_PATTERN)]


def action_name(action: int) -> str:
    return ACTION_NAMES[ScheduleAction(int(action))]
