import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport2:
    value: float
    flag: bool
    label: str


def clinical_transform_2_0(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_2_0_high" if flag else "band_2_0_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_1(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_2_1_high" if flag else "band_2_1_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_2(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_2_2_high" if flag else "band_2_2_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_3(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_2_3_high" if flag else "band_2_3_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_4(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_2_4_high" if flag else "band_2_4_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_5(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_2_5_high" if flag else "band_2_5_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_6(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_2_6_high" if flag else "band_2_6_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_7(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_2_7_high" if flag else "band_2_7_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_8(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_2_8_high" if flag else "band_2_8_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_9(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_2_9_high" if flag else "band_2_9_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_10(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_2_10_high" if flag else "band_2_10_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_11(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_2_11_high" if flag else "band_2_11_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_12(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_2_12_high" if flag else "band_2_12_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_13(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_2_13_high" if flag else "band_2_13_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_14(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_2_14_high" if flag else "band_2_14_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_15(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_2_15_high" if flag else "band_2_15_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_16(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_2_16_high" if flag else "band_2_16_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_17(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_2_17_high" if flag else "band_2_17_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_18(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_2_18_high" if flag else "band_2_18_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_19(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_2_19_high" if flag else "band_2_19_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_20(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_2_20_high" if flag else "band_2_20_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_21(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_2_21_high" if flag else "band_2_21_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_22(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_2_22_high" if flag else "band_2_22_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_23(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_2_23_high" if flag else "band_2_23_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_24(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_2_24_high" if flag else "band_2_24_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_25(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_2_25_high" if flag else "band_2_25_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_26(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_2_26_high" if flag else "band_2_26_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_27(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_2_27_high" if flag else "band_2_27_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_28(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_2_28_high" if flag else "band_2_28_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_29(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_2_29_high" if flag else "band_2_29_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_30(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_2_30_high" if flag else "band_2_30_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_31(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_2_31_high" if flag else "band_2_31_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_32(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_2_32_high" if flag else "band_2_32_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_33(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_2_33_high" if flag else "band_2_33_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_34(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_2_34_high" if flag else "band_2_34_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_35(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_2_35_high" if flag else "band_2_35_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_36(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_2_36_high" if flag else "band_2_36_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_37(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_2_37_high" if flag else "band_2_37_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_38(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_2_38_high" if flag else "band_2_38_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_39(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_2_39_high" if flag else "band_2_39_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_40(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_2_40_high" if flag else "band_2_40_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_41(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_2_41_high" if flag else "band_2_41_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_42(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_2_42_high" if flag else "band_2_42_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_43(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_2_43_high" if flag else "band_2_43_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_44(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_2_44_high" if flag else "band_2_44_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_45(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_2_45_high" if flag else "band_2_45_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_46(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_2_46_high" if flag else "band_2_46_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_47(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_2_47_high" if flag else "band_2_47_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_48(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_2_48_high" if flag else "band_2_48_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_49(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_2_49_high" if flag else "band_2_49_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_50(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_2_50_high" if flag else "band_2_50_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_51(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_2_51_high" if flag else "band_2_51_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_52(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_2_52_high" if flag else "band_2_52_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_53(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_2_53_high" if flag else "band_2_53_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_54(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_2_54_high" if flag else "band_2_54_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_55(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_2_55_high" if flag else "band_2_55_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_56(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_2_56_high" if flag else "band_2_56_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_57(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_2_57_high" if flag else "band_2_57_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_58(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_2_58_high" if flag else "band_2_58_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_59(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_2_59_high" if flag else "band_2_59_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_60(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_2_60_high" if flag else "band_2_60_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_61(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_2_61_high" if flag else "band_2_61_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_62(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_2_62_high" if flag else "band_2_62_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_63(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_2_63_high" if flag else "band_2_63_low"
    return TransformReport2(value, flag, label)


def clinical_transform_2_64(age: float, ae: float, risk: float, month: int) -> TransformReport2:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_2_64_high" if flag else "band_2_64_low"
    return TransformReport2(value, flag, label)
