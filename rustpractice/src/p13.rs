// #[cfg(test)]
pub mod p13 {
    use std::{cmp::min, collections::HashMap, hash::Hash};
    pub struct Solution {}
    impl Solution {
        pub fn roman_to_int(self, s: String) -> i32 {
            let mut done_map = HashMap::new();
            let mut m = HashMap::new();
            m.insert("I", 1);
            m.insert("V", 5);
            m.insert("X", 10);
            m.insert("L", 50);
            m.insert("C", 100);
            m.insert("D", 500);
            m.insert("M", 1000);
            m.insert("IV", 4);
            m.insert("IX", 9);
            m.insert("XL", 40);
            m.insert("XC", 90);
            m.insert("CD", 400);
            m.insert("CM", 900);

            //    let b =  &s[0..s.len()];
            // let part1 = &s[0..0];
            // println!("part1 : {}";', part1);
            println!("s len:{:?}", s.len());
            let mut sum: i32 = 0;
            for i in 0..s.len() {
                match done_map.get(&i) {
                    Some(t) => {}
                    None => {
                        let last = min(i + 2, s.len());
                        let b = &s[i..i + 1];
                        let b2 = &s[i..last];
                        println!("i {} b2 {}", i, b2);
                        // let c = b2.to_owned();
                        if ("IV" == b2)
                            || ("IX" == b2)
                            || ("XL" == b2)
                            || ("XC" == b2)
                            || ("CD" == b2)
                            || ("CM" == b2)
                        {
                            // println!("sss");
                            let v = m.get(b2).unwrap();
                            println!("b2 {} add {}", b2, v);
                            for j in i..last {
                                done_map.insert(j, 0);
                            }
                            sum = sum + v;
                            continue;
                        } else {
                            let v = m.get(b).unwrap();
                            println!("b {} add {}", b, v);
                            done_map.insert(i, 0);
                            sum = sum + v;
                        }

                        println!("-------------------- {:?}", b.to_string());
                    }
                }
            }
            println!("{}", sum);
            sum
        }
    }

    #[test]
    pub fn test() {
        let a = Solution {};
        let s = "MCMXCIV";

        assert_eq!(1994, a.roman_to_int(s.to_string()));
    }
}
