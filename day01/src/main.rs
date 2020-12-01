use itertools::Itertools;
use std::fs;

fn main() {
    let nums = match fs::read_to_string("../day01-1.txt") {
        Ok(x) => x
            .split_terminator("\n")
            .map(|n| n.parse().expect("Yo this is not a number!"))
            .collect::<Vec<i32>>(),
        Err(a) => panic!(a),
    };

    let result: Vec<i32> = nums
        .iter()
        .filter(|&&i| nums.contains(&(2020 - i)))
        .take(1)
        .map(|i| i * (2020 - i))
        .take(1)
        .collect();
    println!("{}", result[0]);

    let result: Vec<i32> = nums
        .iter()
        .permutations(2)
        .filter(|i| nums.contains(&(2020 - i[0] - i[1])))
        .take(1)
        .map(|i| i[0] * i[1] * (2020 - i[0] - i[1]))
        .collect();
    println!("{}", result[0]);
}
