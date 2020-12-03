use std::fs;

fn readlines() -> Vec<Vec<char>> {
    let text = match fs::read_to_string("day3.txt") {
        Ok(file) => file,
        Err(err) => panic!("Couldn't readlines {}", err),
    };
    let mut text_vex: Vec<Vec<char>> = Vec::new();
    let lines = text.lines();
    for line in lines {
      let mut sub_vec: Vec<char> = Vec::new();
      for _i in 1..200 {
        for character in line.chars() {
          sub_vec.push(character);
        }
      }
      text_vex.push(sub_vec);
    }
    text_vex
}

fn tree_counter(map: &Vec<Vec<char>>, x: usize, y: usize) -> u128 {
  let mut counter: u16 = x as u16;
  let mut trees: u32 = 0;
  let incrementer: u32 = 1;
  let base_len: usize = map.len();
  for i in (y..base_len).step_by(y) {
    let row = &map[i];
    let indexer: usize = counter.into();
    let cha = row[indexer];
    let chars: char = "#".chars().next().unwrap();
    if cha ==  chars {
      trees += incrementer;
    };
    counter += x as u16;
  };
  trees as u128
}

fn main() {
  let res = readlines();
  println!("Step 3,1: {}",tree_counter(&res,3,1));
  let fres: u128 = tree_counter(&res,3,1) * tree_counter(&res,1,1) * tree_counter(&res,5,1) * tree_counter(&res,7,1) * tree_counter(&res,1,2);
  println!("Some routes: {}",fres);
}