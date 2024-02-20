#[cfg(test)]
pub mod problem1 {
    use std::collections::HashMap;
    pub struct Solution {}

    impl Solution {
        pub fn two_sum(self, nums: Vec<i32>, target: i32) -> Vec<i32> {
            let mut map = HashMap::new();
            let mut resultv = Vec::new();

            for (i, v) in nums.iter().enumerate() {
                let diff = target - *v;
                let ta_idx = map.get(&diff);
                println!("diff:{:?} ta_idx:{:?}", diff, ta_idx);
                match ta_idx {
                    Some(tidx) => {
                        resultv.push(*tidx);
                        resultv.push(i as i32);
                        break;
                    }
                    None => {
                        map.insert(*v, i as i32);
                    }
                }
                println!("map:{:?} ", map);
            }
            // println!("{:?}",map);
            // println!("{:?}",nums);

            // for (i,v ) in nums.iter().enumerate(){
            //     let diff = target - *v;
            //     let ta_idx = map.get(&diff);
            //     println!("diff:{:?} ta_idx:{:?}", diff, ta_idx);
            //     match ta_idx{
            //         Some(tidx) => {
            //             let c  = i as i32;
            //             if c != *tidx{
            //                 resultv.push(c);
            //                 resultv.push(*tidx);
            //                 break;
            //             }
            //         },
            //         None=>{}
            //     }

            // }
            resultv
        }
    }
    #[test]
    pub fn test() {
        let a = Solution {};
        let nums = vec![3, 2, 4];
        let r = a.two_sum(nums, 6);
    }
}
