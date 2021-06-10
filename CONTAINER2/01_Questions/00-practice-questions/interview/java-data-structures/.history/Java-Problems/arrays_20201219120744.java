static int binarySearch(int[] a, int val)
{
    int left = 0, right = a.length - 1;
    while(left <= right)
    {
        int mid = (left + right) / 2;
        if(a[mid] == val)
        {
            return mid;
        }
        else if(a[mid] > val)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return -1;
}
static int binarySearchWithStreams(int[] a, int val)
{
    List<Integer> list = Arrays.stream(a)
                              .boxed()
                              .collect(Collectors.toList());
    return Collections.binarySearch(list, val);
}
static int binarySearchWithInsertPos(int[] a, int val)
{
    int left = 0, right = a.length - 1;
    while(left <= right)
    {
        int mid = (left + right) / 2;
        if(a[mid] == val)
        {
            return mid;
        }
        else if(a[mid] > val)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return -left;
  }
    return Arrays.stream(a).distinct().toArray();
}
static int findLonelyNumber(int[] a)
{
    int v = a[0];
    for(int i = 1; i < a.length; ++i)
    {
        v ^= a[i];
    }
    return v;
}




// ---------Testin---------------------------------------


