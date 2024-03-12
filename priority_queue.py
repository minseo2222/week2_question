class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True) 

    def pop(self):
        if self.queue:
            return self.queue.pop(0)[1]  
        else:
            return None  # 큐가 비어있을 경우 None 반환

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index][0] > self.heap[index][0]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and \
                    self.heap[left_child_index][0] > self.heap[smallest][0]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and \
                    self.heap[right_child_index][0] > self.heap[smallest][0]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
