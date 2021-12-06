fn main() {
    part1();
    part2();
}

fn part1() {
    let input = include_str!("../input.txt");
    const size: usize = 1000;
    let matrix: &mut [[u8; size]; size] = &mut [[0; size]; size];
    for line in input.lines() {
        let mut range = vec![[0; 2]; 2];
        for (i, l) in line.split(" -> ").enumerate() {
            let v = l
                .split(",")
                .map(|x| x.parse::<usize>().unwrap())
                .collect::<Vec<usize>>();
            range[i] = [v[0], v[1]];
        }
        if range[0][0] != range[1][0] && range[0][1] != range[1][1] {
            continue;
        }
        let (x1, x2) = if range[0][0] < range[1][0] {
            (range[0][0], range[1][0])
        } else {
            (range[1][0], range[0][0])
        };
        for x in x1..=x2 {
            let (y1, y2) = if range[0][1] < range[1][1] {
                (range[0][1], range[1][1])
            } else {
                (range[1][1], range[0][1])
            };
            for y in y1..=y2 {
                matrix[y][x] += 1;
            }
        }
    }
    // count the number of squares that are greater than 1
    let mut count = 0;
    for i in 0..size {
        for j in 0..size {
            if matrix[i][j] > 1 {
                count += 1;
            }
        }
    }
    println!("{}", count);
}
fn absdiff(a: usize, b: usize) -> usize {
    if a > b {
        a - b
    } else {
        b - a
    }
}

const X: usize = 0;
const Y: usize = 1;
struct Point {
    x: usize,
    y: usize,
}
fn part2() {
    let input = include_str!("../input.txt");
    const size: usize = 1000;
    let mut matrix = vec![[0u8; 1000]; 1000];
    for line in input.lines() {
        let mut range = vec![Point { x: 0, y: 0 }, Point { x: 0, y: 0 }];
        for (i, l) in line.split(" -> ").enumerate() {
            let v = l
                .split(",")
                .map(|x| x.parse::<usize>().unwrap())
                .collect::<Vec<usize>>();
            range[i] = Point { x: v[X], y: v[Y] };
        }
        let is_diag = absdiff(range[0].x, range[1].x) == absdiff(range[0].y, range[1].y);
        if range[0].x != range[1].x && range[0].y != range[1].y && !is_diag {
            continue;
        }

        let reverse = range[0].x > range[1].x;
        let (start, end) = if reverse {
            (&range[1], &range[0])
        } else {
            (&range[0], &range[1])
        };
        for x in start.x..=end.x {
            if is_diag {
                if start.y < end.y {
                    matrix[start.y + (x - start.x)][x] += 1;
                } else {
                    matrix[start.y - (x - start.x)][x] += 1;
                };
            } else {
                if start.y < end.y {
                    for y in start.y..=end.y {
                        matrix[y][x] += 1;
                    }
                } else {
                    for y in end.y..=start.y {
                        matrix[y][x] += 1;
                    }
                }
            }
        }
    }
    // count the number of squares that are greater than 1
    let mut count = 0;
    for i in 0..size {
        for j in 0..size {
            if matrix[i][j] > 1 {
                count += 1;
            }
        }
    }

    println!("{}", count);
}
