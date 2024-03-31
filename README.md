
### `group_rank`

```c
// group_rank(x, group) : Each element in a group is assigned 
//                        the corresponding rank in this group
// Example: x          : [5, 1, 8, 3, 2, 7, 4, 6]
//          group      : [A, A, B, A, B, B, A, B]
//    --->  group_rank : [4, 1, 4, 2, 1, 3, 3, 2]
// Explain: 
//  For group A, the values in x are [5, 1, 3, 4].
//  When ranked, these should be:
//    5 is the highest, so it gets the rank 4.
//    4 is the next highest, so it gets the rank 3.
//    3 is the next, so it gets the rank 2.
//    1 is the lowest, so it gets the rank 1.
//  Therefore, since group A has values [5, 1, 3, 4] in this order, 
//  the ranks are [4, 1, 2, 3].
```
