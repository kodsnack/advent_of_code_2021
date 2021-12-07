use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let rows : Vec<&str>= contents.lines().filter(|s| s.chars().count() > 0).clone().collect();
    let mut x = 0;
    let mut y = 0;

    for (_j, v) in rows.iter().enumerate() {
        let action : Vec<&str> = v.split(' ').collect();
        let length = action[1].parse::<i32>().unwrap();
        match action[0] {
            "down" => { y += length }
            "up" => { y -= length }
            "forward" => { x += length }
            _ => {}
        }
    }
    println!("Result: {}", x * y)
}
