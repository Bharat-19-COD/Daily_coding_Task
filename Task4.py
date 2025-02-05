# What is the time, space complexity of following code :

# int a = 0, b = 0; 
# for (i = 0; i < N; i++) { 
#     for (j = 0; j < N; j++) { 
#         a = a + j; 
#     } 
# } 
# for (k = 0; k < N; k++) { 
#     b = b + k; 

# Time Complexity:

# The first nested loop runs N × N = O(N²).
# The second loop runs O(N).
# Overall, O(N² + N) = O(N²).
                       
# Space Complexity:

# Only a few integer variables are used (O(1)).






