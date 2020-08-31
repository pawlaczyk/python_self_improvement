# derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}
#
# print(derek_dict["f_name"])
# derek_dict["address"] = "215 Nort Street"
# derek_dict["city"] = "Pittsburgh"
# print("Is there a city: ", "city" in derek_dict)
# print(derek_dict.values())
# print(derek_dict.keys())
#
# for k, v in derek_dict.items():
#     print(k,v)
#
# print(derek_dict.get("m_name", "Not Here"))
# del derek_dict["f_name"]
# for i in derek_dict.keys():
#     print(i)
#
# derek_dict.clear()
# for i in derek_dict.keys():
#     print(i)
#
# employees = []
# f_name, l_name = input("Enter Employee name: ").split()
# employees.append({"f_name": f_name, "l_name": l_name})
# print(employees)
#


#######################
customers = []
while True:
    choose = input("Enter a customer: ")[0].lower()
    if choose == "y":
        f_name, l_name = input("Enter Customer name").split()
        customers.append({"f_name": f_name, "l_name": l_name})
    else:
        break

for i in customers:
    print(i)

