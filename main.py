import random

# import classes for the assignment
import page

if __name__ == '__main__':
    pageReferences = []
    for i in range(100) :
        if i == 0 :
            pageReferences.append(random.randint(0,99))
        else :
            x = random.randint(-5, 5)
            if x >= 100 : x -= 100
            pageReferences.append(pageReferences[-1] + x)
    capacity = 8
    fpr_memory = page.Memory(capacity, page.FirstPageReplacementAlgorithm())
    now = 0
    for pageID in pageReferences :
        fpr_memory.access(pageID, now)
    print(f"First Page Replacement had {fpr_memory.pageFaults} page faults.")

