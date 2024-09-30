n, m = map(int,input().split())

# 최대공약수 : GCD(n,m) = GCD(m,n%m) (while n%m==0)
def GCD(n,m):
    if m==0:
        return n
    else:
        return GCD(m,n%m)

print(GCD(n,m))

# 최소공배수
print(n//GCD(n,m)*m)

