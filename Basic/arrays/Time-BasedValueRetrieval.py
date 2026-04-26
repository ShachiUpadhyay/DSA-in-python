#https://drive.google.com/drive/folders/15VFIdsrnBr9h8TRponKYC4CnrNyyr5Yx
#Time-Based Value Retrieval and System Optimization

# Use to assess L3-L4 SWE
# Data Structures & Algorithms,	Binary Search, Sorting, Hash Table		
# Arrays	
# Question Answer guide

# # Question details

# Let's design a critical component for a Test Automation Framework. 
# Our framework needs to verify the behavior of a system (like an e-commerce site) 
# that has data changing over time. For example, to validate a customer's invoice from last week,
#  our Test Agent must be able to query what the exact price of a product was at the moment of purchase. 
# To do this, the agent is given access to a 'Source of Truth (SoT).
#  The SoT is a list of records sorted chronologically by timestamp. 
# Each record contains information (e.g., price) that is valid from its timestamp up to the timestamp of the next record. 
# Your task is to write a function that takes a sorted list of input timestamps (representing the times to be queried) 
# and efficiently returns the correct record for each one.

# # Background

# Let the candidate know they can assume the following
# The SoT is a list of (timestarp, value) tuples, sorted by tirestamp.
# The queries list (for the core problem) is also sorted by tirestanp
# Boundary Condition: if a query timestamp is earlier than the first timestamp in the SoT, the function should return None (or null)

def getPriceForTimestamps(sot: list[tuple[int, str]], queries: list[int]) -> list[str | None]:
     if not sot:
          return [None] * len(queries)

     result: list[str | None] = []
     sot_index: int = 0
     n = len(sot)
     for query in queries:
          if query < sot[0][0]:
               result.append(None)
               continue
          # Move sot_index forward while next timestamp is <= query
          while sot_index + 1 < n and query >= sot[sot_index + 1][0]:
               sot_index += 1
          result.append(sot[sot_index][1])
     return result


if __name__ == "__main__":
     # Example SoT: (timestamp, value)
     sot = [
          (1, "A"),
          (5, "B"),
          (10, "C"),
          (20, "D")
     ]
     # Example queries
     queries = [0, 1, 3, 5, 9, 10, 15, 20, 25]
     expected = [None, "A", "A", "B", "B", "C", "C", "D", "D"]
     result = getPriceForTimestamps(sot, queries)
     print("SoT:", sot)
     print("Queries:", queries)
     print("Expected:", expected)
     print("Result:  ", result)
     print("PASS" if result == expected else "FAIL")

 
    


    
          
     
     
     