import sys
sys.stdin = open('홀수더하기.txt', 'r')
#홀수더하기 파일을 불러옴

N = input()
#첫번째줄 3을 불러옴
#print(type(N)) - str 형태로 불러옴

N = int(N)
#str 형태를 int 형태로 변환

for line in range(N):
#세줄 반복적으로 불러옴
    l = list(map(int, input().split()))
    #세 줄을 불러와서 각각 spilt로 쪼갬
    #쪼갠걸 숫자형태로 바꿔줌, map으로 변경
    #map(바꾸고싶은 형태, 나머지 전체)
    #map 전체를 list화

    res = 0
    #더하기 전 시작점
    for num in l:
    #한줄 안에 데이터 10개를 불러옴
        if num % 2 == 1:
            res += num
            #res = res+num을 축약
    print(f'#{line+1} {res}')