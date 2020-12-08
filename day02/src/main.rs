use std::fs;

fn validate1(line: &str) -> bool {
    let mut parts = line.split(" ");
    let mut range = parts.next().unwrap().split("-");
    let min = range.next().unwrap().parse::<usize>().unwrap();
    let max = range.next().unwrap().parse::<usize>().unwrap();
    let character: char = parts.next().unwrap().chars().next().unwrap();
    let password = parts.next().unwrap();
    let total = password.chars().filter(|&x| x == character).count();
    if (min <= total) && (total <= max) {
        return true;
    } else {
        return false;
    }
}

fn validate2(line: &str) -> bool {
    let mut parts = line.split(" ");
    let mut range = parts.next().unwrap().split("-");
    let character: char = parts.next().unwrap().chars().next().unwrap();
    let password = parts.next().unwrap();

    let counter = range
        .filter(|&x| {
            password
                .chars()
                .nth(x.parse::<usize>().unwrap() - 1)
                == Some(character)
        })
        .count();

    if counter == 1 {
        return true;
    } else {
        return false;
    }
}

fn main() {
    println!(
        "{}",
        fs::read_to_string("../day02-1.txt")
            .unwrap()
            .trim()
            .split("\n")
            .filter(|&x| validate1(x))
            .count()
    );

    println!(
        "{}",
        fs::read_to_string("../day02-1.txt")
            .unwrap()
            .trim()
            .split("\n")
            .filter(|&x| validate2(x))
            .count()
    )
}
