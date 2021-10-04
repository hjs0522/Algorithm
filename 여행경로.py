def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], [])+[t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            answer.append(stack.pop())
    return answer[::-1]
