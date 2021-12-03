use std::fs::read_to_string;

fn main() {
    aoc1a();
}

fn aoc1a() {
    // let test = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    let numbers: Vec<i32> = read_to_string("data/1")
        .unwrap()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let mut n_increased = 0;
    let mut prev: Option<i32> = None;
    for n in numbers {
        if prev.is_some() && n > prev.unwrap() {
            n_increased += 1;
        }
        prev = Some(n);
    }
    println!("{}", n_increased);
}
