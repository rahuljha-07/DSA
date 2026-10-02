from collections import deque
import sys


def initializeGraph(v, e, adj, indegree, tokens):
    for i in range(e):
        x = int(next(tokens))
        y = int(next(tokens))
        adj[x].append(y)
        indegree[y] += 1


def calculateJobTimes(v, adj, indegree):
    jobTime = [0] * (v + 1)
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            jobTime[i] = 1
    while q:
        currentNode = q.popleft()
        for neighbor in adj[currentNode]:
            jobTime[neighbor] = max(jobTime[neighbor], jobTime[currentNode] + 1)
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return jobTime


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
