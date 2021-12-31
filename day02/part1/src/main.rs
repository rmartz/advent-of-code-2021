use std::{io, io::prelude::*};
use std::collections::HashMap;

struct Movement(isize, isize);
struct Action(fn(isize) -> Movement, isize);

struct Closure {
    f: fn(isize) -> Movement,
}

fn line_to_action(directions: &HashMap::<&str, Closure>, line: &str) -> Action {
    let split: Vec<&str> = line.split(" ").collect();
    let closure = directions.get(split[0]).unwrap();
    return Action(closure.f, split[1].parse::<isize>().unwrap())
}

fn add_movement(acc: Movement, add: Movement) -> Movement {
    return Movement(acc.0 + add.0, acc.1 + add.1)
}

fn main() {
    let mut directions = HashMap::<&str, Closure>::new();


    directions.insert("forward", Closure { f: (|x| Movement(x, 0)) });
    directions.insert("down", Closure { f: (|y| Movement(0, y)) });
    directions.insert("up", Closure { f: (|y| Movement(0, -y)) });

    let stdin = io::stdin();
    let displacement = stdin.lock().lines()
        .map(|line| line.unwrap())
        .map(|line| line_to_action(&directions, &line))
        .map(|action| (action.0)(action.1))
        .reduce(|acc, add| add_movement(acc, add)).unwrap();
    println!("{}", displacement.0 * displacement.1)

}
