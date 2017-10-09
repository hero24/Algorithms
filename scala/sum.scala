/*
  "Corpus delicti" ~ Julian Tuwim
*/

// Gausian sum for first n conescutive numbers
def gaussian_sum(n:Int) = (n/2) * (n + 1)

// Gausian sum for range of numbers from s to n
def gaussian_sum(s:Int,n:Int) = (n/2 + s/2) * (n - s + 1)
