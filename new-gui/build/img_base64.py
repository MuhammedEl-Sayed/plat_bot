from tkinter import *
def img1():
    return PhotoImage("frameFocusBorder", data="""
R0lGODlhQABAAOYAAAAAFWtpazs5O0NBQ1NRU0tJS2NhY1tZW3Nxc4OBg0tJ
TGVjZmRiZkdGSDw6QDQyOUdFTC0sMkA/RTY1PB8eJyYlLwwLHB0bOBEQIRQT
IwYFGgYFGAkIGygnSQAAFAEBFgEBFQEBFAEBEgICFwICFgMDFwMDFgQEGAQE
FwUFGAYGGQcHGgcHGQoKGwsLHQsLHAwMHQ4OHhISIhERIBQUIBsbKQABFQQF
GB8gLBYXICQlLDc4PTM0ODk6PiYoLzc5PTAyNEVHR09RUDs9O0NFQ1NVU0tN
S2NlY1tdW1pcWnt9e3N1c2tta////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAUAAE0A
LAAAAABAAEAAAAf/gACCg4SFhoeIiYqLjI2Oj5CRkpOUlZaOE0IBR0xHAZsB
nZ+eoqClpJ6mqZ5CE5RCSBEkl48kEUgKkC0BObSUFAEpjS0Gs76VR8KLAceX
JMyKQhTNlzlCiSkH1LRIyoY/Q9uXAj2ISMbilBpIiNDpyIhH75buhCD185FH
JYYZ8vmTAsBAB6AEDHwAHR3J0O9fQkgCCRpE+HDRwoYVIQ4kNDHjo4uF/Hl0
FJHjwZGNQBISiXLZxkEdWypSOYilzHYvBcW8eYimIJs8C5WEeTKoIZ8AgBoV
NFRn0aWDkCpd2rTgU6gApDrEWnUnVq1YB3W9ChVsWABjKQY1Gzbt2awM/0Nu
hVrVxgq1PH1+uDGXak4ANkoweOuTxIkFb+uO6Gs0QFxCHAIQNKrhCAwQ9lgY
EBBWgIHLhVYU0YYVSREYhkrsOHIB6oUjRlYYAuEiiWSjz5A4MGHoQwkIR4rx
JGHgSBEZFmZ/wGGgU+uWF0IZkDADc+oaRQIgYGKgg4aKJDo0R3DkgI8WiEqc
CHIgwJL3TDbFnx+qPv379vPPZxL/E4L3SwRwgBExWAdACIV8oIIR7f2nRAIQ
RijhhBRWaGECSiixBAICGlGBNwCI0BsGRhRRHBMI/Afgiiy26OKKKr63XXBF
FKADQR54cMgHLxBBwGgGFCdkcEQOaWSRSA5ZpGMBBxRBABEP8EOIjomQwAIP
DRhhBAFbckmAl2B2KeaXY4ZJphEFDAAEDQYKkuMiIGwAwggqvJABDHfmieee
evbJ5595rrACCmwa8iYkmCUKgKKMLupoo5C2aSiVb00pAqUABAIAOw==""")


def img2():
    return PhotoImage("frameFocusBorder", data="""
R0lGODlhQABAAOYAAAAAFWtpazs5O0NBQ1NRU0tJS2NhY1tZW3Nxc4OBg0tJ
TGVjZmRiZkdGSDw6QDQyOUdFTC0sMkA/RTY1PB8eJyYlLwwLHB0bOBEQIRQT
IwYFGgYFGAkIGygnSQAAFAEBFgEBFQEBFAEBEgICFwICFgMDFwMDFgQEGAQE
FwUFGAYGGQcHGgcHGQoKGwsLHQsLHAwMHQ4OHhISIhERIBQUIBsbKQABFQQF
GB8gLBYXICQlLDc4PTM0ODk6PiYoLzc5PTAyNEVHR09RUDs9O0NFQ1NVU0tN
S2NlY1tdW1pcWnt9e3N1c2tta////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAUAAE0A
LAAAAABAAEAAAAf/gACCg4SFhoeIiYqLjI2Oj5CRkpOUlZaOE0IBR0xHAZsB
nZ+eoqClpJ6mqZ5CE5RCSBEkl48kEUgKkC0BObSUFAEpjS0Gs76VR8KLAceX
JMyKQhTNlzlCiSkH1LRIyoY/Q9uXAj2ISMbilBpIiNDpyIhH75buhCD185FH
JYYZ8vmTAsBAB6AEDHwAHR3J0O9fQkgCCRpE+HDRwoYVIQ4kNDHjo4uF/Hl0
FJHjwZGNQBISiXLZxkEdWypSOYilzHYvBcW8eYimIJs8C5WEeTKoIZ8AgBoV
NFRn0aWDkCpd2rTgU6gApDrEWnUnVq1YB3W9ChVsWABjKQY1Gzbt2awM/0Nu
hVrVxgq1PH1+uDGXak4ANkoweOuTxIkFb+uO6Gs0QFxCHAIQNKrhCAwQ9lgY
EBBWgIHLhVYU0YYVSREYhkrsOHIB6oUjRlYYAuEiiWSjz5A4MGHoQwkIR4rx
JGHgSBEZFmZ/wGGgU+uWF0IZkDADc+oaRQIgYGKgg4aKJDo0R3DkgI8WiEqc
CHIgwJL3TDbFnx+qPv379vPPZxL/E4L3SwRwgBExWAdACIV8oIIR7f2nRAIQ
RijhhBRWaGECSiixBAICGlGBNwCI0BsGRhRRHBMI/Afgiiy26OKKKr63XXBF
FKADQR54cMgHLxBBwGgGFCdkcEQOaWSRSA5ZpGMBBxRBABEP8EOIjomQwAIP
DRhhBAFbckmAl2B2KeaXY4ZJphEFDAAEDQYKkuMiIGwAwggqvJABDHfmieee
evbJ5595rrACCmwa8iYkmCUKgKKMLupoo5C2aSiVb00pAqUABAIAOw==""")