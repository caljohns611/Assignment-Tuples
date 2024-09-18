#question 1 task 1
def making_itineraries_list(itineraries):
    itineraries_list = []

    for index, (trveler_name, origin, destination) in enumerate(itineraries, start=1):
        string_list = (f"Itinerary {index}: {trveler_name} - From {origin} to {destination}.")
        itineraries_list.append(string_list)
    return "\n".join(itineraries_list)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Charles", "Texas", "Flordia")]

result = making_itineraries_list(itineraries)
print(result)