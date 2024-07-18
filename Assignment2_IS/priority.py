import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 # for sorting ties

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        # pops and gives highest priority item
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)

    def __contains__(self, item):
        return any(item == node for (_, _, node) in self._queue)

    def remove(self, item):
        new_queue = []
        for priority, index, node in self._queue:
            if node != item:
                new_queue.append((priority, index, node))
        self._queue = new_queue
        heapq.heapify(self._queue)