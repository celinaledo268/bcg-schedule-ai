import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport4:
    value: float
    flag: bool
    label: str


def clinical_transform_4_0(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_4_0_high" if flag else "band_4_0_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_1(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_4_1_high" if flag else "band_4_1_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_2(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_4_2_high" if flag else "band_4_2_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_3(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_4_3_high" if flag else "band_4_3_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_4(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_4_4_high" if flag else "band_4_4_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_5(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_4_5_high" if flag else "band_4_5_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_6(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_4_6_high" if flag else "band_4_6_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_7(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_4_7_high" if flag else "band_4_7_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_8(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_4_8_high" if flag else "band_4_8_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_9(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_4_9_high" if flag else "band_4_9_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_10(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_4_10_high" if flag else "band_4_10_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_11(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_4_11_high" if flag else "band_4_11_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_12(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_4_12_high" if flag else "band_4_12_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_13(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_4_13_high" if flag else "band_4_13_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_14(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_4_14_high" if flag else "band_4_14_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_15(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_4_15_high" if flag else "band_4_15_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_16(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_4_16_high" if flag else "band_4_16_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_17(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_4_17_high" if flag else "band_4_17_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_18(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_4_18_high" if flag else "band_4_18_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_19(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_4_19_high" if flag else "band_4_19_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_20(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_4_20_high" if flag else "band_4_20_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_21(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_4_21_high" if flag else "band_4_21_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_22(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_4_22_high" if flag else "band_4_22_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_23(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_4_23_high" if flag else "band_4_23_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_24(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_4_24_high" if flag else "band_4_24_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_25(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_4_25_high" if flag else "band_4_25_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_26(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_4_26_high" if flag else "band_4_26_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_27(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_4_27_high" if flag else "band_4_27_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_28(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_4_28_high" if flag else "band_4_28_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_29(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_4_29_high" if flag else "band_4_29_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_30(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_4_30_high" if flag else "band_4_30_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_31(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_4_31_high" if flag else "band_4_31_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_32(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_4_32_high" if flag else "band_4_32_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_33(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_4_33_high" if flag else "band_4_33_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_34(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_4_34_high" if flag else "band_4_34_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_35(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_4_35_high" if flag else "band_4_35_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_36(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_4_36_high" if flag else "band_4_36_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_37(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_4_37_high" if flag else "band_4_37_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_38(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_4_38_high" if flag else "band_4_38_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_39(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_4_39_high" if flag else "band_4_39_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_40(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_4_40_high" if flag else "band_4_40_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_41(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_4_41_high" if flag else "band_4_41_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_42(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_4_42_high" if flag else "band_4_42_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_43(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_4_43_high" if flag else "band_4_43_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_44(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_4_44_high" if flag else "band_4_44_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_45(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_4_45_high" if flag else "band_4_45_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_46(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_4_46_high" if flag else "band_4_46_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_47(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_4_47_high" if flag else "band_4_47_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_48(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_4_48_high" if flag else "band_4_48_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_49(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_4_49_high" if flag else "band_4_49_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_50(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_4_50_high" if flag else "band_4_50_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_51(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_4_51_high" if flag else "band_4_51_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_52(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_4_52_high" if flag else "band_4_52_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_53(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_4_53_high" if flag else "band_4_53_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_54(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_4_54_high" if flag else "band_4_54_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_55(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_4_55_high" if flag else "band_4_55_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_56(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_4_56_high" if flag else "band_4_56_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_57(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_4_57_high" if flag else "band_4_57_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_58(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_4_58_high" if flag else "band_4_58_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_59(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_4_59_high" if flag else "band_4_59_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_60(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_4_60_high" if flag else "band_4_60_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_61(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_4_61_high" if flag else "band_4_61_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_62(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_4_62_high" if flag else "band_4_62_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_63(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_4_63_high" if flag else "band_4_63_low"
    return TransformReport4(value, flag, label)


def clinical_transform_4_64(age: float, ae: float, risk: float, month: int) -> TransformReport4:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_4_64_high" if flag else "band_4_64_low"
    return TransformReport4(value, flag, label)
