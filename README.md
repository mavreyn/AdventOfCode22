# AdventOfCode22

These are my files from the 2022 Advent of Code challenges put up by Eric Wastl. Advent of Code is a seasonal competition where beginner and professional coders can attempt a variety of plain-text coding challenges to test their ability or as a means of learning a new language.

# How it Works

Each day from December 1 - 25, a new puzzle is opened containing two parts. The puzzle is related to the story for that season; this season was about the elves' journey. An example using smaller numbers and or less data is provided and solution is explained in simple terms to the user. Each user receives a different large dataset with a unique solution that could theoretically be processed manually, but would be much faster with a simple script.

And yes the puzzles get harder with each day. Unfortunately, I was only able to do up to puzzle number eight giving no more than an hour a day to each puzzle. And even then I couldn't figure out puzzle 7, a tricky file navigation system.

# My Favorite Example

My favorite challenge from AoC 2022 is puzzle 5: the crate moving challenge, the example involves 'crates' being moved from one stack to another with only the top crate being changed during each instruction. The example looked as follows:

```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

Simple enough. However my input looked as follows:

```
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9 

move 4 from 9 to 6
move 7 from 2 to 5
move 3 from 5 to 2
move 2 from 2 to 1
move 2 from 8 to 4
move 1 from 6 to 9
move 1 from 9 to 4
move 7 from 1 to 2
move 5 from 2 to 3
move 5 from 7 to 4
move 5 from 6 to 3
move 1 from 7 to 6
move 2 from 6 to 9
move 3 from 2 to 4
move 4 from 5 to 6
...
```

and there were 500 lines of instructions... The solution was the concatenation of the characters of the boxes at the top of each stack; a string 9 characters long.

There are many other challenges available, and puzzles from Previous years are also available on the website. Enjoy!
