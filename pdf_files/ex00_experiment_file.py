count = 0

def add_one():
    global count
    count += 1

def show_count():
    print(count)

show_count()
add_one()
show_count()