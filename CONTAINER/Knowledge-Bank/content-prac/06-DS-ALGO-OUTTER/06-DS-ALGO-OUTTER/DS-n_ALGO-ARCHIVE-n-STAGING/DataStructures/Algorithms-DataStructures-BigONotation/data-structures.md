{#main}
DATA STRUCTURES {#data-structures .titles}
===============

Data structures are fundamental constructs around which you build your
application. A data structure determines the way data is stored, and
organized in your computer. Whenever data exists it must have some kind
of data structure in order to be stored in a computer.

## Contiguous or linked data structures {#contiguous-or-linked-data-structures .inner-titles}

Data structures can be classified as either contiguous or linked,
depending whether they are based on arrays or pointers(references):

**Contiguous-allocated structures**, are made of single slabs of memory,
some of these data structures are arrays, matrices, heaps, and hash
tables.

**Linked data structures**, are composed as distinct chunks of memory
linked together by pointers (references). Some of this data structures
are lists, trees, and graph adjacency lists.

## Comparison {#comparison .inner-titles}

Some advantages of linked lists over static arrays are:

- Overflow is more difficult to occur on a linked structures than it
  is in an array. It only happens when the memory is actually full.
- Insertions and deletions are simpler than for contiguous data
  structures such as arrays.
- Linked list don't need to know size on initialization

Advantages of arrays:

- Linked structures require allocating extra space for storing
  pointers.
- Arrays allow efficient access to any item.

{.division}

# ARRAY {#array .titles}

Arrays are the fundamental contiguously allocated data structure. They
have a fixed size and each element can be efficiently located by its
index. Imagine an array is like a street full of houses, one right next
to each other, each house can be easily located by its address (index).

The following is an example of usage of Java\'s implementation of
ArrayList, which is an Array that is resized when needed

{.code-div}

        /*
        * We can determine at the moment of instantiation the capacity
        * of the    ArrayList this gives a little boost in performance,
        * instead of making the array resize constantly
        */
          List<String> exampleList = new ArrayList<>(100);

        /*
         * Don't confuse capacity with size, the following
         * statement outputs 0, as currently the ArrayList
         * size is 0, but it's capacity is 100
         */
          System.out.println(exampleList.size());

          exampleList.add("first");
          exampleList.add("second");
          exampleList.add("third");

          System.out.println(exampleList.size());//prints 3



{.division}

# SET {#set .titles}

A Set is a Collection that cannot contain duplicate elements.

In Java the Set interface contains methods inherited from Collection and
adds the restriction that duplicate elements are prohibited. Java also
adds a stronger contract on the behavior of the equals() and hashCode()
methods, allowing Set instances to be compared meaningfully even if
their implementation types differ. Some methods declared by Set are:

- add( ) Adds an object to the collection
- clear( ) Removes all objects from the collection
- contains( ) Returns true if a specified object is an element within
  the collection
- isEmpty( ) Returns true if the collection has no elements
- iterator( ) Returns an Iterator object for the collection which may
  be used to retrieve an object
- remove( ) Removes a specified object from the collection
- size( ) Returns the number of elements in the collection

Let\'s use an example of Java\'s implementation of set to understand how
it works. First, we need to define the DataType and override the
equals() and hashCode() methods:

{.code-div}

       public class DataType {
        private String name;
        private int number;

        public DataType(String name, int number){
            this.name = name;
            this.number = number;
        }

        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + ((name == null) ? 0 :
             name.hashCode());
            return result;
        }


          /*
          * We override method equals so that objects
          * with same name can't be added to the set,
          * but objects with same numbers can be added
          */
        @Override
        public boolean equals(Object obj) {
            if (obj == null)
                return false;

            if (this.getClass() != obj.getClass())
                return false;

            DataType other = (DataType) obj;
            if (other.name == null)
                    return false;

            return this.name.equals(other.name);
        }

        @Override
        public String toString() {
            return "DataType: name=" + name + ", number=" + number;
        }
       }



Now we can proceed to use the class

{.code-div}

       Set<DataType> example = new HashSet<>();

       DataType data1 = new DataType("first", 1);

       //notice name repeated it's not valid
       DataType data2 = new DataType("first", 1);

       //notice different name but same number it's valid
       DataType data3 = new DataType("second", 1);

       example.add(data1);
       example.add(data2);
       example.add(data3);

       for (DataType x : example){
        System.out.println(x);
       }



the output is:

{.code-div}

       DataType: name=first, number=1
       DataType: name=second, number=1



## Multiset {#multiset .inner-titles}

A multiset is similar to a set but allows repeated values. For Java,
third-party libraries provide multiset functionality

- Apache Commons Collections provides the Bag and SortedBag
  interfaces, with implementing classes like HashBag and TreeBag.

- Google Guava provides the Multiset interface, with implementing
  classes like HashMultiset and TreeMultiset.

This data structure is perfect for when we need to perform statistical
data that needs no sorting, for example calculating the average or
Standard Deviation of a multiset.

{.division}

# STACKS AND QUEUES {#stacks-and-queues .titles}

Arrays, Linked list, Trees are best use to represent real objects,
Stacks & Queues are best to complete _tasks_, they are like a tool to
complete and then discard.

They are useful to manage data in more a particular way than arrays and
lists.

- Queue are first in, first out (FIFO)
- Stack are last in, first out (LIFO)

When to use stacks and queues:

- Use a queue when you want to get things out in the order that you
  put them in.
- Use a stack when you want to get things out in the reverse order
  than you put them in.
- Use a list when you want to get anything out, regardless of when you
  put them in (and when you don\'t want them to automatically be
  removed).

The following is an implementation of Queues in Java, based on the
[course by R.Sedgewick in
coursera](https://www.coursera.org/course/algs4partI)

{.code-div}

       /*This implementation uses a singly-linked list
        * with a static nested class for linked-list nodes.
        * All operations take constant O(1) time in the worst case.
        */
       public class Queue<Generic> implements Iterable<Generic> {
            private Node<Generic> firstNode; // beginning of queue
            private Node<Generic> lastNode; // end of queue
            private int size; // number of elements on queue

            private static class Node<Item> {
                private Item item;
                private Node<Item> next;
            }

            public Queue() {
                firstNode = null;
                lastNode = null;
                size = 0;
            }

            public boolean isEmpty() {
                return firstNode == null;
            }

            public int size() {
                return size;
            }

            public Generic peek() {
                if (isEmpty())
                    throw new NoSuchElementException("Queue underflow");
                return firstNode.item;
            }

            public void enqueue(Generic item) {
                Node<Generic> oldlast = lastNode;
                lastNode = new Node<Generic>();
                lastNode.item = item;
                lastNode.next = null;
                if (isEmpty())
                    firstNode = lastNode;
                else
                    oldlast.next = lastNode;
                size++;
            }

            public Generic dequeue() {
                if (isEmpty())
                    throw new NoSuchElementException("Queue underflow");
                Generic item = firstNode.item;
                firstNode = firstNode.next;

                if (isEmpty())
                    lastNode = null;// to avoid loitering
                size--;
                return item;
            }

            public String toString() {
                StringBuilder s = new StringBuilder();
                for (Generic item : this)
                    s.append(item + " ");
                return s.toString();
            }

            public Iterator<Generic> iterator() {
                return new ListIterator<Generic>(firstNode);
            }

            private class ListIterator<Item> implements Iterator <Item> {
                private Node <Item> current;

                public ListIterator(Node<Item> first) {
                    current = first;
                }

                public boolean hasNext() {
                    return current != null;
                }

                public void remove() {
                    throw new UnsupportedOperationException();
                }

                public Item next() {
                    if (!hasNext())
                        throw new NoSuchElementException();
                    Item item = current.item;
                    current = current.next;
                    return item;
                }
            }

            public static void main(String[] args) {
                Queue<String> q = new Queue<>();
                q.enqueue("FIRST IN");
                q.enqueue(" 2nd ");
                q.enqueue(" 3rd ");

                System.out.println(q.dequeue() + " first out ==> FIFO");
            }
       }



{.division}

# DICTIONARIES {#dictionaries .titles}

A Dictionary is a data structure that maps a **key** to a **value**.This
is useful in cases where you want to be able to access data via a
particular key rather than an integer index.

In Java, Dictionaries are implemented as a Map: The Map interface maps
unique keys to values. A key is an object that you use to retrieve a
value at a later date.

Given a key and a value, you can store the value in a Map object. After
the value is stored, you can retrieve it by using its key.

Following is a simple Map Implementation as an array. Firstly, we create
a class to help store the key and it\'s value in an object:

{.code-div}

       public class Entry<K, V> {
          private final K key;
          private V value;

          public Entry(K key, V value) {
            this.key = key;
            this.value = value;
          }

          public K getKey() {
            return key;
          }

          public V getValue() {
            return value;
          }

          public void setValue(V value) {
            this.value = value;
          }
       }



Then the implementation of map:

{.code-div}

       public class Map<K, V> {
          private int size;
          private int CAPACITY = 16;
          private Entry<K, V>[] entriesArray = new Entry[CAPACITY];

          public void put(K key, V value) {
            boolean insert = true;
            for (int i = 0; i < size; i++) {
                if (entriesArray[i].getKey().equals(key)) {
                    entriesArray[i].setValue(value);
                    insert = false;
                }
            }
            if (insert) {
                growArray();
                entriesArray[size++] = new Entry<K, V>(key, value);
            }
          }

          private void growArray() {
            if (size == entriesArray.length) {
                int newSize = entriesArray.length * 2;
                entriesArray = Arrays.copyOf(entriesArray, newSize);
            }
          }

          public V get(K key) {
            for (int i = 0; i < size; i++) {
                if (entriesArray[i] != null) {
                    if (entriesArray[i].getKey().equals(key)) {
                        return entriesArray[i].getValue();
                    }
                }
            }
            return null;
          }

          public void remove(K key) {
            for (int i = 0; i < size; i++) {
                if (entriesArray[i].getKey().equals(key)) {
                    entriesArray[i] = null;
                    size--;
                    condenseArrayElements(i);
                }
            }
          }

           //Moves backwards elements from start arg
           private void condenseArrayElements(int start){
            for (int i = start; i < size; i++) {
              entriesArray[i] = entriesArray[i+1];
            }
           }

           public int size(){ return size; }

            public Set<K> keySet(){
            Set<K> set = new HashSet<K>();
            for (int i = 0; i < size; i++) {
             set.add(entriesArray[i].getKey());
            }
            return set;
           }

            public static void main(String[] args) {
              Map<String, Integer> mapExample = new Map<>();
               mapExample.put("Key 1", 100);
              System.out.println(mapExample.get("Key 1"));

              mapExample.put("Key 2", 200);
              mapExample.put("Woaah", 100000);
              System.out.println(mapExample.get("Key 2"));

              System.out.println("keySet: " + mapExample.keySet());

              System.out.print("Values: ");
              for (String key : mapExample.keySet()){
               System.out.print(mapExample.get(key) + " ");
              }
                mapExample.remove("Key 2");
              System.out.println("\nkeySet: " + mapExample.keySet());
             }
       }



{.division}
