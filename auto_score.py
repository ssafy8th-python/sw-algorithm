import json
import os

jwj_baek = os.listdir('jwj/baek/3class')
jwj_swea = os.listdir('jwj/swea/D1-D2')


with open('/workspace/sw-algorithm/score.txt', 'w', encoding='utf-8') as make_file:
    make_file.write(f'정원재\n백준 해결한 문제 : {len(jwj_baek)}\nSW Expert Academy 해결한 문제 : {len(jwj_swea)}\n총 해결한 문제{len(jwj_baek) + len(jwj_swea)}')
    

os.system('git pull')
os.system('git add *')
os.system('git commit -m "auto score system operate"')
os.system('git push')
