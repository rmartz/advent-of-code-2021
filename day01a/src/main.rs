use std::{io, io::prelude::*};

fn main() {
    println!("{}", part1());
}

fn part1() -> isize {
    let stdin = io::stdin();
    let input = stdin.lock().lines();
    let lines: Vec<String> = match input.map(|line| line).collect() {
        Ok(lines) => lines,
        Err(e) => panic!("{}", e),
    };

    let numbers: Vec<isize> = match lines.iter().map(|line| line.parse::<isize>()).collect() {
        Ok(numbers) => numbers,
        Err(e) => panic!("{}", e),
    };

    let mut count = 0;
    let mut cur = numbers[0];

    for num in numbers {
        if num > cur {
            count += 1;
        }
        cur = num;
    }

    return count;
}
