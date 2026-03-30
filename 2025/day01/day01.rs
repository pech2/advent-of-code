use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    let mut start = 50;
    let mut zeroes = 0;

    if let Ok(lines) = read_lines("./.input") {
        for line in lines.map_while(Result::ok) {
            let direction = &line[0..1];
            let num = &line[1..].parse::<i32>().unwrap();
            if direction == "L" {
                start -= num;
            } else {
                start += num;
            }
            start %= 100;
            if start == 0 {
                zeroes += 1;
            }
        }
    }
    println!("{}", zeroes);
}
