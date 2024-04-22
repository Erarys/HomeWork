from reactivex import of, operators
from reactivex.operators import concat

source = of("Task_1", "Task_2", "Task_3", "Task_4")

while True:
    action = input("Action: ")

    if action == "add":
        added_item = input("Added item: ")
        source = source.pipe(concat(of(added_item)))
    elif action == "del":
        ob = input("Del item: ")
        source = source.pipe(operators.filter(lambda i: i != ob))
    else:
        break

    source.subscribe(
        on_next=lambda i: print("Received {0}".format(i)),
        on_error=lambda e: print("Error Occurred: {0}".format(e)),
        on_completed=lambda: print("Done!")
    )

source.subscribe(
    on_next=lambda i: print("Received {0}".format(i)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!")
)