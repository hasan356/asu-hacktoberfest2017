def selection(numbers):
	
	# Traverse through the array
	for i in range(len(numbers)): 
	    
	    # Find the index of the minimum element in remaining sorted array  
	    min_index = i 
	    for j in range(i+1, len(numbers)): 
	        if numbers[min_index] > numbers[j]: 
	            min_index = j 
	    
	    # Swap the found minimum element with this index
	    numbers[i], numbers[min_index] = numbers[min_index], numbers[i] 

	#return the sorted array
	return numbers