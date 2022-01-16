#파이썬 한줄 입력
a = list(map(int, input().split()))

#파이썬 여러줄 입력
numArr = []
for i in range(9) :
        numArr.append(int(input()))
        
#반복문에서 input()대신 사용
import sys
int(sys.stdin.readline().strip())

#리스트의 서로 다른 문자 개수 세기
list=list(str(123451))
for i in range (len(list)):
        print("%d는 %d개"%(i,list.count(str(i))))
        
#f-string
# print("%5.3f" %(p/grade[0]*100)+"%")를
#rate=p/grade[0]*100
#print(f"{rate:.3f}%")로 사용 가능