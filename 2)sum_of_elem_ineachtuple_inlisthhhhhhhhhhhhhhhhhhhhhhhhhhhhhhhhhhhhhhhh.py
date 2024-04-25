#Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.



List_of_tuples = [(1, 2), (2, 3), (3, 4)]

sum_of_tuples = [sum(t) for t in List_of_tuples]

print("list of tuples",List_of_tuples)
print(sum_of_tuples)

#output : [3, 5, 7]