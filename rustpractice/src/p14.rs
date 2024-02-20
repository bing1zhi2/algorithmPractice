#[cfg(test)]
pub mod p14 {
    use std::cmp::min;

    pub struct Solution {}

    impl Solution {
        pub fn longest_common_prefix(strs: Vec<String>) -> String {
            // let max_str = strs.iter().max();
            // let min_str = strs.iter().min();
            // // println!("max_str {:?}",max_str.unwrap());
            // // println!("min_str {:?}",min_str.unwrap());

            // let max_chrs = max_str.unwrap().chars();
            // let min_chrs = min_str.unwrap().chars();
            // // println!("{:?} {:?}",max_chrs, min_chrs);
            // let b = max_chrs.zip(min_chrs).take_while(|x| x.0 == x.1);
            // println!("==============b==={:?}",b);
            // let r = b.map(|x| x.0).collect();
            // // println!("==============R==={:?}",r);
            // r
            // // strs.iter()
            if strs.len() == 0 {
                return "".to_string();
            }
            // let answer:String = "".to_string();
            let firststr = &strs[0];
            let mut ans = firststr.to_string();

            for i in 1..strs.len() {
                ans = Self::strcmp(&ans, &strs[i]);
                // firststr = &answer;
                println!("{:?}", ans);
                if ans.len()==0 {
                    break;
                }
                
            }
            ans
            
        }
        pub fn strcmp(str1: &String, str2: &String) -> String {
            let minlen = min(str1.len(), str2.len());
            let mut index: usize = 0;
            for i in 0..minlen {
                if str1.as_bytes()[i] != str2.as_bytes()[i] {
                    break;
                } else {
                    index += 1;
                }
            }
            str1[..index].to_string()
        }
    }
    #[test]
    pub fn test() {
        // let solution = Solution {};
        // let s = "MCMXCIV";
        let strs = vec![
            "flower".to_string(),
            "fzow".to_string(),
            "flight".to_string(),
        ];
        let a = Solution::longest_common_prefix(strs);
        println!("============={}", a);
        // assert_eq!(1994, a.roman_to_int(s.to_string()));
    }
}
