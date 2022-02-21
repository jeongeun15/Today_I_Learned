# 리스트 안의 숫자들의 갯수를 {숫자:갯수} 이렇게 표현하는 방법
lst = [1, 3, 22, 5]

n_dict = dict()

for num in lst:
    if not n_dict.get(num):
        n_dict[num] = 1
    else:
        n_dict[num] += 1
        
print(n_dict)