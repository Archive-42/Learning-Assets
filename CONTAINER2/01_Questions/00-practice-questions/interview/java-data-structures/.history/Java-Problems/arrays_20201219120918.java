static int binarySearch(int[] a, int val)

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






// ---------Testing---------------------------------------
