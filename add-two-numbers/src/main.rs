struct Solution {}

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut h1 = l1;
        let mut h2 = l2;
        let mut carry = 0;

        let mut head = ListNode::new(0);

        let mut tail: Option<Box<ListNode>> = None;

        // While both list heads are not none, add to a third list
        let x = h1.is_some();
        while h1.is_some() || h2.is_some() || carry != 0 {
            let mut add = h1.as_ref().unwrap().val + h2.as_ref().unwrap().val + carry;
            carry = 0;
            if add >= 10 {
                carry = 1;
                add = add % 10;
            }
            // Append node TODO
            let tail = Some(Box::new(add));
            let next = tail;
        }
        return head.next;
    }
}

fn main() {
    let mut h1 = ListNode { val: 2, next: None };
    let mut n2 = ListNode::new(4);
    let mut n3 = ListNode::new(3);
    n2.next = Some(Box::new(n3));
    h1.next = Some(Box::new(n2));

    let mut h2 = ListNode { val: 5, next: None };
    let mut n4 = ListNode::new(6);
    let mut n5 = ListNode::new(4);
    n4.next = Some(Box::new(n5));
    h2.next = Some(Box::new(n4));

    let res = Solution::add_two_numbers(Some(Box::new(h1)), Some(Box::new(h2)));

    // let nums = vec![2, 7, 11, 15];
    // let target = 9;
    // let res = Solution::two_sum(nums, target);
    // print!("{:?}", res);
}
