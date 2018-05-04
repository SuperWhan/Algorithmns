SO as my understanding of heap, the first question we solve during the class is: could we make a list as a binary tree? and we find the way to solve it (such as parent is i, and left is 2*i-1, and right is 2*i ect). So in my code, there's no class for the binary tree like Node, element or keys, it mostly based on the list itself. That's mean I turn the txt file into an array, then make it looks better and easier to handle with:
	that's the work of function:string_helper and function:check_helper

Then the Max_heapfy also based on the list itself. use those two helper functions, re_arrange the list using Max_heapfy algorithms.

For the Insert function, since my code is list-base, so it need specific method to insert new element: 
	For example: Insert(your_list, 'alan : 40')  (where the element is alan, and key is 40)

and Maximum and Extract_Max are just focus on the first element of the list.

but my out put is something like :

Lilian : 9001
Adrienne : 8
Yehonatan : 5
Alan : 5
Paul : 2
Agnessa : -1
Yehonatan : -5

but not as the output requir:
Lilian Adrienne Alan Paul Agnessa Yehonatan 

Since I think that's not a big deal, it is just about the list edit, what I need to show is the understanding of heapfy, so I just let it be like this, or if it is neccessary to change, contact me and I'll use helper function to make it looks good


for running code, just use:

./run.sh input.txt
