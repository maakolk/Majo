from rotaryEncoder.helper.slicer import Slices
from unittest import TestCase


class TestSlices(TestCase):

    def test_nextSector(self):

        sl = Slices(3, 180, 360);
        hasNext = True
        results = []

        while hasNext:
            result = (sl.nextInterval())
            hasNext = result[2]
            print(result)
            results.append(result)

        self.assertEquals(3, len(results))
        self.assertEquals((180,240,True), results[0])
        self.assertEquals((240,300,True), results[1])
        self.assertEquals((300,360,False), results[2])
