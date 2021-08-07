# The task of finding a car buyer among friends and friends of friends.
from collections import deque


# List of those who need a car.
def person_who_need_car(name):
    person_who_need_car_list = ["Nikita", "Maxim"]
    return name in person_who_need_car_list


# Graph of friends and friends of friends.
graph = {"Me": ["Maria", "Alice", "Daria"], "Daria": ["Nikita", "Sasha"], "Alice": ["Misha", "Lisa"], "Maria": ["Lida"],
         "Sasha": ["Maxim"], "Nikita": [], "Misha": [], "Lisa": [], "Lida": [], "Maxim": []}


def search_buyer(name):
    search_queue = deque()
    search_queue += graph[name]
    # This is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            if person_who_need_car(person):
                print(f'{person} wants to buy a car!')
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False


search_buyer("Me")
search_buyer("Sasha")