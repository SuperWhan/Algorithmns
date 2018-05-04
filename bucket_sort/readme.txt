for the bucket_sort, what I did is: make 26 buckets for 26 letters (Example: buckets[0] = the bucket for letter 'A' or 'a'), go through the name list, put them into the buckets they should stay (check them from first letter.)

 so if like the inputP4, the return value of bucket_sort will be liek :[[] ,[],[Candy],[]....] (jsut run the buckets_sort before the line: new_lis = []). then for the part below the new_lis = [], checking each buckets, see the elements is more than 10 or not, if it is more than 10, recursively call the bucket_sort, make another 26 buckets, and check the letter after the one checked before (which is i+1 did). If it is not, just insertion_sort this bucket.

at end, I merge them in a string list.

we done!

for running code, just use:

./run.sh input.txt

Goal:
Assume you have a list of names that you want to sort in alphabetical order. Use bucket sort to solve
this problem (i.e. the program should run in average case O(n)). However, use bucket sort recursively
to ensure that each of the final buckets that are sorted via insertion sort contain no more than 10
elements/names. The way you would do this is when sorting each bucket, if there are more than 10
elements/names in the bucket then you would create sub-buckets and run a mini-bucket sort on only the
elements in this large bucket. You may assume there are no spaces in the names and only contain
normal English alphabet characters. Also the first letter of names will be capitalized.

Sample output.txt (sorted name array separated by spaces (no space after final name)):
Candy Mahesh Rishi Svetovid

Sample input.txt (unsorted names separated by spaces (no space after final name)):
Svetovid Candy Rishi Mahesh
