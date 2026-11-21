import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport6:
    value: float
    flag: bool
    label: str


def clinical_transform_6_0(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_6_0_high" if flag else "band_6_0_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_1(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_6_1_high" if flag else "band_6_1_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_2(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_6_2_high" if flag else "band_6_2_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_3(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_6_3_high" if flag else "band_6_3_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_4(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_6_4_high" if flag else "band_6_4_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_5(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_6_5_high" if flag else "band_6_5_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_6(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_6_6_high" if flag else "band_6_6_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_7(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_6_7_high" if flag else "band_6_7_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_8(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_6_8_high" if flag else "band_6_8_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_9(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_6_9_high" if flag else "band_6_9_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_10(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_6_10_high" if flag else "band_6_10_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_11(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_6_11_high" if flag else "band_6_11_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_12(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_6_12_high" if flag else "band_6_12_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_13(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_6_13_high" if flag else "band_6_13_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_14(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_6_14_high" if flag else "band_6_14_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_15(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_6_15_high" if flag else "band_6_15_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_16(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_6_16_high" if flag else "band_6_16_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_17(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_6_17_high" if flag else "band_6_17_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_18(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_6_18_high" if flag else "band_6_18_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_19(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_6_19_high" if flag else "band_6_19_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_20(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_6_20_high" if flag else "band_6_20_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_21(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_6_21_high" if flag else "band_6_21_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_22(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_6_22_high" if flag else "band_6_22_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_23(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_6_23_high" if flag else "band_6_23_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_24(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_6_24_high" if flag else "band_6_24_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_25(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_6_25_high" if flag else "band_6_25_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_26(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_6_26_high" if flag else "band_6_26_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_27(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_6_27_high" if flag else "band_6_27_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_28(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_6_28_high" if flag else "band_6_28_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_29(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_6_29_high" if flag else "band_6_29_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_30(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_6_30_high" if flag else "band_6_30_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_31(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_6_31_high" if flag else "band_6_31_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_32(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_6_32_high" if flag else "band_6_32_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_33(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_6_33_high" if flag else "band_6_33_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_34(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_6_34_high" if flag else "band_6_34_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_35(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_6_35_high" if flag else "band_6_35_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_36(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_6_36_high" if flag else "band_6_36_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_37(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_6_37_high" if flag else "band_6_37_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_38(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_6_38_high" if flag else "band_6_38_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_39(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_6_39_high" if flag else "band_6_39_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_40(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_6_40_high" if flag else "band_6_40_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_41(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_6_41_high" if flag else "band_6_41_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_42(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_6_42_high" if flag else "band_6_42_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_43(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_6_43_high" if flag else "band_6_43_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_44(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_6_44_high" if flag else "band_6_44_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_45(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_6_45_high" if flag else "band_6_45_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_46(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_6_46_high" if flag else "band_6_46_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_47(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_6_47_high" if flag else "band_6_47_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_48(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_6_48_high" if flag else "band_6_48_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_49(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_6_49_high" if flag else "band_6_49_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_50(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_6_50_high" if flag else "band_6_50_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_51(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_6_51_high" if flag else "band_6_51_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_52(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_6_52_high" if flag else "band_6_52_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_53(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_6_53_high" if flag else "band_6_53_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_54(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_6_54_high" if flag else "band_6_54_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_55(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_6_55_high" if flag else "band_6_55_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_56(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_6_56_high" if flag else "band_6_56_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_57(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_6_57_high" if flag else "band_6_57_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_58(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_6_58_high" if flag else "band_6_58_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_59(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_6_59_high" if flag else "band_6_59_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_60(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_6_60_high" if flag else "band_6_60_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_61(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_6_61_high" if flag else "band_6_61_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_62(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_6_62_high" if flag else "band_6_62_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_63(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_6_63_high" if flag else "band_6_63_low"
    return TransformReport6(value, flag, label)


def clinical_transform_6_64(age: float, ae: float, risk: float, month: int) -> TransformReport6:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_6_64_high" if flag else "band_6_64_low"
    return TransformReport6(value, flag, label)
