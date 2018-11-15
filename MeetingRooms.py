def minmeetingrooms(intervals):
    intervals.sort(key = lambda x:x[0]);
    print(intervals);
    numRooms = 0;
    while intervals:
        end = intervals[0][1];
        del intervals[0];
        remove_list = [];
        for i in intervals:
            if i[0] >= end:
                end = i[1];
                remove_list.append(i);
        for i in remove_list:
            intervals.remove(i);
        numRooms = numRooms + 1;
    return numRooms;






a = [[2,15],[36,45],[9,29],[16,23],[4,9]];
print(minmeetingrooms(a));
s = "aaab";
print(s.endswith(""));