import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport3:
    value: float
    flag: bool
    label: str


def clinical_transform_3_0(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_3_0_high" if flag else "band_3_0_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_1(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_3_1_high" if flag else "band_3_1_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_2(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_3_2_high" if flag else "band_3_2_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_3(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_3_3_high" if flag else "band_3_3_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_4(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_3_4_high" if flag else "band_3_4_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_5(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_3_5_high" if flag else "band_3_5_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_6(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_3_6_high" if flag else "band_3_6_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_7(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_3_7_high" if flag else "band_3_7_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_8(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_3_8_high" if flag else "band_3_8_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_9(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_3_9_high" if flag else "band_3_9_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_10(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_3_10_high" if flag else "band_3_10_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_11(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_3_11_high" if flag else "band_3_11_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_12(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_3_12_high" if flag else "band_3_12_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_13(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_3_13_high" if flag else "band_3_13_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_14(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_3_14_high" if flag else "band_3_14_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_15(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_3_15_high" if flag else "band_3_15_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_16(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_3_16_high" if flag else "band_3_16_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_17(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_3_17_high" if flag else "band_3_17_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_18(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_3_18_high" if flag else "band_3_18_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_19(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_3_19_high" if flag else "band_3_19_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_20(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_3_20_high" if flag else "band_3_20_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_21(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_3_21_high" if flag else "band_3_21_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_22(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_3_22_high" if flag else "band_3_22_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_23(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_3_23_high" if flag else "band_3_23_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_24(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_3_24_high" if flag else "band_3_24_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_25(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_3_25_high" if flag else "band_3_25_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_26(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_3_26_high" if flag else "band_3_26_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_27(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_3_27_high" if flag else "band_3_27_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_28(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_3_28_high" if flag else "band_3_28_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_29(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_3_29_high" if flag else "band_3_29_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_30(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_3_30_high" if flag else "band_3_30_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_31(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_3_31_high" if flag else "band_3_31_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_32(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_3_32_high" if flag else "band_3_32_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_33(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_3_33_high" if flag else "band_3_33_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_34(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_3_34_high" if flag else "band_3_34_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_35(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_3_35_high" if flag else "band_3_35_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_36(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_3_36_high" if flag else "band_3_36_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_37(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_3_37_high" if flag else "band_3_37_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_38(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_3_38_high" if flag else "band_3_38_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_39(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_3_39_high" if flag else "band_3_39_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_40(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_3_40_high" if flag else "band_3_40_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_41(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_3_41_high" if flag else "band_3_41_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_42(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_3_42_high" if flag else "band_3_42_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_43(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_3_43_high" if flag else "band_3_43_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_44(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_3_44_high" if flag else "band_3_44_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_45(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_3_45_high" if flag else "band_3_45_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_46(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_3_46_high" if flag else "band_3_46_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_47(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_3_47_high" if flag else "band_3_47_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_48(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_3_48_high" if flag else "band_3_48_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_49(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_3_49_high" if flag else "band_3_49_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_50(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_3_50_high" if flag else "band_3_50_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_51(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_3_51_high" if flag else "band_3_51_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_52(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_3_52_high" if flag else "band_3_52_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_53(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_3_53_high" if flag else "band_3_53_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_54(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_3_54_high" if flag else "band_3_54_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_55(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_3_55_high" if flag else "band_3_55_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_56(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_3_56_high" if flag else "band_3_56_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_57(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_3_57_high" if flag else "band_3_57_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_58(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_3_58_high" if flag else "band_3_58_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_59(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_3_59_high" if flag else "band_3_59_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_60(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_3_60_high" if flag else "band_3_60_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_61(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_3_61_high" if flag else "band_3_61_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_62(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_3_62_high" if flag else "band_3_62_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_63(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_3_63_high" if flag else "band_3_63_low"
    return TransformReport3(value, flag, label)


def clinical_transform_3_64(age: float, ae: float, risk: float, month: int) -> TransformReport3:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_3_64_high" if flag else "band_3_64_low"
    return TransformReport3(value, flag, label)
