from enum import Enum
from collections import defaultdict
import bisect
from datetime import datetime, timedelta

class EventType(Enum):
    IMPRESSION = "impression"
    CLICK = "click"

class AdEvent:
    def __init__(self, adId: int, date: str, eventType: EventType):
        self.adId = adId
        self.date = date
        self.eventType = eventType

class AdAnalytics:
    def __init__(self):
        self.adMap = defaultdict(list)
    
    def consumeAdEvent(self, adEvent: AdEvent)->None:
        adData = self.adMap[adEvent.adId]

        temp = [adEvent.date, 0, 0]

        idx = bisect.bisect_left(adData, temp)

        if idx<len(adData) and adData[idx][0] == adEvent.date:
            if adEvent.eventType == EventType.IMPRESSION:
                adData[idx][1] += 1
            else:
                adData[idx][2] += 1
        else:
            if adEvent.eventType == EventType.IMPRESSION:
                temp[1] += 1
            else:
                temp[2] += 1
            
            adData.insert(idx, temp)
    
    def getDailyAdEventHistory(self, adId: int) -> list:
        return self.adMap[adId]

    def getPastDate(self, date: str, y: int)->str:
        dtobject = datetime.strptime(date, "%Y-%m-%d")

        pastDate = dtobject - timedelta(days=y)

        return pastDate.strftime("%Y-%m-%d")


    def isCappedAt(self, adId: int, Addate: str, x:int, y:int)->bool:
        adDataList = self.adMap[adId]
        end = bisect.bisect_left(adDataList, [Addate,0,0])
        startDate = self.getPastDate(Addate, y)
        start = bisect.bisect_left(adDataList, [startDate,0,0])

        end = min(len(adDataList)-1, end)

        if start >= len(adDataList):
            return False
        
        icount = 0 
        ccount = 0

        for i in range(start, end+1):
            icount += adDataList[i][1]
            ccount += adDataList[i][2]
            if ccount>0:
                return False
        
        if icount >= x:
            return True
        else:
            return False
    

if __name__=="__main__":
    analytics = AdAnalytics()

    # -----------------------------
    # Test 1: Single impression
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-01", EventType.IMPRESSION)
    )

    print("Test 1:")
    print(analytics.getDailyAdEventHistory(1))
    print()

    # Expected:
    # [["2025-04-01", 1, 0]]

    # -----------------------------
    # Test 2: Multiple impressions same day
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-01", EventType.IMPRESSION)
    )

    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-01", EventType.IMPRESSION)
    )

    print("Test 2:")
    print(analytics.getDailyAdEventHistory(1))
    print()

    # Expected:
    # [["2025-04-01", 3, 0]]

    # -----------------------------
    # Test 3: Add click same day
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-01", EventType.CLICK)
    )

    print("Test 3:")
    print(analytics.getDailyAdEventHistory(1))
    print()

    # Expected:
    # [["2025-04-01", 3, 1]]

    # -----------------------------
    # Test 4: Multiple dates
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-02", EventType.IMPRESSION)
    )

    analytics.consumeAdEvent(
        AdEvent(1, "2025-04-03", EventType.IMPRESSION)
    )

    print("Test 4:")
    print(analytics.getDailyAdEventHistory(1))
    print()

    # Expected:
    # [
    #   ["2025-04-01", 3, 1],
    #   ["2025-04-02", 1, 0],
    #   ["2025-04-03", 1, 0]
    # ]

    # -----------------------------
    # Test 5: Should NOT be capped
    # because click exists
    # -----------------------------
    result = analytics.isCappedAt(
        1,
        "2025-04-03",
        x=3,
        y=7
    )

    print("Test 5:")
    print(result)
    print()

    # Expected: False

    # -----------------------------
    # Test 6: Capped case
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(2, "2025-04-01", EventType.IMPRESSION)
    )

    analytics.consumeAdEvent(
        AdEvent(2, "2025-04-02", EventType.IMPRESSION)
    )

    analytics.consumeAdEvent(
        AdEvent(2, "2025-04-03", EventType.IMPRESSION)
    )

    analytics.consumeAdEvent(
        AdEvent(2, "2025-04-03", EventType.IMPRESSION)
    )

    result = analytics.isCappedAt(
        2,
        "2025-04-03",
        x=3,
        y=7
    )

    print("Test 6:")
    print(result)
    print()

    # Expected: True

    # -----------------------------
    # Test 7: Not enough impressions
    # -----------------------------
    result = analytics.isCappedAt(
        2,
        "2025-04-03",
        x=10,
        y=7
    )

    print("Test 7:")
    print(result)
    print()

    # Expected: False

    # -----------------------------
    # Test 8: Rolling window
    # old event should not count
    # -----------------------------
    analytics.consumeAdEvent(
        AdEvent(2, "2025-03-01", EventType.IMPRESSION)
    )

    result = analytics.isCappedAt(
        2,
        "2025-04-03",
        x=4,
        y=7
    )

    print("Test 8:")
    print(result)
    print()

    # Expected: True

    # -----------------------------
    # Test 9: Empty ad
    # -----------------------------
    result = analytics.isCappedAt(
        999,
        "2025-04-03",
        x=1,
        y=7
    )

    print("Test 9:")
    print(result)
    print()





    



