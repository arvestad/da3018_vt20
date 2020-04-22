/*
 * Implement a max heap
 */


class Heap {
    double heap_array[];
    int n_elems = 0;
    int capacity;

    // Constructor
    Heap(int _capacity) {
        capacity = _capacity;
        heap_array = new double[capacity];
    }

    /**
     * Private method for maintaining the heap.
     * @param i, index of the element to heapify from
     */
    private void heapify(int i) {
        // Implement this!
    }

    public int capacity() {
        return capacity;
    }

    public int size() {
        return n_elems;
    }

    public boolean is_empty() {
        return n_elems == 0;
    }

    /**
     * Add an element to the heap and ensure the heap property
     * Throws an exception if trying to add elements to a full heap.
     * @param x Element to add
     */
    public void insert(double x) throws Exception {
        // Implement this!
    }

    /**
     * Remove and return largest element, and maintain the heap property.
     * Throws an exception if trying to extract an element from an empty heap.
     */
    public double extract_max() throws Exception {
        // Implement this!
    }


    /**
     * For convenience, a small program to test the code.
     * There are better ways of doing this kind of testing!
     *
     */
    static public void main(String args[]) { // A simple test program
        // Declare two heaps. Both should work nicely!
        Heap h1 = new Heap(100);
        Heap h2 = new Heap(10);
        double data[] = {1, 4, 10, 14, 7, 9, 3, 2, 8, 16};


        //
        // Insert 1 element to heap 1, and several to heap 2.
        //
        System.out.println("Inserting data.");
        try {
            h1.insert(7);       // Insert a single element in heap 1

            // Insert several elements in heap 2. Heap 1 must not be affected.
            for (double x: data) {
                h2.insert(x);
            }
        } catch (Exception e) {
            System.err.println("During insertion:");
            System.err.println(e);
            System.exit(1);
        }

        if (h2.size() != data.length) {
            System.err.println("Error! Wrong number of elements in heap 2.");
        }


        //
        // Time to empty heap 2. Does that work?
        //
        try {
            System.out.println("Contents of heap 2:");
            while (! h2.is_empty()) {
                double x = h2.extract_max();
                System.out.println(x);
            }
            if (! h2.is_empty()) {
                System.err.println("Error! Heap 2 has not been emptied!");
            }
            if (h1.size() != 1) {
                System.err.println("Error! Wrong number of elements in heap 1.");
            }

        } catch (Exception e) {
            System.err.println("During extraction:");
            System.err.println(e);
            System.exit(1);
        }

    }
}
