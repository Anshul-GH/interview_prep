def minimum_swaps(ratings: list) -> int:
  # get the rating compliment value. That is, lower value is higher rating
  complmnt = [len(ratings)-val+1 for val in ratings]

  len_arr = len(complmnt)

  idx = 0
  swap_counter = 0
  while idx < len_arr:
      if complmnt[idx] != (idx+1):        
          # swap the values with adjacent value if not as per rating compliment
          complmnt[complmnt[idx]-1], complmnt[idx] = complmnt[idx], complmnt[complmnt[idx]-1]
          swap_counter += 1

      idx += 1
  return swap_counter
