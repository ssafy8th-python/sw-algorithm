def enqueue(item):
    global rear

    # isFull?
    if (rear + 1) % size == front:
        print("큐가 가득 찼습니다.")

    else:
        rear = (rear + 1) % size
        queue[rear] = item
        print(queue[rear])


def dequeue():
    global front

    # isEmpty?
    if front == rear:
        print('큐가 비어있습니다.')
    else:
        front = (front + 1) % size
        print(queue[front])


front = 0
rear = 0

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