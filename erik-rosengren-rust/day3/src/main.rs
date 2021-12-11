use std::fs::File;
use std::io::Read;

fn get_number_from_binary_string(binary_string: &str) -> u32 {
    let mut number = 0;
    for (i, c) in binary_string.chars().enumerate() {
        if c == '1' {
            number += 1 << binary_string.len() - i - 1;
        }
    }
    number
}
fn inverter(input: &str) -> String {
    let mut output = String::new();
    for c in input.chars() {
        if c == '0' {
            output.push('1');
        } else {
            output.push('0');
        }
    }
    output
}
fn read_file_to_word_vec(file_name: &str) -> Vec<String> {
    let mut file = File::open(file_name).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
    let mut words = Vec::new();
    for word in contents.split_whitespace() {
        words.push(word.to_string());
    }
    words
}

fn main() {
    part1();
    let oxygen_generator_rating = part2(false);
    let co2_scrubber_rating = part2(true);
    println!("Oxygen generator rating: {}", oxygen_generator_rating);
    println!("Co2 scrubber rating: {}", co2_scrubber_rating);
    println!(
        "Total rating: {}",
        oxygen_generator_rating * co2_scrubber_rating
    );
}

fn part1() {
    let numbers = read_file_to_word_vec("input.txt");
    let middle = numbers.len() / 2;
    let mut index_count = vec![0; numbers.first().unwrap().chars().count()];

    for n in numbers {
        for (i, c) in n.chars().enumerate() {
            if c == '1' {
                index_count[i] += 1;
            }
        }
    }
    let mut binstr: String = String::new();
    index_count.iter().for_each(|x| {
        let bit = if x < &middle { 0 } else { 1 };
        binstr += &bit.to_string();
        println!("{} {}", x, bit);
    });
    let gamma_rate = get_number_from_binary_string(binstr.as_str());
    let epsilon_rate = get_number_from_binary_string(&inverter(binstr.as_str()));
    println!("{} {}", binstr.as_str(), inverter(binstr.as_str()));
    println!("{} {}", gamma_rate, epsilon_rate);
    let power = gamma_rate * epsilon_rate;
    println!("{}", power);
}

fn part2(invert: bool) -> u32 {
    let mut numbers = read_file_to_word_vec("input.txt");
    let n_bits = numbers.first().unwrap().chars().count();
    for i in 0..n_bits {
        let mut one_balance = 0;
        //
        for n in &numbers {
            if !n.is_empty() && n.chars().nth(i).unwrap() == '1' {
                one_balance += 1;
            } else {
                one_balance -= 1;
            }
        }
        let bit = if one_balance < 0 { '0' } else { '1' };
        println!("{} {}", one_balance, bit);
        if invert {
            numbers.retain(|n| n.chars().nth(i).unwrap() != bit);
        } else {
            numbers.retain(|n| n.chars().nth(i).unwrap() == bit);
        }
        if numbers.len() == 1 {
            break;
        }
    }
    println!("{}", numbers.first().unwrap());
    get_number_from_binary_string(numbers.first().unwrap().as_str())
}
