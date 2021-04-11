s1 = input()
s2 = input()
s3 = input()

alphas = [ c for c in s1 ] + [ c for c in s2 ] + [ c for c in s3 ]
alphas = list(set(alphas))
alpha_dict = dict(zip(alphas,[ 0 * 10]))
num_flags = [ 0 * 10]

p=range(10)
flag = 0
for idx in range(len(s3)):
    for q in itertools.permutations(p,3):
        alpha_dict[s1[idx]],alpha_dict[s2[idx]],alpha_dict[s3[idx]] = q
        if (alpha_dict[s1[idx]]==alpha_dict[s2[idx]] and s1[idx]!=s2[idx]) or 
            (alpha_dict[s2[idx]]==alpha_dict[s3[idx]] and s2[idx]!=s3[idx]) or
            (alpha_dict[s1[idx]]==alpha_dict[s3[idx]] and s1[idx]!=s3[idx]):
            break
        elif alpha_dict[s1[idx]]+alpha_dict[s2[idx]]+flag==alpha_dict[s3[idx]]:
            flag=0
            pass
        elif (alpha_dict[s1[idx]]+alpha_dict[s2[idx]]+flag==alpha_dict[s3[idx]]+10):
            flag = 1


