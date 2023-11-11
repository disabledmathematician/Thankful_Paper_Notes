def linear_search(L, e):
	for x in range(len(L)):
		if L[x] == e:
			print("{} is at the {} index".format(L[x], x))
			return (L[x], x)
			
def bisection_search(L, e):
	high = len(L)
	low = 0
	guess = int(round((high + low) / 2.0, 0))
	while L[guess] != e:
		if L[guess] > e:
			high = guess
		elif L[guess] < e:
			low = guess
		guess = int(round((high + low) / 2.0, 0))
	print("{} is at the {} index".format(L[guess], guess))
	
# Charles Thomas Wallace Truscott

def insertion_sort(L):
	for j in range(1, len(L)):
		key = L[j]
		i = j - 1
		while i >= 0 and L[i] > key:
			L[i + 1] = L[i]
			i -= 1
		L[i + 1] = key
	return L
	
def sort(left, right):
	outcome = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			outcome.append(left[i])
			i += 1
		else:
			outcome.append(right[j])
			j += 1
	while i < len(left):
		outcome.append(left[i])
		i += 1
	while j < len(right):
		outcome.append(right[j])
		j += 1
	return outcome

def mergeSort(L):
	if len(L) < 2:
		return L[:]
	else:
		half = len(L) // 2
		left = mergeSort(L[:half])
		right = mergeSort(L[half:])
		return sort(left, right)
	
linear_search([x for x in range(1, 10 + 1)], 5)
bisection_search([x for x in range(1, 10 + 1)], 5)
print(insertion_sort([x for x in range(10, 0, -1)]))
print(mergeSort([x for x in range(20, 0, -1)]))
