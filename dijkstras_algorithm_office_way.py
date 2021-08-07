# Алгоритм Дейкстры связывает с каждым ребром гафа число - вес.
# Граф с весами - взвешенный граф.
# Алгоритм Дейкстры работает с DAG (Directed Acyclic Graph).

# Найти самы быстрый путь от дома до работы(офиса)  если впемя пути дом - парк 6 мин, дом - школа 2 мин,
# парк - школа 1 мин, парк - работа 3 мин, школа - работа 3 мин.
# Таблица по времени в пути между точками (узлами): дом, парк, школа, офис.
graph = {}
graph["home"] = {}
graph["home"]["park"] = 6
graph["home"]["school"] = 2

graph["park"] = {}
graph["park"]["office"] = 3
graph["park"]["school"] = 1

graph["school"] = {}
graph["school"]["office"] = 3
graph["school"]["park"] = 1

graph["office"] = {}

# Стоимость узла (время перехода к узлу от начального узла - дом)
infinity = float("inf")
costs = {}
costs["park"] = 6
costs["school"] = 2
costs["office"] = infinity

# Родители узла
parents = {}
parents["park"] = "home"
parents["school"] = "home"
parents["office"] = None
# Массив для отслеживания уже обработанных узлов
processed = []


# Поиск узла с наименьшей стоимостью среди необработанных
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Перебираем все узлы
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

# Пока не закончатся узлы
while node is not None:
    cost = costs[node]
    # Перебор соседей узла.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Обновить стоимость узла если до него можно добраться быстрее.
        if costs[n] > new_cost:
            costs[n] = new_cost
            # Узел стновится новым родителем.
            parents[n] = node
    # Пометить ка обработанный узел.
    processed.append(node)
    # Найти следующий узел для обработки.
    node = find_lowest_cost_node(costs)

print(f'Время до каждой точки: {costs}.')
print(f'Кротчайший путь через {parents["office"]}.')
print(f'Если выберете самый быстрый путь, доберетесь до офиса за {costs["office"]} минут.')
