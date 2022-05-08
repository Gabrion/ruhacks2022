import Int
import sqlite3
import func
import readQR

Int.int()
Int.populate()
func.add("Vanco Bay","Vancouver","BC","Canada","5a5a5a","Vancouver Inn","Inn","English","SLE")

print("Search Restaurants: ",func.searchEat("cafeee", "Toronto"))

print("Search Hotels: ",func.searchStay("", "Calgary"))

print("Search Tour Guides: ",func.searchTour("", ""))

print("List of Locations: ",func.Loclist())

print("List of Tour Guides: ",func.Tourlist())

print(readQR.scan())