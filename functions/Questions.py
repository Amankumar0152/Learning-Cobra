cities = ["delhi", "varanasi", "noida", "delhi", "Russia"]

# def print_len(city):
#     print(city)


# def print_list(city):
#     for item in city:
#         print(item, end=" ")

# print_list(cities)

#Q2

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

fact(5)

#Q3
def converter(usd_val):
    inr_val = usd_val * 95.16
    print(usd_val, "USD: ", inr_val, "INR: ")

converter(40)

