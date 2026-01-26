import heapq
from dataclasses import dataclass
from typing import Optional, List, Set

@dataclass
class TaskInfo:
    priority: int
    timestamp: int
    version: int = 0

class TaskScheduler:
    def __init__(self):
        self.task_heap = []
        self.task_map = {}
        self.priority_index = {}
    
    def scheduleTask(self, taskId: str, priority: int, timestamp: int) -> None:
        if taskId in self.task_map:
            self.updatePriority(taskId, priority)
            return
        
        heapq.heappush(self.task_heap, (-priority, timestamp, taskId))
        self.task_map[taskId] = TaskInfo(priority, timestamp)
        
        if priority not in self.priority_index:
            self.priority_index[priority] = set()
        self.priority_index[priority].add(taskId)
    
    def executeNext(self) -> Optional[tuple]:
        while self.task_heap:
            neg_priority, timestamp, taskId = heapq.heappop(self.task_heap)
            priority = -neg_priority
            
            if taskId not in self.task_map:
                continue
            
            task_info = self.task_map[taskId]
            if task_info.priority != priority or task_info.timestamp != timestamp:
                continue
            
            del self.task_map[taskId]
            self.priority_index[priority].discard(taskId)
            if len(self.priority_index[priority]) == 0:
                del self.priority_index[priority]
            
            return (taskId, priority, timestamp)
        
        return None
    
    def cancelTask(self, taskId: str) -> bool:
        if taskId not in self.task_map:
            return False
        
        task_info = self.task_map[taskId]
        priority = task_info.priority
        
        del self.task_map[taskId]
        self.priority_index[priority].discard(taskId)
        if len(self.priority_index[priority]) == 0:
            del self.priority_index[priority]
        
        return True
    
    def updatePriority(self, taskId: str, newPriority: int) -> bool:
        if taskId not in self.task_map:
            return False
        
        task_info = self.task_map[taskId]
        old_priority = task_info.priority
        
        if old_priority == newPriority:
            return True
        
        self.priority_index[old_priority].discard(taskId)
        if len(self.priority_index[old_priority]) == 0:
            del self.priority_index[old_priority]
        
        task_info.priority = newPriority
        task_info.version += 1
        
        if newPriority not in self.priority_index:
            self.priority_index[newPriority] = set()
        self.priority_index[newPriority].add(taskId)
        
        heapq.heappush(self.task_heap, (-newPriority, task_info.timestamp, taskId))
        
        return True
    
    def getTasksByPriority(self, priority: int) -> List[str]:
        if priority not in self.priority_index:
            return []
        return list(self.priority_index[priority])

# Example usage
if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    scheduler.scheduleTask("task1", 5, 100)
    scheduler.scheduleTask("task2", 10, 101)
    scheduler.scheduleTask("task3", 10, 99)  # Earlier timestamp
    scheduler.scheduleTask("task4", 3, 102)
    
    print(scheduler.executeNext())  # Should get task3 (priority 10, earliest)
    print(scheduler.executeNext())  # Should get task2 (priority 10)
    
    scheduler.updatePriority("task1", 10)
    print(scheduler.executeNext())  # Should get task1 (updated to priority 10)
    
    scheduler.cancelTask("task4")
    print(scheduler.executeNext())  # Should be None (task4 was cancelled)
    
    scheduler.scheduleTask("task5", 7, 200)
    scheduler.scheduleTask("task6", 7, 201)
    print(scheduler.getTasksByPriority(7))  # ['task5', 'task6']