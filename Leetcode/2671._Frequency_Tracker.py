class FrequencyTracker:

    def __init__(self):
        self.numFreq = {}
        self.freqCount = {}

    def add(self, number: int) -> None:
        old = self.numFreq.get(number, 0)
        new = old + 1
        if old > 0:
            self.freqCount[old] -= 1
            if self.freqCount[old] == 0:
                del self.freqCount[old]
        self.freqCount[new] = self.freqCount.get(new, 0) + 1
        self.numFreq[number] = new

    def deleteOne(self, number: int) -> None:
        if number not in self.numFreq:
            return
        old = self.numFreq[number]
        new = old - 1
        self.freqCount[old] -= 1
        if self.freqCount[old] == 0:
            del self.freqCount[old]
        if new > 0:
            self.freqCount[new] = self.freqCount.get(new, 0) + 1
            self.numFreq[number] = new
        else:
            del self.numFreq[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqCount
