pub fn main() {
    let input = include_str!("../input.txt").lines().next().unwrap();
    let pos = input
        .split(",")
        .map(|x| x.parse::<u16>().unwrap())
        .collect::<Vec<u16>>();

    let mut min_fuel_cost = u32::max_value();
    let mut target = 0;
    for i in *pos.iter().min().unwrap()..=*pos.iter().max().unwrap() {
        let cost = get_fuel_cost2(i, &pos);
        if cost < min_fuel_cost {
            min_fuel_cost = cost;
            target = i;
        }
    }
    println!("{} {}", target, min_fuel_cost);
}

fn get_fuel_cost(target: u16, pos: &Vec<u16>) -> u32 {
    let mut total = 0u32;
    for i in pos {
        total += (*i as i32 - target as i32).abs() as u32;
    }
    total
}
fn get_fuel_cost2(target: u16, pos: &Vec<u16>) -> u32 {
    let mut total = 0u32;
    for i in pos {
        let dist = (*i as i32 - target as i32).abs() as u32;
        total += (1..=dist).sum::<u32>();
    }
    total
}
