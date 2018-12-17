d= input().rstrip()
d_list = d.split(" ")

def solution(d_list):
    if d_list.count("5") !=2:
        return "NO"
    else:
        if d_list.count("7") !=1:
            return "NO"
        else:
            return "YES"
            
def main():
    print(solution(d_list))
    
if __name__ == '__main__':
    main()