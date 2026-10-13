def classify(value):
    if value<208:
        return "Below range"
    elif value<=212:
        return "In range"
    else:
        return "Above range"
def calculate_average(total,count):
    return total/count
total_width=0
num_below=0
num_in_range=0
num_above=0
count=int(input("Enter the number of sheets:"))

for a in range(count):
    width=int(input("Enter the paper sheet width:"))
    cl=classify(width)
    print(cl)
    if cl=="Below range":
        num_below=num_below+1
    elif cl=="In range":
        num_in_range=num_in_range+1
    elif cl=="Above range":
        num_above=num_above+1
    total_width=total_width+width
    avg=calculate_average(total_width,count)

print(f"Total width:{total_width}")
print(f"Average width:{avg}")
print(f"Below range:{num_below}")
print(f"In range:{num_in_range}")
print(f"Above range:{num_above}")



