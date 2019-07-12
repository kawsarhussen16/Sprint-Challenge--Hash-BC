#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    current_destination = None

    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)
        if tickets[i].source == "NONE":
            current_destination = tickets[i].destination
            route[0] = current_destination

    for i in range(1, length):
        next_destination = hash_table_retrieve(ht, current_destination)
        route[i] = next_destination
        current_destination = next_destination
    return route