
Numbers = list[13,6543,234,7,90] # Create a List with Numbers

sortet_numbers = sorted(Numbers) # Sort the List from low to high with the sorted() function

sortet_back = sorted(Numbers, reverse=True) # Sort the List from high to low with the sorted(*,reverse=True) function

print("Numbers from high to low:", sortet_back)
print("Numbers from low to high:", sortet_numbers)