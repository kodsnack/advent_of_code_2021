use std::fs::read_to_string;

pub fn main() {
    // aoc1a();
    aoc1b();
}
fn aoc1b() {
    // let numbers = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    let numbers: Vec<i32> = read_to_string("data/1")
        .unwrap()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let mut n_increased = 0;
    let max_n_measures = 3;
    let mut prev: Option<i32> = None;
    let v = vec![0, 0, 0];
    for (i, n) in numbers.iter().enumerate() {
        if i >= max_n_measures - 1 {
            let sum = n + numbers[i - 1] + numbers[i - 2];
            if prev.is_some() && sum > prev.unwrap() {
                n_increased += 1;
                println!("{}", sum);
            }
            prev = Some(sum);
            continue;
        }
    }
    println!("{}", n_increased);
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
