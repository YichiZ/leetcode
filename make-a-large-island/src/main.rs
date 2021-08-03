struct Solution {}

impl Solution {
    pub fn island_size(grid: &Vec<Vec<i32>>, x: usize, y: usize) -> i32 {
        // Try to see horizontal and vertical, add the stack
        // See if I can go top, right, bottom, left

        // Need some form of recursion
        // If island size is 2 x 2
        // Need to check grid total size
        let mut i = y;
        let mut j = x;

        let mut count = 1;

        // check position and need to keep track of the path already done

        if grid[j][i] == 0 {
            panic!("this should not happen")
        }
        // check top

        if i > 0 {
            match grid.get(i - 1) {
                Some(val) => match val.get(j) {
                    Some(val2) => {
                        if *val2 == 1 {
                            count += Solution::island_size(grid, i - 1, j);
                        }
                    }
                    _ => (),
                },
                _ => (),
            }
        }

        // check right
        match grid.get(i) {
            Some(val) => match val.get(j + 1) {
                Some(val2) => {
                    if *val2 == 1 {
                        count += Solution::island_size(grid, i, j + 1);
                    }
                }
                _ => (),
            },
            _ => (),
        }

        // check bottom
        match grid.get(i + 1) {
            Some(val) => match val.get(j) {
                Some(val2) => {
                    if *val2 == 1 {
                        count += Solution::island_size(grid, i + 1, j);
                    }
                }
                _ => (),
            },
            _ => (),
        }

        // check left
        if j > 0 {
            match grid.get(i) {
                Some(val) => match val.get(j - 1) {
                    Some(val2) => {
                        if *val2 == 1 {
                            count += Solution::island_size(grid, i, j - 1);
                        }
                    }
                    _ => (),
                },
                _ => (),
            }
        }
        return count;
    }

    pub fn largest_island(grid: Vec<Vec<i32>>) -> i32 {
        // Keep track of a starting position
        return 0;
    }
}

fn main() {
    // [[1, 0],
    //  [1, 1]]
    let grid = vec![vec![1, 0], vec![1, 1]];

    let res = Solution::island_size(&grid, 0, 0);
    //let res = Solution::largest_island(grid);

    println!("{}", res);
}
