


 {#main}
SEARCHING AND SORTING {#searching-and-sorting .titles}
=====================

In this section we are going to review searching and sorting algorithms.

Why is sorting so important {#why-is-sorting-so-important .inner-titles}
---------------------------

-   The first step in organizing data is sorting. Lots of tasks become
    easier once a data set of items is sorted
-   Some algorithms like binary search are built around a sorted data
    structure.
-   In accordance to S. Skiena computers have historically spent more
    time sorting than doing anything else. Sorting remains the most
    ubiquitous combinatorial algorithm problem in practice.

Considerations: {#considerations .inner-titles}
---------------

-   How to sort: descending order or ascending order?
-   Sorting based on what? An object name (alphabetically), by some
    number defined by its fields/instance variables. Or maybe compare
    dates, birthdays, etc.
-   What happens with equals keys, for example various people with the
    same name: John, then sort them by Last Name.
-   Does your sorting algorithm sorts in place or needs extra memory to
    hold another copy of the array to be sorted. This is even more
    important in embedded systems.

Java uses Comparable interface for sorting and returns: +1 if compared
object is greater, -1 if compared object is less and 0 if compared
objects are equal.

Sorting becomes more ubiquitous when we think on all the things we do
daily that are previously sorted for us to understand and have better
access to them:

-   Imagine trying to find a phone number in an unsorted phone book, or
    searching for a word in an unsorted dictionary.
-   Your MP3 player can sort your lists by artists name, genre, song
    name, ratings.
-   Search engines display results in descending order of importance
-   Spreadsheets can be sorted in various ways to work better with their
    contents

Searching {#searching .inner-titles}
---------

There are two types of searching algorithms: Those that need a
previously ordered data structure in order to work properly, and those
that don't need an ordered list.

Searching is also very important for many computing applications:
searching through a search engine, finding a bank account balance for
some client, searching in a large data set for a particular value,
searching in your directories for some needed file. Many applications
rely on effective search, if your application is complete but takes long
too perform a search and retrieve data it will be discarded as useless.

 {.division}


SELECTION SORT {#selection-sort .titles}
==============

It is called selection sort because it repeatedly selects the smallest
remaining item:

1.  Find the smallest element. Swap it with the first element.
2.  Find the second smallest element. Swap it with the second element
3.  Find the third smallest element. Swap it with the third element
4.  Repeat finding the smallest element and swapping in the correct
    position until the list is sorted

Implementation in java for selection sort:

 {.code-div}
                        
        public class SelectionSort {
        
           public static void selectionSort(Comparable[] array) {
          
            for (int i = 0; i < array.length; i++) {
             int min = i;
             for (int j = i + 1; j < array.length; j++) {
              if (isLess(array[j], array[min])) {
               min = j;
              }
             }
             swap(array, i, min);
            }
           }
           
           //returns true if Comparable j is less than min
           private static boolean isLess(Comparable j, Comparable min) {
            int comparison = j.compareTo(min);
            return  comparison< 0;
           }
          
           private static void swap(Comparable[] array, int i, int j) {
            Comparable temp = array[i];
            array[i] = array[j];
            array[j] = temp;
           }
          
           public static <E> void printArray(E[] array) {
            for (int i = 0; i < array.length; i++) {
             System.out.print(array[i] + " ");
            }
           }
           
           // Check if array is sorted
           public static boolean isSorted(Comparable[] array) {
            for (int i = 1; i < array.length; i++) {
             if (isLess(array[i], array[i - 1])) {
              return false;
             }
            }
            return true;
           }
           
            public static void main(String[] args) {
              Integer[] intArray = { 34, 17, 23, 35, 45, 9, 1 };
              System.out.println("Unsorted Array: ");
              printArray(intArray);
              System.out.println("\nIs intArray sorted? "
                + isSorted(intArray));
            
              selectionSort(intArray);
              System.out.println("\nSelection sort:");
              printArray(intArray);
              System.out.println("\nIs intArray sorted? "
                + isSorted(intArray));
            
              String[] stringArray = { "z", "g", "c", "o", "a",
                "@", "b", "A", "0", "." };
              System.out.println("\n\nUnsorted Array: ");
              printArray(stringArray);
            
              System.out.println("\n\nSelection sort:");
              selectionSort(stringArray);
              printArray(stringArray);
           }
       }                    
                        
                    


Output is:

 {.code-div}
                            
       Unsorted Array: 
       34 17 23 35 45 9 1 
       Is intArray sorted? false
       
       Selection sort:
       1 9 17 23 34 35 45 
       Is intArray sorted? true
       
       
       Unsorted Array: 
       z g c o a @ b A 0 . 
       
       Selection sort:
       . 0 @ A a b c g o z 
             
           


 {.division}


SHELLSORT {#shellsort .titles}
=========

Shell sort is perfect good for embedded systems as it doesn't require a
lot of extra memory allocation; it is also useful for small to medium
size arrays. Lets see the following implementation in java code:

 {.code-div}
                   
       public class ShellSort {
       
        public static void shellSort(Comparable[] array) {
         int N = array.length;
         int h = 1;
         while (h < N/3) h = 3*h + 1;
         while (h >= 1){
          for (int i=h; i<N ; i++) {
           for(int j=i; j>=h && isLess(array[j], array[j-h]); j-=h){
            swap(array, j, j-h);
           }
          }
          h = h/3;
         }
        }
       
        // returns true if Comparable j is less than min
        private static boolean isLess(Comparable j, Comparable min) {
        
         int comparison = j.compareTo(min);
         return comparison< 0;
         
        }
       
        private static void swap(Comparable[] array, int i, int j) {
        
         Comparable temp = array[i];
         array[i] = array[j];
         array[j] = temp;
         
        }
       
        public static <E> void printArray(E[] array) {
        
         for (int i = 0; i < array.length; i++) {
          System.out.print(array[i] + " ");
         }
         
        }
       
        // Check if array is sorted
        public static boolean isSorted(Comparable[] array) {
        
         for (int i = 1; i < array.length; i++) {
          if (isLess(array[i], array[i - 1])) {
           return false;
          }
         }
         return true;
        }
       
        public static void main(String[] args) {
        
         Integer[] intArray = { 34, 1000, 23, 2, 35, 0, 9, 1 };
         System.out.println("Unsorted Array: ");
         printArray(intArray);
         System.out.println("\nIs intArray sorted? " + isSorted(intArray));
       
         shellSort(intArray);
         System.out.println("\nSelection sort:");
         printArray(intArray);
         System.out.println("\nIs intArray sorted? " + isSorted(intArray));
       
         String[] stringArray = { "z", "Z","999", "g", "c", "o",
             "a", "@", "b", "A","0", "." };
         System.out.println("\n\nUnsorted Array: ");
         printArray(stringArray);
       
         System.out.println("\n\nSelection sort:");
         shellSort(stringArray);
         printArray(stringArray);
        }
       }
                   
                   
                   
                   
                


Output:

 {.code-div}
                   
       Unsorted Array: 
       34 1000 23 2 35 0 9 1 
       Is intArray sorted? false
       
       Selection sort:
       0 1 2 9 23 34 35 1000 
       Is intArray sorted? true
       
       
       Unsorted Array: 
       z Z 999 g c o a @ b A 0 . 
       
       Selection sort:
       . 0 999 @ A Z a b c g o z  
                   
                


 {.division}


MERGESORT {#mergesort .titles}
=========

Mergesort is also called divide and conquer algorithm, because it
divides the original data into smaller pieces of data to solve the
problem. Merge sort works in the following way:

1.  Divide into 2 collections. Mergesort will take the middle index in
    the collection and split it into the left and right parts based on
    this middle index.
2.  Resulting collections are again recursively splited and sorted
3.  Once the sorting of the two collections is finished, the results are
    merged
4.  Now Mergesort it picks the item which is smaller and inserts this
    item into the new collection.
5.  Then selects the next elements and sorts the smaller element from
    both collections

 {.code-div}
                   
       public class MergeSort {
       
           public int[] sort(int [] array){
            mergeSort(array, 0, array.length-1);
            return array;
            
           }
           
           private void mergeSort(int[] array, int first, int last) {
           
            // We need mid to divide problem into smaller size pieces
            int mid = (first + last) / 2;
            
            //If first < last the array must be recursively sorted
            if (first < last) {
             mergeSort(array, first, mid);
             mergeSort(array, mid + 1, last);
            }
            
            //merge solved pieces to get solution to original problem
            int a = 0, f = first, l = mid + 1;
            int[] temp = new int[last - first + 1];
          
            while (f <= mid && l <= last) {
             temp[a++] = array[f] < array[l] ? array[f++] : array[l++];
            }
            
            while (f <= mid) {
             temp[a++] = array[f++];
            }
            
            while (l <= last) {
             temp[a++] = array[l++];
            }
            
            a = 0;
            while (first <= last) {
             array[first++] = temp[a++];
            }
           }
           
           public static void printArray(int[] array) {
            for (int i = 0; i < array.length; i++) {
             System.out.print(array[i] + " ");
            }
            
           }
          
           public static void main(String[] args) {
           
            System.out.println("Original array:");
            int[] example = { 100, 30, 55, 62, 2, 42, 20, 9, 394, 1, 0 };
            printArray(example);
            
            System.out.println("\nMergesort");
            MergeSort merge = new MergeSort();
            merge.sort(example);
            printArray(example);
            
           }
       }  
                      
                


Output:

 {.code-div}
                   
       Original array:
       100 30 55 62 2 42 20 9 394 1 0 
       Mergesort
       0 1 2 9 20 30 42 55 62 100 394   
                   
                


 {.division}


QUICKSORT {#quicksort .titles}
=========

Quick sort is better than merge sort from a memory usage comparison.
Because quick sort doesn't require additional storage to work. It only
uses a small auxiliary stack.

Skiena discovered via experimentation that a properly implemented
quicksort is typically 2-3 times faster than mergesort or heapsort

The pseudo-code for quicksort is:

1.  If the array contains only 1 element or 0 elements then the array is
    sorted.
2.  If the array contains more than 1 element:
3.  Select randomly an element from the array. This is the \"pivot
    element\".
4.  Split into 2 arrays based on pivot element: smaller elements than
    pivot go to the first array, the ones above the pivot go into the
    second array
5.  Sort both arrays by recursively applying the Quicksort algorithm.
6.  Merge the arrays

Quicksort may take quadratic time O(n^2^) to complete but this is highly
improbable to occur. This happens when the partitions are unbalanced.
For example, the first partition is on the smallest item, the second
partition of the next smallest item, so each time the program just
remove one item for each call, leading to a large number of partitions
of large sub arrays .If the collection of elements is previously
randomized the most probable performance time for quicksort is Θ (n log
n). So if you're having problems with performance of quicksort, you can
rearrange randomly elements in the collection this will increase the
probability of quicksort to perform in Θ (n log n).

Implementation of quicksort:

 {.code-div}
                   
       import java.util.Random;
       
       public class QuickSort {
       
           public void quicksort(int[] array) {
            quicksort(array, 0, array.length - 1);
           }
           
           private void quicksort(int[] array, int first, int last) {
            if (first < last) {
             int pivot = partition(array, first, last);
             
             // Recursive call
             quicksort(array, first, pivot - 1);
             quicksort(array, pivot + 1, last);
            }
           }
           
           private int partition(int[] input, int first, int last) {
           
            /*
            *notice how pivot is randomly selected this makes O(n^2) 
            *very low probability
            */
            int pivot = first + new Random().nextInt(last - first + 1); 
            
            swap(input, pivot, last);
            for (int i = first; i < last; i++) {
             if (input[i] <= input[last]) {
              swap(input, i, first);
              first++;
             }
            }
            
            swap(input, first, last);
            return first;
           }
           
           private void swap(int[] input, int a, int b) {
            int temp = input[a];
            input[a] = input[b];
            input[b] = temp;
           }
           
           public static void printArray(int[] array) {
            for (int i = 0; i < array.length; i++) {
             System.out.print(array[i] + " ");
            }
           }
           
           public static void main(String[] args) {
           
            int[] example = { 90, 6456, 20, 34, 65, -1, 54, -15, 
            1, -999, 55, 529, 0 }; 
            System.out.println("Original Array");
            printArray(example);
            System.out.println("\n\nQuickSort");
            QuickSort sort = new QuickSort();
            sort.quicksort(example);
            printArray(example);
            
           }
       }
                   
                


Output:

 {.code-div}
                   
       Original Array
       90 6456 20 34 65 -1 54 -15 1 -999 55 529 0 
       
       QuickSort
       -999 -15 -1 0 1 20 34 54 55 65 90 529 6456
                   
                


 {.division}


LINEAR SEARCH {#linear-search .titles}
=============

This is the most basic type of search, easy to implement and understand
but inefficient for extremely large data sets. Let's look at the
following implementation:

 {.code-div}
                   
       public class LinearSearch {
       
          public static void main(String[] args) {
             int[] array = { 0, 2, 9, 10, 100, -2, -3, 
                            902, 504, -1000, 20, 9923 };
             
             System.out.println(linearSearch(array, 100)); 
             //prints: 100 found at position index: 4
             
             System.out.println(linearSearch(array, -1)); 
             //prints: not found
             
             System.out.println(linearSearch(array, 9923));
             //prints: 9923 found at position index: 11
          }
          
          private static String linearSearch(int[] array, int toSearch){
             String result ="not found";
             
             for (int i=0; i< array.length; i++){
                if(array[i]==toSearch){
                   result = array[i] +" found at position index: " + i;
                   break;
                }
             }
             return result;
          }
       }  
                   
                


 {.division}


BINARY SEARCH {#binary-search .titles}
=============

Binary search is also easy to implement and easy to understand. We
actually make use of binary search without knowing when searching in a
dictionary for a specific word or in a phone book. Technically it's not
the same but it is a very similar process.

We open a dictionary more or less by the middle if the word we are
searching for starts in a letter over the middle, we discard the first
half of the dictionary and now focus more or less by the middle of the
second half. If the word is below the middle of the second half, we
discard the top half and keep applying this same technique until we find
our word

Let's look at the pseudocode to make this idea clearer:

1.  Receive a sorted array of n elements
2.  Compute middle point
3.  If index toSearch is less than array\[mid\] then highestIndex = mid
    -1 (This changes mid)
4.  If index toSearch is greater than array\[mid\] then lowestIndex =
    mid +1
5.  else if index isn\'t greater nor less than array\[mid\], this means
    it\'s equal so return 0
6.  If not greater, less nor equal, then it\'s not in the array so
    return -1

 {.code-div}
                   
       public class BinarySearch {
       
        private BinarySearch(){ } //Constructor
       
        public static int binarySearch(int toSearch, int[]array){
            int lowestIndex = 0;
            int highestIndex = array.length -1;
         
           while (lowestIndex <= highestIndex){
                      int mid = lowestIndex + 
                         (highestIndex - lowestIndex)/2;
       
                       if  ( toSearch < array[mid]) 
                             highestIndex = mid -1;
          
                      else if ( toSearch > array[mid]) 
                                  lowestIndex = mid + 1;
          
                       else if (toSearch==array[mid])
                                   return mid;
           }
           return -1;
        }
        
        public static void main(String[] args) {
         int [] array = { -100, 1 , 2, 3, 4, 5, 100, 999, 10203};
         
         System.out.println(binarySearch(999, array));  //returns index 6
         System.out.println(binarySearch(-100, array)); //returns index 0
         System.out.println(binarySearch(6, array));    //returns index -1
        }
        
       }  
                   
                


Java implements its own .binarySearch() static methods in the classes
Arrays and Collections in the standard java.util package for performing
binary searches on Java arrays and on Lists, respectively. They must be
arrays of primitives, or the arrays or Lists must be of a type that
implements the Comparable interface, or you must specify a custom
Comparator object.

 {.division}


