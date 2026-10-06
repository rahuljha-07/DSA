from collections import deque
import sys


# Function to initialize the graph and indegree array
def initializeGraph(v, e, adj, indegree, tokens):
    for i in range(e):
        x = int(next(tokens))
        y = int(next(tokens))
        # Edge from x to y
        adj[x].append(y)
        indegree[y] += 1


# Function to perform topological sorting and calculate job times
def calculateJobTimes(v, adj, indegree):
    # Stores the minimum time to start each job
    jobTime = [0] * (v + 1)
    q = deque()
    # Push all nodes with 0 indegree to the queue
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            # Jobs with no dependencies can start immediately
            jobTime[i] = 1
    # Perform topological sorting and calculate job completion times
    while q:
        currentNode = q.popleft()
        for neighbor in adj[currentNode]:
            jobTime[neighbor] = max(jobTime[neighbor], jobTime[currentNode] + 1)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return jobTime


# Function to display job completion times
def displayJobTimes(jobTime):
    for i in range(1, len(jobTime)):
        print(jobTime[i], end=" ")
    print()


def main():
    tokens = iter(sys.stdin.read().split())
    v = int(next(tokens))
    e = int(next(tokens))
    adj = [[] for _ in range(v + 1)]
    indegree = [0] * (v + 1)
    initializeGraph(v, e, adj, indegree, tokens)
    jobTime = calculateJobTimes(v, adj, indegree)
    displayJobTimes(jobTime)


if __name__ == "__main__":
    main()


'''
Let V=v and E be dependency count; input must be a DAG.
Time: O(V + E): Kahn's queue processes each job once and each dependency
once. Maximum completion time is propagated from ALL predecessors.
Space: O(V) auxiliary jobTime/queue plus O(V + E) input graph/indegrees.
indegree is consumed in place; each job takes one unit of time.
'''
