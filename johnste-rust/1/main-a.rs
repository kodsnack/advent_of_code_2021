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

    for s in contents.split('\n') {

        if s.chars().count() == 0 {
            continue;
        }

        let current = s.parse::<i32>().unwrap();

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
