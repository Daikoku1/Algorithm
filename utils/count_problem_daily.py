from pathlib import Path

def count_problem_by_source():
    directory_list = ['백준', 'Codeup', 'LeetCode', 'Programmers']
    problem_count = []
    for d_path in directory_list:
        code_path = Path.cwd() / d_path
        problem_count.append(len(list(code_path.glob('*.ipynb'))))

    count_info = f"#### 현재까지 풀어본 총 문제 수 : {sum(problem_count)}개\n"
    for name, cnt in zip(directory_list, problem_count):
        count_info += f"- {name} - {cnt}개\n"
    return count_info

def make_readme(count_info):
    return f"""# Algorithm
    =====
- 모든 문제는 Python3로 작성되었습니다.
- 문제는 별도로 기재하지 않으며, 동일한 제목으로 출처사이트에서 문제를 확인할 수 있습니다.
- 몇몇 문제의 경우에는 [블로그](https://blog.naver.com/jjys9047)에 문제풀이 아이디어와 코드 설명이 포스팅되어 있습니다.
- 코드에 기재된 time은 해당 코드의 구동시간으로, 컴퓨터의 성능, 인터넷의 연결 상태 등에 달라질 수 있습니다. 코드간 상대적 비교에만 사용하시기 바랍니다.
{count_info}
### 문제 출처
- [Programmers](https://programmers.co.kr/)
- [LeetCode](https://leetcode.com/)
- [백준](https://www.acmicpc.net/)
- [Codeup](https://codeup.kr/index.php)""" 


def update_readme():
    count_info = count_problem_by_source()
    readme = make_readme(count_info)
    return readme 


if __name__ == "__main__": 
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f: 
        f.write(readme)


