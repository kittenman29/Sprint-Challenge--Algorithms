Add your answers to the Algorithms exercises here.

a) O(n). This function is just comparing 'a' to our input cubed but then setting it to squared, so it's only being run O(n) times.

b) O(n^3). The first for loop involving our input gives this function O(n). The second for loop is iterating through the list one index ahead of the first loop but is also calling our input, giving the function another O(n). So we're at O(n^2) now. The third for loop is doing the same thing as the 2nd for loop so now we're at O(n^3). The last for loop is just iterating through a pre-defined range of k so it isn't going to add any runtime as our inputs grow other than a constant integer.

c) O(n). This is a recursive function but the time complexity is limited at the amount of inputs that we give it.

So many questions. If you drop one egg off floor f and it breaks, can you assume that all eggs would break from f or higher? Is there a max floor height? Min floor height?  
I'm going to make an assumption that it's a minimum of a two story building (n>=2). That way if you're on floor 2 or higher, eggs would break but if you're on the first floor and throw them off(? out?), they wouldn't break. If it's a 1 or 0 story building, what's one floor lower than the first or zero-th floor? So yeah, minimum of a two story building for a base-case otherwise return (f"impossible").

Once I have a proper if statement set up for my base-case, I would define a function, egg_rescue, that takes in one input, n. This function would return a 1 if the egg breaks and a 0 if it doesn't break. I would then do binary search but searching for the lowest floor that returns a 1. I would do this by searching for the highest f where f-1 = 0. So if your first midpoint returns a 0, you would remove the bottom half of the floors and calculate a new midpoint with your remaining floors. If you get a midpoint that returns a 1, you would check the index immediately before it to see if it's a 0 or 1. If it's a 0 you would print out f and say "this is the first floor where the egg breaks".

Binary search is O(log n) time I believe.
