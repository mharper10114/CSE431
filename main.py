"""
Author: Matthew Harper
File: main.py
"""

import random
import time
import matplotlib.pyplot as plt
import numpy as np


def merge_sort(arr):
    """
    Merge sort algorithm.
    Merge sorting algorithm was found from Geeks for Geeks at the link listed below.
    https://www.geeksforgeeks.org/merge-sort/
    :param arr: An unsorted array
    :return: None
    """
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    """
    Insertion sort algorithm
    Insertion sorting algorithm was found from Geeks for Geeks at the link listed below:
    https://www.geeksforgeeks.org/insertion-sort/
    :param arr: An unsorted array
    :return: none
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    merge_times = []
    insertion_times = []
    for x in range(1, 1000):
        unsorted_merge = []
        unsorted_insertion = []

        for i in range(0, x):
            val = random.randint(0, 1000)
            unsorted_merge.append(val)
            unsorted_insertion.append(val)

        merge_start = time.time()
        merge_sort(unsorted_merge)
        merge_time = time.time() - merge_start
        merge_times.append(merge_time)

        insertion_start = time.time()
        insertion_sort(unsorted_insertion)
        insertion_time = time.time() - insertion_start
        insertion_times.append(insertion_time)

    x_values = list(range(len(merge_times)))
    plt.scatter(x_values, merge_times, label="Merge Sort")
    m_merge, b_merge = np.polyfit(np.asarray(x_values), np.asarray(merge_times), 1)
    plt.plot(x_values, (m_merge * np.asarray(x_values)) + b_merge, 'r')
    plt.xlabel("Size of List")
    plt.ylabel("Runtime")
    plt.title("Merge Sort Times")
    plt.legend()
    plt.show()

    plt.scatter(x_values, insertion_times, label="Insertion Sort")
    m_insert, b_insert = np.polyfit(np.asarray(x_values), np.asarray(insertion_times), 1)
    plt.plot(x_values, (m_insert * np.asarray(x_values)) + b_insert, 'r')
    plt.xlabel("Size of List")
    plt.ylabel("Runtime")
    plt.title("Insertion Sort Times")
    plt.legend()
    plt.show()

    plt.plot(x_values, (m_insert * np.asarray(x_values)) + b_insert, 'r', label="Insertion Sort")
    plt.plot(x_values, (m_merge * np.asarray(x_values)) + b_merge, label="Merge Sort")
    plt.xlabel("Size of List")
    plt.ylabel("Runtime")
    plt.title("Insertion Sort vs Merge Sort")
    plt.legend()
    plt.show()

    return 0


if __name__ == "__main__":
    main()
