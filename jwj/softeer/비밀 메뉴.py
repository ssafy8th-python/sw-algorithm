M, N, K = map(int, input().split())

secret = input()
click_btn = input()

if secret in click_btn:
    print("secret")
else:
    print("normal")
