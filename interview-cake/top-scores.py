def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time

    '''
    - Go through the list and add values to a new list
    - where index is  the score and value is the count of that score
    - go through this list, appending

    '''


    # make a reference counter for all possible scores
    counter = [0] * (highest_possible_score + 1)

    # populate counter object
    for score in unsorted_scores:
        counter[score] += 1

    # create empty sorted array
    sorted_scores = []

    # go backwards through the counter, adding values based on count
    for ind in range(len(counter) - 1, -1, -1):
        count = counter[ind]

        for time in range(count):
            sorted_scores.append(ind)


    return sorted_scores