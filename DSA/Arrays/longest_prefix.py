def long_comm_pref(strs):
        if not strs:
            return ""
        ref=strs[0]
        for i in range(len(ref)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return ref[:i]
                elif ref[i]!=strs[j][i]:
                    return ref[:i]
        return ref
