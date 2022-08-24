def enqueue(item):
    global rear

    # isFull
    if rear == size-1:
        print("큐가 가득 찼습니다.")
    else:
        rear += 1
        queue[rear] = item
        print(queue[rear])


def dequeue():
    global front

    # isEmpty
    if rear == front:
        print("큐가 비어 있습니다.")
    else:
        front += 1
        print(queue[front])


front = -1
rear = -1
size = 5
queue = [0] * size

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()