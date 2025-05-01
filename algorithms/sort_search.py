import matplotlib.pyplot as plt
import seaborn as sns

def draw_bars(arr, colors, ax, pause_time=0.1):
    ax.clear()
    ax.bar(range(len(arr)), arr, color=colors)
    plt.pause(pause_time)

def bubble_sort_visual(arr, filename):
    sns.set()
    fig, ax = plt.subplots()
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            colors = ['yellow' if x == j or x == j + 1 else 'blue' for x in range(len(arr))]
            draw_bars(arr, colors, ax)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    draw_bars(arr, ['green'] * len(arr), ax)
    plt.savefig(filename)
    plt.close()

def insertion_sort_visual(arr, filename):
    sns.set()
    fig, ax = plt.subplots()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            draw_bars(arr, ['yellow' if x == j or x == j + 1 else 'blue' for x in range(len(arr))], ax)
            j -= 1
        arr[j + 1] = key
    draw_bars(arr, ['green'] * len(arr), ax)
    plt.savefig(filename)
    plt.close()

def selection_sort_visual(arr, filename):
    sns.set()
    fig, ax = plt.subplots()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            colors = ['yellow' if x == j or x == min_idx else 'blue' for x in range(len(arr))]
            draw_bars(arr, colors, ax)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    draw_bars(arr, ['green'] * len(arr), ax)
    plt.savefig(filename)
    plt.close()

def quick_sort_visual(arr, filename):
    sns.set()
    fig, ax = plt.subplots()

    def quicksort(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            quicksort(arr, low, p - 1)
            quicksort(arr, p + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            colors = ['yellow' if x == j or x == i else 'blue' for x in range(len(arr))]
            draw_bars(arr, colors, ax)
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    quicksort(arr, 0, len(arr) - 1)
    draw_bars(arr, ['green'] * len(arr), ax)
    plt.savefig(filename)
    plt.close()

def merge_sort_visual(arr, filename):
    sns.set()
    fig, ax = plt.subplots()

    def merge_sort(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)

    def merge(arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        for k in range(l, r + 1):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            draw_bars(arr, ['yellow' if x == k else 'blue' for x in range(len(arr))], ax)

    merge_sort(arr, 0, len(arr) - 1)
    draw_bars(arr, ['green'] * len(arr), ax)
    plt.savefig(filename)
    plt.close()

def linear_search_visual(arr, target, filename):
    sns.set()
    fig, ax = plt.subplots()
    for i in range(len(arr)):
        colors = ['yellow' if x == i else 'blue' for x in range(len(arr))]
        if arr[i] == target:
            colors[i] = 'green'
        draw_bars(arr, colors, ax)
        if arr[i] == target:
            break
    plt.savefig(filename)
    plt.close()

def binary_search_visual(arr, target, filename):
    sns.set()
    fig, ax = plt.subplots()
    arr.sort()
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        colors = ['yellow' if x == mid else 'blue' for x in range(len(arr))]
        if arr[mid] == target:
            colors[mid] = 'green'
        draw_bars(arr, colors, ax)
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    plt.savefig(filename)
    plt.close()