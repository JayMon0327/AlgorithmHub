
# 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #데이터의 갯수 -1 까지 반복함
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프(파이썬 스왑연산)

print(array)
# [0,1,2,3,4,5,6,7,8,9]




# 삽입 정렬 
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j] #스와프
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
#[0,1,2,3,4,5,6,7,8,9]




# 퀵 정렬

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)
# [0,1,2,3,4,5,6,7,8,9]




# 퀵 정렬 : 파이썬의 장점을 살린 방식

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트(= 2번째 원소부터 마지막원소까지)

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
# [0,1,2,3,4,5,6,7,8,9]




# 계수정렬

#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+ 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 





# <문제> 두 배열의 원소 교체

n, k = map(int, input().split()) #N과 K를 입력받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() #배열 A는 오름차순 정렬 수행
b.sort(reverse=True) #배열 B는 내림차순 정렬 수행

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break
print(sum(a)) #배열 A의 모든 원소의 합을 출력