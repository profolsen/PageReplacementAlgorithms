class Page :
    def __init__(self):
        self.id = id

class PageReplacementAlgorithm :
    def identifyReplaceablePage(self, frames):
        pass

class FirstPageReplacementAlgorithm(PageReplacementAlgorithm) :
    def identifyReplaceablePage(self, frames):
        return 0

class RandomPageReplacementAlgorithm(PageReplacementAlgorithm) :
    pass #implement this class!

class FIFOPageReplacementAlgorithm(PageReplacementAlgorithm) :
    pass #implement this class!

class LRUPageReplacementALgorithm(PageReplacementAlgorithm) :
    pass #implement this class!

class Memory :
    def __init__(self, capacity, evictor):
        self.frames = []
        self.capacity = capacity
        self.pageFaults = 0
        self.evictor = evictor

    #access the specific pageID at the current time (= now)
    def access(self, pageID, now):
        # see if the page is in frames.
        # if not, increment page fault and
        # first evict a page if there are no empty frames
        # add the page to an empty frame
        pass

    def evict(self):
        frameToFree = self.evictor.identifyReplaceablePage(self.frames)
        self.frames[frameToFree] = None


