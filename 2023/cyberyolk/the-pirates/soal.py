import hashlib


def onClick(view):
    main_activity = MainActivity()
    obj = main_activity.f1871w.getText().toString()
    length = len(obj)
    iArr = [ord(obj[i]) << 1 for i in range(length)]
    textView = main_activity.f1872x
    sb = "Encrypted: "

    if len(obj) == 41:
        i6 = sum(ord(obj[i]) for i in range(1, len(obj), 2))
        if i6 == 1679:
            i8 = sum(ord(obj[i]) for i in range(0, len(obj), 2))
            if i8 != 1729:
                pass  # No change in textView and sb
            else:
                try:
                    digest = hashlib.sha256(obj.encode("utf-8")).hexdigest()
                    if (
                        digest
                        != "be18ea5292734e86ede79110c94735d173ea0fafc5139f2340eec024d753f624"
                    ):
                        pass  # No change in textView and sb
                    else:
                        bArr = bytearray(length)
                        i11 = 12
                        while i11 < 19:
                            bArr[i11 - 12] = iArr[i11] ^ 80
                            i11 += 1

                        bArr2 = bytearray([-64, 48, -2, -18, -118, -94, -18])
                        i12 = sum(1 for i13 in range(7) if bArr[i13] == bArr2[i13])
                        if i12 == 7:
                            iArr2 = [iArr[i3] + iArr[i3 + 1] for i3 in range(19, 27)]
                            i16 = sum(
                                1
                                for i17 in range(8)
                                if iArr2[i17]
                                == [258, 326, 332, 336, 334, 268, 356, 296][i17]
                            )
                            if i16 != 8:
                                pass  # No change in textView and sb
                            else:
                                cArr = list(obj)
                                cArr2 = [""] * 10
                                for i4 in range(27, 37):
                                    cArr[i4 - 27] = obj[i4]

                                for i18 in range(5):
                                    cArr[i18], cArr[9 - i18] = cArr[9 - i18], cArr[i18]
                                    cArr2[i18] = cArr[i18]
                                    cArr2[9 - i18] = cArr[9 - i18]

                                if "".join(cArr2) == "a5S3M_DnE5":
                                    iArr4 = [
                                        134,
                                        132,
                                        178,
                                        246,
                                        232,
                                        144,
                                        98,
                                        230,
                                        190,
                                        98,
                                        230,
                                        190,
                                    ]
                                    i20 = sum(
                                        1
                                        for i21 in range(12)
                                        if iArr4[i21] == iArr[i21]
                                    )
                                    if i20 == 12:
                                        str = "Correct!\n Here is the flag: " + obj
                                        textView.setText(str)
                                else:
                                    pass  # No change in textView and sb
                        else:
                            pass  # No change in textView and sb
                except (UnicodeEncodeError, AttributeError):
                    pass  # No change in textView and sb
        else:
            pass  # No change in textView and sb
    else:
        pass  # No change in textView and sb

    str = sb
    textView.setText(str)
