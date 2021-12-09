use std::error::Error;
use std::fs::File;
use std::io::Read;

fn main() {
    part1()
}

fn part1() {
    let boards = load_board("input.txt");
}

// load bingo board from file
fn load_board(filename: &str) {
    let mut file = File::open(filename).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents);
    let mut board = Vec::new();
    let mut boards = Vec::new();
    let mut draws = Vec::new();
    let mut sums = Vec::new();
    let mut sum: u32 = 0;
    for line in contents.lines() {
        if draws.len() == 0 {
            draws = line.split(",").map(|s| s.parse::<u32>().unwrap()).collect();
        } else {
            if line.len() == 0 {
                if board.len() > 0 {
                    boards.push(board);
                    sums.push(sum);
                    sum = 0;
                    board = Vec::new();
                }
                continue;
            }
            let mut row = Vec::new();
            for num in line.split_whitespace() {
                let byte = num.parse::<u32>().unwrap();
                sum += byte;
                row.push(byte);
            }
            board.push(row);
        }
    }
    if board.len() > 0 {
        boards.push(board);
        sums.push(sum);
    }
    // find the winning board
    let mut winning_sum = 0;
    let mut losing_sum = 0;
    let mut winning_draw = 0;
    let mut losing_draw = 0;
    let mut min_n_draws = draws.len();
    let mut max_n_draws = 0;
    for (i, board) in boards.iter().enumerate() {
        let mut temp_sum = sums[i];
        let mut match_count = vec![0; 5];
        let mut bingo = false;
        let mut board_n_draws = vec![0, 0];
        let mut losing_sums = vec![0, 0];

        for (draw_i, draw) in draws.iter().enumerate() {
            for (row_i, row) in board.iter().enumerate() {
                if bingo {
                    break;
                }
                if row.contains(&draw) {
                    temp_sum -= draw;
                    match_count[row_i] += 1;
                    if match_count[row_i] == 5 {
                        bingo = true;
                        println!(
                            "{} bingo at board {}, row {}, draw {}",
                            draw_i, i, row_i, draw
                        );
                        if draw_i < min_n_draws {
                            min_n_draws = draw_i;
                            winning_sum = temp_sum;
                            winning_draw = *draw;
                            println!("{}: draw {}, row{:?}, sum {}", i, draw_i, row, temp_sum);
                        }
                        if draw_i > board_n_draws[0] {
                            board_n_draws[0] = draw_i;
                            losing_sums[0] = temp_sum;
                            // losing_draw = *draw;
                        }
                        // break;
                    }
                }
            }
        }
        // loop through each column of the board
        temp_sum = sums[i];
        match_count = vec![0; 5];
        bingo = false;
        for (draw_i, draw) in draws.iter().enumerate() {
            for col in 0..board[0].len() {
                for row in board {
                    if bingo {
                        break;
                    }
                    if &row[col] == draw {
                        temp_sum -= draw;
                        match_count[col] += 1;
                        if match_count[col] == 5 {
                            println!(
                                "{} bingo at board {}, col {}, draw {}",
                                draw_i, i, col, draw
                            );
                            bingo = true;
                            if draw_i < min_n_draws {
                                min_n_draws = draw_i;
                                winning_sum = temp_sum;
                                winning_draw = *draw;
                                println!("{}: draw {}, col{:?}, sum {}", i, draw_i, col, temp_sum);
                            }
                            if draw_i > board_n_draws[1] {
                                // max_n_draws = draw_i;
                                board_n_draws[1] = draw_i;
                                losing_sums[1] = temp_sum;
                                // losing_draw = *draw;
                            }
                            // break;
                        }
                    }
                }
            }
        }
        let highest_n_draws = board_n_draws[0].min(board_n_draws[1]);
        if highest_n_draws > max_n_draws {
            max_n_draws = highest_n_draws;
            losing_draw = draws[highest_n_draws];
            losing_sum = if board_n_draws[0] < board_n_draws[1] {
                losing_sums[0]
            } else {
                losing_sums[1]
            };
            println!("board {}: draw {}, sum {}", i, highest_n_draws, losing_sum);
        }
    }
    println!("winning draw: {}", winning_draw);
    println!("winning sum: {}", winning_sum);
    println!("product: {}", winning_sum * winning_draw);

    println!("losing draw: {}", losing_draw);
    println!("losing sum: {}", losing_sum);
    println!("product: {}", losing_sum * losing_draw);
}
