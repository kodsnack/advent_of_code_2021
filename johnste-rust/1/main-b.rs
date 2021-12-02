use std::env;
use std::fs;

fn main() {
    let filename = "input.txt";

    // Statements here are executed when the compiled binary is called

    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut last: Option<i32> = None;
    let mut increments = 0;
    let all_contents : Vec<i32>= contents.split('\n').filter(|s| s.chars().count() > 0).map(|s| s.parse::<i32>().unwrap()).clone().collect();

    let i = 3;
    //println!("window: {:?}", );

    for (j, _current) in all_contents.iter().enumerate() {
        if j < 2 {
            continue;
        }

        let current = window(j, all_contents.clone());


        println!("{:?} and {}", last, current);

        match last {
            Some(xlast) => {
                if xlast < current {
                    increments += 1;
                }
                last = Some(current);
                // pattern
                println!("Got {} ", xlast);
            }
            None => {
                // other pattern
                last = Some(current);
                println!("Got nothing");
            }
        }
    }

    println!("Result: {}", increments)


}

fn window(i: usize, numbers: Vec<i32>) -> i32 {
    return numbers[i] + numbers[i-1] + numbers[i-2]
}