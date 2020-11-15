
#Question 6. How to get unique items and counts of unique items?

items = np.array([1,2,3,4,5,1,2,1,2, 4,5,6,2,2,3,1])

(unique, counts) = np.unique (items,

return_counts=True)

frequencies = np.asarray( (unique, co

unts)).T

print(f'Element : Count')

for i in frequencies: print(f'{i[0]}: {i[1]}')

Element

1: 4

2: 5

3 : 2

4 : 2

5 : 2

: 1