use regex::Regex;
use std::fs;

fn validate1(line: &str) -> bool {
    let re = Regex::new(r"^(\d+)-(\d+) ([a-z]): (.*)$").unwrap();
    let parts = re.captures(line).unwrap();
    let min = parts
        .get(1)
        .map_or("", |m| m.as_str())
        .parse::<usize>()
        .unwrap();
    let max = parts
        .get(2)
        .map_or("", |m| m.as_str())
        .parse::<usize>()
        .unwrap();
    let character = parts.get(3).map_or("", |m| m.as_str());
    let password = parts.get(4).map_or("", |m| m.as_str());
    let total = password.chars().filter(|&x| x.to_string() == character).count();
    if (min <= total) && (total <= max) {
        return true;
    } else {
        return false;
    }
}

fn validate2(line: &str) -> bool {
    let mut parts = line.split(" ");
    let range = parts.next().unwrap().split("-");
    let character: char = parts.next().unwrap().chars().next().unwrap();
    let password = parts.next().unwrap();

    let counter = range
        .filter(|&x| {
            password.chars().nth(x.parse::<usize>().unwrap() - 1)
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
