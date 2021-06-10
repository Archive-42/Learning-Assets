# Algorithms on Graphs: Heaps Demystified

> Much of the algorithms we’ll be discussing in this series will require us to efficiently pull the lowest values in a set of unsorted…

[![Try Khov](https://miro.medium.com/fit/c/56/56/1*lZQW8bISAb2I1oSh2fGZUA@2x.jpeg)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/?source=post_page-----e3e1385ae534--------------------------------)

Much of the algorithms we’ll be discussing in this series will require us to efficiently pull the lowest values in a set of unsorted numbers without looking at every number in the list.

While sorting or traversing a list may appear to be efficient, it gets rather expensive when we have to do these multiple times, especially when we’re constantly updating or adding new elements to the list.

This is where heaps come into play in helping us get the lowest (or highest) values in a much faster way and in this post, we’ll discuss how.

First, let’s talk discuss what a heap exactly is.

Heaps are graphs that have the following properties:

- each node has at most two descending nodes (children nodes)
- the root node has the smallest or highest value of all the values in the graph
- every subtree is itself a heap with the same properties as the overall heap

In the following example, the root node has a value a 3, which is the smallest of all the values in the graph. If we take a look at each subtree, we’ll notice a similar pattern:

![](https://miro.medium.com/max/60/1*B_cYjAO62d8p2KWsDg_8eg.png?q=20)

![](https://miro.medium.com/max/3316/1*B_cYjAO62d8p2KWsDg_8eg.png)

Notice that at the root of each subtree, the value is the smallest value of that subtree. This is what we call a **min-heap**. _If the value was instead the largest, we would call this a_ **_max-heap_**_._

Heaps are commonly represented as array lists. Let’s see how we can translate the visual representation to an array list representation:

![](https://miro.medium.com/max/3462/1*qKdvvy0RV0BZCoXsVaN4zg.png)

There’s a really interesting observation that we make from the array:

![](https://miro.medium.com/max/3450/1*ui0w05jrVJnS3cHaE6jJQQ.png)

From the indices, we can determine the children of each node and vice versa. Here’s an illustration using separate colors to demonstrate which node has which children:

![](https://miro.medium.com/max/3568/1*t7xhyxk3gefUxA6u8P5L7Q.png)

If you haven’t noticed by now, we can use a simple formula to find the index of a child node given the parent’s index.

Assuming index-based 0:

- To find the left child, we use: **_2 \* parent.index + 1_**
- To find the right child, we use: **_2 \* parent.index + 2_**

From the above example:

![](https://miro.medium.com/max/1816/1*OD0FWQWfhWt-cUGdgJo7lg.png)

And what’s great about these equations is that we can use them to find the parents of a given node by simply doing the inverse:

- Find left child’s parent: **_Math.floor(child.index / 2)_**
- Find right child’s parent: **_Math.floor(child.index / 2) -1_**

> **_Note:_** Math.floor() is just a function that drops the decimals of a fraction to give us a whole number

Great! Now that we know what heaps are and how to find children and parents of each node, we can use these ideas to implement the important functions that are used to maintain a heap’s properties whenever a new node is inserted or extracted.

## Insertion and Sift Up

What’s great about an array list is that we can add new elements to its end at **O(1)** time. Since we use them to represent heaps, we can use this nice property to add new nodes easily.

This property is great if the place that we add the node maintains the heap properties. But if it doesn’t, we need to a way to move it to the right place.

Suppose that we have the following min-heap and we want to insert a new node:

![](https://miro.medium.com/max/2670/1*jVzzsRHh5E0SUEefioPCCQ.png)

Parent nodes always add children in the order of left child then right child. This is consistent with our array representation because when we had a new element to the array, we always fill from left to right:

![](https://miro.medium.com/max/3182/1*WKRl7JqWZjPzU7oJ6d_mJQ.png)

Incorrect Insertion

![](https://miro.medium.com/max/2870/1*QdoiC6S0JiMNcpEPbwHucQ.png)

Correct insertion

Now, let’s add another node and suppose that this node is not in the correct position because it is a lower value than the parent.

![](https://miro.medium.com/max/1624/1*7FOzCR6hDmRlMso8UpPrRQ.png)

Let’s take this step by step. When we inserted **node 2**, we see that it is a lower value than its parent, **node 8**. In order for it to be in the correct position, we have to make a swap because **node 2** needs to be the parent of **node 8** in order for the subtree and the overall graph to maintain its heap property.

![](https://miro.medium.com/max/2730/1*8gAcYcBd1YBaFQjMV0NlVA.png)

So now that **node 2** is a parent of **node 8**, we maintained the heap property for that particular subtree **_but_** we failed to satisfy the condition for the overall tree because **node 2** is less than **node 5** but **node 5** is the parent of **node 2**.

So we have to do another swap.

![](https://miro.medium.com/max/3306/1*qu9TLMu2tlAULDEbHORI5w.png)

The method that we call on a node to swap with its parent is called **sift up**.

Here’s the code for **siftUp** in JavaScript:

So the algorithm for adding a node to a heap goes as follows:

1.  add the node to the end of the array list
2.  then compare it to its parents and sift up if needed
3.  repeat sifting up the node until its relationship with its parent is consistent with the heap

Here’s the code for **insertNode** in JavaScript:

## Analysis of Insert and Sift Up

Since we’re using an array list to represent a heap, adding a new element to the end of it takes **O(1)** time. However, we need to move it up to its correct place if we wish to maintain the heap.

Remember that the node that’s being sifted up is swapped with its parent. So its index in the array is being divided by 2 (cut in half) after each swap, which means that sifting up takes **O(log n)** time.

Therefore, inserting and sifting up a node takes **O(log n)** runtime.

## Extraction and Sift Down

The reason why heaps are so great is that they allow us to extract the minimum (or maximum) value of a set of numbers really quickly.

Let’s think about this scenario. Suppose you had a regular array and you wanted to get and remove the smallest value. You could do two things:

1.  Search the array for the smallest value
2.  Sort the array and get the smallest value

Both of these operations seem pretty efficient. After all, searching the array just takes **O(n)** time while sorting takes **O(n \* log n)** (assuming you’re using the most efficient sorting algorithms).

But let’s suppose that instead of doing this just once, you have to do it multiple times. The two operations end up becoming expensive in the long run, especially when values in the array get updated between operations.

This is where heaps shine in getting the smallest (or largest) value in a shorter amount of time. Let’s look at this example of a min-heap:

![](https://miro.medium.com/max/1370/1*NSgrXoL-8WFdrsyPoEzEKw.png)

By definition, the minimum value of a min-heap is the root node. To just get the value, we can simply just call **heap\[0\]** and it’ll have **O(1)** cost. Pretty cool right?

Now let’s suppose we wanted to get the minimum value and remove it from the heap. Instead of pulling from the root directly and go through the trouble of fixing all the remaining nodes to maintain the heap, let’s just swap the root node with the last node:

![](https://miro.medium.com/max/3622/1*BcShVsEaRXvAf84LDHed4g.png)

Since we’re using an array list to represent the heap, we can easily remove the last value of the array list with an **O(1)** cost.

But we have an issue. The root is no longer the minimum value and because of that, we no longer have a heap.

![](https://miro.medium.com/max/864/1*sKc9HM8laVCBSaM7i0z13Q.png)

But don’t panic! We do have a way to correct this. Let’s do something similar to what we did with our **siftUp** method but in the opposite direction.

Before we can start moving, we need to ask which node is the lowest among **node 12**’s children? This is important because we need to have the lowest value as the new root in order to maintain the heap. While it’s obvious in the image above, let’s walk through it step by step:

![](https://miro.medium.com/max/3048/1*_IgkvqWBqFkqBC1570jgFw.png)

The idea here is that we want to find the smallest values among these three nodes. If **12 > 5**, we need to check if **5** is the smallest value by comparing it with **7**. Since **5** is not greater than **7**, we know that **5** is the smallest value so we swap **12** with **5**.

> Note: If the root was indeed the smallest value among the three nodes, then it’s already in the correct place and we wouldn’t have to do anything.

![](https://miro.medium.com/max/2156/1*QM9e4UInFKNgS38vA-dctg.png)

And just like **siftUp**, we apply the same logic going down as we compare **12** with its new children and so on until the overall heap is maintained.

![](https://miro.medium.com/max/3070/1*I7LGB2yMnz7BFtnwCWcoSA.png)

![](https://miro.medium.com/max/2850/1*biD6PdwzoKQN8ZPWTmSWvQ.png)

Here’s the code for **siftDown**:

Here’s the code for **extractMin**:

## Analysis of Extract and Sift Down:

So extracting the root really boils down to swapping the root with the last node, moving the new root down until we have a new heap and then return the old root.

Since the swapping and extracting takes **O(1)** time, the bottleneck is really positioning the interim root to its correct place to maintain the heap.

Since **siftDown** is really just **siftUp** but going in the opposite direction, the runtime for both **extractMin** and **siftDown** is **O(log n)**.

The benefit of using heaps is that extracting the minimum (or maximum) value of a list of numbers is relatively faster than traversing the whole list or sorting it. We found that we can do it in **O(log n)** runtime as opposed to **O(n)** or **O(n \* log n)** and this difference will save us a lot of time in the long run, especially if we’re asked to repeat this process multiple times in an algorithm.

- Heaps come in two types: min-heaps or max-heaps
- Heaps are used to find the minimum (or maximum) value of a list of numbers without needing to sort or traverse the list.
- Heaps are commonly represented as array lists
- The indices in the array list allows us to find the parents or children of a particular node
- Each time a new node is inserted, it must be sifted up to the correct position in order to maintain the heap property. This is done in **O(log n)** time.
- Each time a root is extracted, it must be swapped with the last node, the new root must be sifted down to the correct position to maintain the heap property, and then the former root can be removed from the end of the list. This can be done in **O(log n)** time.

[Source](https://trykv.medium.com/algorithms-on-graphs-the-importance-of-heaps-e3e1385ae534)
