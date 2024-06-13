# lunch.py

def hello():
    print("Hello, user!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lunch_list):
    if not lunch_list:
        print("My lunchbox is empty!")
    else:
        for i, item in enumerate(lunch_list):
            if i == 0:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")

# Calling the functions to test them
hello()

packed_list = pack("sandwich", "chips", "apple")
print(packed_list)

eat_lunch(["sandwich", "chips", "apple"])
eat_lunch([])
