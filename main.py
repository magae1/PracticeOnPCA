from parser import CSVParser
import numpy as np
import matplotlib.pyplot as plot

# 데이터 로드 이후 파싱
csv_parser = CSVParser('winequality-red.csv')
csv_parser.parse()
data = np.array(csv_parser.data)
score = data[:, -1]
data = data[:, :-1]

print(f'데이터{data.shape}')
print(data)

# 공분산 행렬(D X D) 생성
cov_matrix = np.cov(data.T)

print(f'공분산 행렬{cov_matrix.shape}')
print(cov_matrix)

# 공분산 행렬로부터 고유값과 고유벡터를 계산
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print(f'고유값{eigenvalues.shape}')
print(eigenvalues)
print(f'고유벡터{eigenvectors.shape}')
print(eigenvectors)

# 2차원의 부분 공간 생성을 위한 고유벡터 찾기
col, row = eigenvectors.shape
max_var = 0
max_vec_idx = (-1, -1)
for i in range(col - 1):
    for j in range(i+1, col):
        fst_vec = eigenvectors[i]
        sec_vec = eigenvectors[j]
        subspace = np.vstack((fst_vec, sec_vec)).T
        projected_data = np.dot(data, subspace)
        var = projected_data.var()
        if max_var < var:
            max_var = var
            max_vec_idx = (i, j)

print(f'차원 축소된 데이터들의 분산들 중 최대 분산: {max_var}')
print(f'해당하는 부분 공간을 이루는 고유벡터들의 인덱스: {max_vec_idx}')

# 부분공간으로 사영
subspace = np.vstack((eigenvectors[max_vec_idx[0]], eigenvectors[max_vec_idx[1]])).T
projected_data = np.dot(data, subspace)

print(f'부분 공간으로 사영된 데이터{projected_data.shape}')
print(projected_data)

# 사영된 데이터에 대한 정보 요약
print(f'평균: {projected_data.mean(axis=0)}')
print(f'분산: {projected_data.var(axis=0)}')
print(f'표준 편차: {np.sqrt(projected_data.var(axis=0))}')
print(f'최댓값: {np.max(projected_data, axis=0)}')
print(f'최솟값: {np.min(projected_data, axis=0)}')

plot.scatter(projected_data[:, 0], projected_data[:, 1], c=score, cmap='plasma')
plot.show()