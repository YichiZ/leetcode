use std::collections::HashMap;

struct Solution {}

// optimize
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<String, usize> = HashMap::new();

        for i in 0..nums.len() {
            let value = nums[i];

            let complement = (target - value).to_string();

            match map.get(&complement) {
                Some(&value) => {
                    let result = vec![value as i32, i as i32];
                    return result;
                }
                None => {
                    map.insert(value.to_string(), i);
                }
            }
        }
        panic!("Not found")
    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let res = Solution::two_sum(nums, target);
    print!("{:?}", res);
}
