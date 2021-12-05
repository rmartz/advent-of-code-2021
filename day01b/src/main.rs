use std::{io, io::prelude::*};

fn main() {
    println!("{}", part2());
}

fn part2() -> isize {
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

    let mut windows: Vec<isize> = [].to_vec();

    let window_size = 3;
    for i in 0..numbers.len() - window_size + 1 {
        let sum = numbers[i .. i + window_size].iter().sum();
        windows.push(sum);
    }

    let mut count = 0;
    let mut cur = windows[0];

    for num in windows {
        if num > cur {
            count += 1;
        }
        cur = num;
    }

    return count;
}
