import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport7:
    value: float
    flag: bool
    label: str


def clinical_transform_7_0(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_7_0_high" if flag else "band_7_0_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_1(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_7_1_high" if flag else "band_7_1_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_2(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_7_2_high" if flag else "band_7_2_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_3(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_7_3_high" if flag else "band_7_3_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_4(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_7_4_high" if flag else "band_7_4_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_5(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_7_5_high" if flag else "band_7_5_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_6(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_7_6_high" if flag else "band_7_6_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_7(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_7_7_high" if flag else "band_7_7_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_8(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_7_8_high" if flag else "band_7_8_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_9(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_7_9_high" if flag else "band_7_9_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_10(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_7_10_high" if flag else "band_7_10_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_11(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_7_11_high" if flag else "band_7_11_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_12(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_7_12_high" if flag else "band_7_12_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_13(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_7_13_high" if flag else "band_7_13_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_14(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_7_14_high" if flag else "band_7_14_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_15(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_7_15_high" if flag else "band_7_15_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_16(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_7_16_high" if flag else "band_7_16_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_17(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_7_17_high" if flag else "band_7_17_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_18(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_7_18_high" if flag else "band_7_18_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_19(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_7_19_high" if flag else "band_7_19_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_20(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_7_20_high" if flag else "band_7_20_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_21(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_7_21_high" if flag else "band_7_21_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_22(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_7_22_high" if flag else "band_7_22_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_23(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_7_23_high" if flag else "band_7_23_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_24(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_7_24_high" if flag else "band_7_24_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_25(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_7_25_high" if flag else "band_7_25_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_26(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_7_26_high" if flag else "band_7_26_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_27(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_7_27_high" if flag else "band_7_27_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_28(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_7_28_high" if flag else "band_7_28_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_29(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_7_29_high" if flag else "band_7_29_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_30(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_7_30_high" if flag else "band_7_30_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_31(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_7_31_high" if flag else "band_7_31_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_32(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_7_32_high" if flag else "band_7_32_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_33(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_7_33_high" if flag else "band_7_33_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_34(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_7_34_high" if flag else "band_7_34_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_35(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_7_35_high" if flag else "band_7_35_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_36(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_7_36_high" if flag else "band_7_36_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_37(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_7_37_high" if flag else "band_7_37_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_38(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_7_38_high" if flag else "band_7_38_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_39(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_7_39_high" if flag else "band_7_39_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_40(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_7_40_high" if flag else "band_7_40_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_41(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_7_41_high" if flag else "band_7_41_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_42(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_7_42_high" if flag else "band_7_42_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_43(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_7_43_high" if flag else "band_7_43_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_44(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_7_44_high" if flag else "band_7_44_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_45(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_7_45_high" if flag else "band_7_45_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_46(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_7_46_high" if flag else "band_7_46_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_47(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_7_47_high" if flag else "band_7_47_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_48(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_7_48_high" if flag else "band_7_48_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_49(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_7_49_high" if flag else "band_7_49_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_50(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_7_50_high" if flag else "band_7_50_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_51(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_7_51_high" if flag else "band_7_51_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_52(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_7_52_high" if flag else "band_7_52_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_53(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_7_53_high" if flag else "band_7_53_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_54(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_7_54_high" if flag else "band_7_54_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_55(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_7_55_high" if flag else "band_7_55_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_56(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_7_56_high" if flag else "band_7_56_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_57(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_7_57_high" if flag else "band_7_57_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_58(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_7_58_high" if flag else "band_7_58_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_59(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_7_59_high" if flag else "band_7_59_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_60(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_7_60_high" if flag else "band_7_60_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_61(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_7_61_high" if flag else "band_7_61_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_62(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_7_62_high" if flag else "band_7_62_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_63(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_7_63_high" if flag else "band_7_63_low"
    return TransformReport7(value, flag, label)


def clinical_transform_7_64(age: float, ae: float, risk: float, month: int) -> TransformReport7:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_7_64_high" if flag else "band_7_64_low"
    return TransformReport7(value, flag, label)
