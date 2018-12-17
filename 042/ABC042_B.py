import sys
t_list = []
for i in sys.stdin.readlines():
    t_list.append(i.rstrip())
t_list.pop(0)
 
def solution(t_list):
    t_list.sort()
    ans_str = ""
    for i in t_list:
        ans_str += i
    return ans_str
    
def main():
    print(solution(t_list))
    
if __name__ == '__main__':
    main()