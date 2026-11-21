import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport5:
    value: float
    flag: bool
    label: str


def clinical_transform_5_0(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_5_0_high" if flag else "band_5_0_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_1(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_5_1_high" if flag else "band_5_1_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_2(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_5_2_high" if flag else "band_5_2_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_3(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_5_3_high" if flag else "band_5_3_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_4(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_5_4_high" if flag else "band_5_4_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_5(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_5_5_high" if flag else "band_5_5_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_6(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_5_6_high" if flag else "band_5_6_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_7(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_5_7_high" if flag else "band_5_7_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_8(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_5_8_high" if flag else "band_5_8_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_9(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_5_9_high" if flag else "band_5_9_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_10(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_5_10_high" if flag else "band_5_10_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_11(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_5_11_high" if flag else "band_5_11_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_12(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_5_12_high" if flag else "band_5_12_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_13(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_5_13_high" if flag else "band_5_13_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_14(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_5_14_high" if flag else "band_5_14_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_15(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_5_15_high" if flag else "band_5_15_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_16(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_5_16_high" if flag else "band_5_16_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_17(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_5_17_high" if flag else "band_5_17_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_18(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_5_18_high" if flag else "band_5_18_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_19(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_5_19_high" if flag else "band_5_19_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_20(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_5_20_high" if flag else "band_5_20_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_21(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_5_21_high" if flag else "band_5_21_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_22(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_5_22_high" if flag else "band_5_22_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_23(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_5_23_high" if flag else "band_5_23_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_24(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_5_24_high" if flag else "band_5_24_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_25(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_5_25_high" if flag else "band_5_25_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_26(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_5_26_high" if flag else "band_5_26_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_27(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_5_27_high" if flag else "band_5_27_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_28(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_5_28_high" if flag else "band_5_28_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_29(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_5_29_high" if flag else "band_5_29_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_30(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_5_30_high" if flag else "band_5_30_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_31(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_5_31_high" if flag else "band_5_31_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_32(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_5_32_high" if flag else "band_5_32_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_33(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_5_33_high" if flag else "band_5_33_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_34(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_5_34_high" if flag else "band_5_34_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_35(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_5_35_high" if flag else "band_5_35_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_36(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_5_36_high" if flag else "band_5_36_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_37(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_5_37_high" if flag else "band_5_37_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_38(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_5_38_high" if flag else "band_5_38_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_39(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_5_39_high" if flag else "band_5_39_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_40(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_5_40_high" if flag else "band_5_40_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_41(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_5_41_high" if flag else "band_5_41_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_42(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_5_42_high" if flag else "band_5_42_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_43(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_5_43_high" if flag else "band_5_43_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_44(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_5_44_high" if flag else "band_5_44_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_45(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_5_45_high" if flag else "band_5_45_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_46(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_5_46_high" if flag else "band_5_46_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_47(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_5_47_high" if flag else "band_5_47_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_48(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_5_48_high" if flag else "band_5_48_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_49(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_5_49_high" if flag else "band_5_49_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_50(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_5_50_high" if flag else "band_5_50_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_51(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_5_51_high" if flag else "band_5_51_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_52(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_5_52_high" if flag else "band_5_52_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_53(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_5_53_high" if flag else "band_5_53_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_54(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_5_54_high" if flag else "band_5_54_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_55(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_5_55_high" if flag else "band_5_55_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_56(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_5_56_high" if flag else "band_5_56_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_57(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_5_57_high" if flag else "band_5_57_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_58(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_5_58_high" if flag else "band_5_58_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_59(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_5_59_high" if flag else "band_5_59_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_60(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_5_60_high" if flag else "band_5_60_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_61(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_5_61_high" if flag else "band_5_61_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_62(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_5_62_high" if flag else "band_5_62_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_63(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_5_63_high" if flag else "band_5_63_low"
    return TransformReport5(value, flag, label)


def clinical_transform_5_64(age: float, ae: float, risk: float, month: int) -> TransformReport5:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_5_64_high" if flag else "band_5_64_low"
    return TransformReport5(value, flag, label)
