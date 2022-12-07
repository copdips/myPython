import sys
import threading
from queue import Queue

from attr import attrib, attrs


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == "shutdown":
                return


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for i in range(10)]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put("prepare table")
        bot.tasks.put("clear table")
    bot.tasks.put("shutdown")

print("Kitchen inventory before service:", kitchen)
for bot in bots:
    bot.start()

for bot in bots:
    bot.join()
print("Kitchen inventory after service:", kitchen)

# when the table number given by sys.argv[1] is large, we will see different Cutlery
# before and after the threading.

# py threadbots_with_error_if_large_number_of_tables.py 100
# Kitchen inventory before service: Cutlery(knives=100, forks=100)
# Kitcheninventoryafterservice: Cutlery(knives=100, forks=100)

# py threadbots_with_error_if_large_number_of_tables.py 10000
# Kitchen inventory before service: Cutlery(knives=100, forks=100)
# Kitchen inventory after service: Cutlery(knives=108, forks=88)
