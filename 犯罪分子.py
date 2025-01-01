for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            for D in [False, True]:
                for E in [False, True]:
                    for F in [False, True]:
                        if (A or B) and ((A and E) or (A and F) or (E and F)) and not (A and D) and ((B and C) or (not B and not C)) and ((C and not D) or (not C and D)) and (not D or not E):
                            criminals = []
                            if A:
                                criminals.append('A')
                            if B:
                                criminals.append('B')
                            if C:
                                criminals.append('C')
                            if D:
                                criminals.append('D')
                            if E:
                                criminals.append('E')
                            if F:
                                criminals.append('F')
                            print(f"罪犯是：{', '.join(criminals)}")