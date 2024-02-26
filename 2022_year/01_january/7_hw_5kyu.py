"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild
west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.
The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).
In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become
directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless
directions removed (W<->E or S<->N side by side).
The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
"NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such.
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.
удалять все рядом стоящие пока не останутся рядом противоположные
"""

# def dirReduc(arr):
#     arr = list(map(lambda x: 1 if x == "NORTH" else -1 if x == "SOUTH" else 2 if x == "EAST" else -2, arr))
#
#     for _ in range(4):
#         i = 0
#         while i < len(arr) - 1:
#             if abs(arr[i]) == abs(arr[i + 1]):
#                 arr.pop(i + 1)
#                 arr.pop(i)
#             else:
#                 i += 1
#
#     return list(map(lambda x: "NORTH" if x == 1 else "SOUTH" if x == -1 else "EAST" if x == 2 else "WEST", arr))

"""
решил не я!!!
принцип алгоритма:
проходим через цикл по всем элементам - удаляем пару, если она противоположна
запускаем цикл сначала
каждый раз после удаления пары - запускаем цикл сначала
и когда противоположных пар не останется - выходим из цикла
"""
def dirReduc(arr):
    while True:
        retry = False
        for i, val in enumerate(arr):
            if i+1 < len(arr):
                if val == "NORTH" and arr[i+1] == "SOUTH":
                    del arr[i]
                    del arr[i]
                    retry = True
                    break
                if val == "SOUTH" and arr[i+1] == "NORTH":
                    del arr[i]
                    del arr[i]
                    retry = True
                    break
                if val == "WEST" and arr[i+1] == "EAST":
                    del arr[i]
                    del arr[i]
                    retry = True
                    break
                if val == "EAST" and arr[i+1] == "WEST":
                    del arr[i]
                    del arr[i]
                    retry = True
                    break
        if retry == False:
            break
    return arr