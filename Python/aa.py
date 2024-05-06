# R와 S 데이터 정의
R = [(1, 1, 1), (2, 1, 2), (3, 2, 2), (4, 3, 3)]
S = [(1, 5, 1), (2, 6, 2), (3, 7, 3)]

# 조인 연산 수행
result = []
for r_row in R:
    for s_row in S:
        if r_row[2] > s_row[0]:  # R.C > S.C 조건
            result.append(r_row + s_row)

# 결과 출력
for row in result:
    print(row)
