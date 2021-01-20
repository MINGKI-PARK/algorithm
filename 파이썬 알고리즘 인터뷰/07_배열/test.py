nums = [1, 2, 3, 4]
out = []
p = 1

for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]
print(out)

p = 1

for i in range(len(nums)-1, 0-1, -1):
    print(i)
    out[i] = out[i] * p
    p = p * nums[i]

print(out)