import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TransformReport1:
    value: float
    flag: bool
    label: str


def clinical_transform_1_0(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 0) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_1_0_high" if flag else "band_1_0_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_1(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 1) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_1_1_high" if flag else "band_1_1_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_2(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 2) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_1_2_high" if flag else "band_1_2_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_3(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 3) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_1_3_high" if flag else "band_1_3_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_4(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 4) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_1_4_high" if flag else "band_1_4_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_5(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 5) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_1_5_high" if flag else "band_1_5_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_6(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 6) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_1_6_high" if flag else "band_1_6_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_7(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 7) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_1_7_high" if flag else "band_1_7_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_8(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 8) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_1_8_high" if flag else "band_1_8_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_9(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 9) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_1_9_high" if flag else "band_1_9_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_10(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 10) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_1_10_high" if flag else "band_1_10_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_11(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 11) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_1_11_high" if flag else "band_1_11_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_12(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 12) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_1_12_high" if flag else "band_1_12_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_13(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 13) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_1_13_high" if flag else "band_1_13_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_14(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 14) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_1_14_high" if flag else "band_1_14_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_15(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 15) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_1_15_high" if flag else "band_1_15_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_16(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 16) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_1_16_high" if flag else "band_1_16_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_17(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 17) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_1_17_high" if flag else "band_1_17_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_18(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 18) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_1_18_high" if flag else "band_1_18_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_19(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 19) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_1_19_high" if flag else "band_1_19_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_20(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 20) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.20
    label = "band_1_20_high" if flag else "band_1_20_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_21(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 21) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.10
    label = "band_1_21_high" if flag else "band_1_21_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_22(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 22) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.00
    label = "band_1_22_high" if flag else "band_1_22_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_23(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 23) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.10
    label = "band_1_23_high" if flag else "band_1_23_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_24(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 24) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.20
    label = "band_1_24_high" if flag else "band_1_24_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_25(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 25) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.30
    label = "band_1_25_high" if flag else "band_1_25_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_26(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 26) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.40
    label = "band_1_26_high" if flag else "band_1_26_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_27(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 27) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.40
    label = "band_1_27_high" if flag else "band_1_27_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_28(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 28) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.30
    label = "band_1_28_high" if flag else "band_1_28_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_29(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 29) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.20
    label = "band_1_29_high" if flag else "band_1_29_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_30(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 30) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.10
    label = "band_1_30_high" if flag else "band_1_30_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_31(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 31) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.00
    label = "band_1_31_high" if flag else "band_1_31_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_32(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 32) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.10
    label = "band_1_32_high" if flag else "band_1_32_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_33(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 33) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.20
    label = "band_1_33_high" if flag else "band_1_33_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_34(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 34) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.30
    label = "band_1_34_high" if flag else "band_1_34_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_35(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 35) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.40
    label = "band_1_35_high" if flag else "band_1_35_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_36(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 36) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.40
    label = "band_1_36_high" if flag else "band_1_36_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_37(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 37) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.30
    label = "band_1_37_high" if flag else "band_1_37_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_38(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 38) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.20
    label = "band_1_38_high" if flag else "band_1_38_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_39(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 39) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.10
    label = "band_1_39_high" if flag else "band_1_39_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_40(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 40) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.00
    label = "band_1_40_high" if flag else "band_1_40_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_41(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 41) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.10
    label = "band_1_41_high" if flag else "band_1_41_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_42(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 42) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.20
    label = "band_1_42_high" if flag else "band_1_42_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_43(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 43) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.30
    label = "band_1_43_high" if flag else "band_1_43_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_44(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 44) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.40
    label = "band_1_44_high" if flag else "band_1_44_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_45(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 45) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.40
    label = "band_1_45_high" if flag else "band_1_45_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_46(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 46) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.30
    label = "band_1_46_high" if flag else "band_1_46_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_47(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 47) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.20
    label = "band_1_47_high" if flag else "band_1_47_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_48(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 48) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.10
    label = "band_1_48_high" if flag else "band_1_48_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_49(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 49) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.00
    label = "band_1_49_high" if flag else "band_1_49_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_50(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 50) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.10
    label = "band_1_50_high" if flag else "band_1_50_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_51(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 51) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.20
    label = "band_1_51_high" if flag else "band_1_51_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_52(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 52) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.30
    label = "band_1_52_high" if flag else "band_1_52_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_53(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 53) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.40
    label = "band_1_53_high" if flag else "band_1_53_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_54(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 54) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.40
    label = "band_1_54_high" if flag else "band_1_54_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_55(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 55) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > -0.30
    label = "band_1_55_high" if flag else "band_1_55_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_56(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 56) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > -0.20
    label = "band_1_56_high" if flag else "band_1_56_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_57(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 57) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > -0.10
    label = "band_1_57_high" if flag else "band_1_57_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_58(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 3.0 / 10.0)
    seasonal = math.sin((month + 58) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > 0.00
    label = "band_1_58_high" if flag else "band_1_58_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_59(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 4.0 / 10.0)
    seasonal = math.sin((month + 59) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > 0.10
    label = "band_1_59_high" if flag else "band_1_59_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_60(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 5.0 / 10.0)
    seasonal = math.sin((month + 60) * 0.08333333333333333)
    value = base + seasonal - ae * 0.05
    flag = value > 0.20
    label = "band_1_60_high" if flag else "band_1_60_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_61(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 6.0 / 10.0)
    seasonal = math.sin((month + 61) * 0.08333333333333333)
    value = base + seasonal - ae * 0.10
    flag = value > 0.30
    label = "band_1_61_high" if flag else "band_1_61_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_62(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 7.0 / 10.0)
    seasonal = math.sin((month + 62) * 0.08333333333333333)
    value = base + seasonal - ae * 0.15
    flag = value > 0.40
    label = "band_1_62_high" if flag else "band_1_62_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_63(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 1.0 / 10.0)
    seasonal = math.sin((month + 63) * 0.08333333333333333)
    value = base + seasonal - ae * 0.20
    flag = value > -0.40
    label = "band_1_63_high" if flag else "band_1_63_low"
    return TransformReport1(value, flag, label)


def clinical_transform_1_64(age: float, ae: float, risk: float, month: int) -> TransformReport1:
    base = math.tanh((age - 70.0) / 18.0 + risk * 2.0 / 10.0)
    seasonal = math.sin((month + 64) * 0.08333333333333333)
    value = base + seasonal - ae * 0.25
    flag = value > -0.30
    label = "band_1_64_high" if flag else "band_1_64_low"
    return TransformReport1(value, flag, label)
