use std::fs::read_to_string;

fn read_string_to_tuples(filename: &str) -> Vec<(String, i32)> {
    let contents = read_to_string(filename).expect("Something went wrong reading the file");
    let mut tuples: Vec<(String, i32)> = Vec::new();
    for line in contents.lines() {
        let mut split = line.split(" ");
        let first = split.next().unwrap();
        let second = split.next().unwrap();
        tuples.push((first.to_string(), second.parse::<i32>().unwrap()));
    }
    tuples
}

fn main() {
    let (mut x, mut y) = (0, 0);
    for (dir, units) in read_string_to_tuples("input.txt").iter() {
        match dir.as_str() {
            "down" => y += units,
            "up" => y -= units,
            "forward" => x += units,
            "back" => x -= units,
            _ => panic!("Unknown direction: {}", dir),
        }
    }
    println!("1: {}", x * y);
}
